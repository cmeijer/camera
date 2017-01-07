import sqlite3
import settings
import datetime
from dateutil.parser import parse

table_name = 'access'
mac_column = 'mac'
time_column = 'time'
columns = ['ip', mac_column, time_column, 'description']


def save_or_update(ip, mac, time, description):
    query = 'INSERT INTO {} VALUES ("{}", "{}", "{}", "{}");'.format(table_name, ip, mac, time, description)
    execute_query(settings.database, query)


def get_time_by_mac(mac):
    query = 'SELECT {} FROM {} WHERE {} = "{}"'.format(time_column,table_name, mac_column, mac)
    results = execute_query(settings.database, query)
    return parse(results[0][0])


def setup():
    create_table(settings.database, table_name, columns)


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
