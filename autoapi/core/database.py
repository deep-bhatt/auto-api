import os
import psycopg2
from psycopg2.extensions import connection

class DatabaseConnection:
    # NOTE: Inital version of the app maintains and re-uses a single connection to DB.
    # This is to be changed as to support parallism and concurrency.
    conn: connection

    def __init__(self) -> None:
        self.db_host = os.getenv("DB_HOST")
        self.port = 5432
        self.user = 'postgres'
        self.password = 'password'
        self.database = 'autoapidb'

    def connect(self) -> bool:
        db_url = f"postgresql://{self.user}:{self.password}@{self.db_host}:{self.port}/{self.database}"
        DatabaseConnection.conn = psycopg2.connect(db_url)
        return True

    @staticmethod
    def execute_query(query, parameters=None) -> list[dict]:
        try:
            cursor = DatabaseConnection.conn.cursor()
            cursor.execute(query, parameters)

            if cursor.description is not None:
                column_names = [desc[0] for desc in cursor.description]
                rows = cursor.fetchall()
                result = []
                for row in rows:
                    row_dict = dict(zip(column_names, row))
                    result.append(row_dict)
                DatabaseConnection.conn.commit()
                cursor.close()
                return result
            else:
                DatabaseConnection.conn.commit()
                cursor.close()
                return []
        except Exception as e:
            DatabaseConnection.conn.rollback()
            print('some error while running SQL query', e)
            return []

    def bootstrap_database(self) -> bool:
        try:
            cursor = DatabaseConnection.conn.cursor()
            with open('autoapi/core/bootstrap.sql', 'r') as f:
                sql_commands = f.read()
                cursor.execute(sql_commands)
            DatabaseConnection.conn.commit()
            cursor.close()
            return True
        except Exception as e:
            DatabaseConnection.conn.rollback()
            print('some error while bootstrapping database', e)
            return False
