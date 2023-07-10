from autoapi.core.database import DatabaseConnection
from typing import Any

def query_field_by_field_name(field_name: str):
    query = 'SELECT id, field_name, field_type FROM field WHERE field_name = %s'
    results = DatabaseConnection.execute_query(query, (field_name,))
    return results

def query_field_by_uuid(id: str):
    query = 'SELECT id, field_name, field_type FROM field WHERE id = %s'
    results = DatabaseConnection.execute_query(query, (id,))
    return results

def query_field_by_field_type(field_type: str):
    query = 'SELECT id, field_name, field_type FROM field WHERE field_type = %s'
    results = DatabaseConnection.execute_query(query, (field_type,))
    return results

def query_all_field_names():
    query = 'SELECT field_name FROM field'
    results = DatabaseConnection.execute_query(query)
    return results


def _build_conditions_or_where_clause(conditions: dict[str, Any]):
    """
    name = %s OR age = %s
    """
    clause = ''
    for _ in conditions.keys():
        clause += f'd1.field_value = %s OR '

    # not to consider trailing 'OR'
    return clause[:-4]

def build_and_run_api(conditions: dict[str, Any]):
    """
    Dynamically builds a safe SQL query using conditions.

    eg.
        conditions = {
        'name': 'foo',
        'age': 25
        }
    query = 'SELECT * from dataset WHERE name = %s OR age = %s'
    parameters = ('foo', 25)
    """
    clause = _build_conditions_or_where_clause(conditions)
    query = f'''
    SELECT d1.row_id, d1.field_value, f1.field_name, f1.field_type FROM dataset d1
    JOIN field f1
    ON d1.field_id = f1.id
    WHERE {clause}
    '''
    parameters = tuple(conditions.values())
    results = DatabaseConnection.execute_query(query, parameters)
    return results

def fetch_dataset_rows(row_ids: tuple[str]):
    query = '''
    SELECT d.row_id, f.field_name, f.field_type, d.field_value, d.created_at from dataset d
    JOIN field f
    ON f.id = d.field_id
    WHERE row_id IN %s
    ORDER BY row_id'''

    results = DatabaseConnection.execute_query(query, (row_ids,))
    return results
