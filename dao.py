import sqlite3



def save_or_update(ip, mac, time):
    pass

def get():
    pass


def create_table(db_name, table_name, table_header):
    """Create a table"""
    try:
        connection_obj = sqlite3.connect(db_name)
        cursor_obj = connection_obj.cursor()
        query = "CREATE TABLE %s%s" % (table_name, tuple(table_header))
        print(query)
        cursor_obj.execute(query)
        connection_obj.commit()
        connection_obj.close()
        print("-Created Table %s" % table_name)
    except Exception as e:
        print("Python says:", str(e))
