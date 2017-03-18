import sqlite3


def create_table(db_name, table_name, table_header):
    """Create a table"""
    query = "CREATE TABLE %s %s" % (table_name, tuple(table_header))
    execute_query(db_name, query)


def execute_query(db_name, query):
    print(db_name, query, end='')
    connection_obj = sqlite3.connect(db_name)
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(query)
    results = cursor_obj.fetchall()
    connection_obj.commit()
    connection_obj.close()
    print('...success')
    return results


def get_index_query(table_name, column_name):
    return "CREATE INDEX %s ON %s (%s);" % (
        '_'.join(["index", table_name, column_name]), table_name, column_name)
