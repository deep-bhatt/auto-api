from autoapi.core.database import DatabaseConnection

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
