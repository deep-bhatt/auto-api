from autoapi.core.database import DatabaseConnection
from autoapi.services import common
from uuid import uuid4

def insert_field(df) -> bool:
    column_data_types = df.dtypes.to_dict()

    for column, dtype in column_data_types.items():
        str_dtype = str(dtype)
        simplified_dtype = None

        if str_dtype.startswith('float') or str_dtype.startswith('int'):
            simplified_dtype = 'number'
        elif str_dtype == 'bool':
            simplified_dtype = 'boolean'
        else:
            simplified_dtype = 'string'

        DatabaseConnection.execute_query(
            'INSERT INTO field (field_name, field_type) VALUES (%s, %s)',
            (column, simplified_dtype)
        )
    return True

def insert_dataset(df):
    data_dict = df.to_dict(orient='records')
    fieldIds = {}
    for row in data_dict:
        row_id = str(uuid4())
        for column, data_value in row.items():
            if column not in fieldIds:
                result = common.query_field_by_field_name(column)[0]
                fieldIds[column] = result['id']

            DatabaseConnection.execute_query(
                'INSERT INTO dataset (field_id, field_value, row_id) VALUES (%s, %s, %s)',
                (fieldIds[column], data_value, row_id)
            )
    return True
