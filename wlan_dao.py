import settings
from dateutil.parser import parse

from dao_utils import execute_query, get_index_query

table_name = 'access'
mac_column = 'mac'
time_column = 'time'
ip_column = 'ip'
description_column = 'description'
columns = [ip_column, mac_column, time_column, description_column]


def save_or_update(ip, mac, time, description):
    query = 'INSERT INTO {} VALUES ("{}", "{}", {}, "{}")'.format(table_name, ip, mac, time, description)
    execute_query(settings.database, query)


def get_time_by_mac(mac):
    query = 'SELECT {} FROM {} WHERE {} = "{}" ORDER BY {} DESC'.format(time_column, table_name, mac_column, mac,
                                                                        time_column)
    results = execute_query(settings.database, query)
    return parse(results[0][0])


def get_all_connections(max_results=5):
    query = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {}'.format(table_name, time_column, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table()


def create_table():
    """Create a table"""
    queries = ["CREATE TABLE %s (%s VARCHAR(32), %s VARCHAR(32), %s REAL, %s VARCHAR(128))" % (
        table_name, ip_column, mac_column, time_column, description_column),
               get_index_query(table_name, time_column),
               get_index_query(table_name, mac_column)]
    for query in queries:
        execute_query(settings.database, query)
