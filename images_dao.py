import settings
import datetime
from dateutil.parser import parse

from dao_utils import execute_query, get_index_query

table_name = 'images'
time_column = 'time'
filename_column = 'filename'
columns = [filename_column, time_column]


def save_or_update(filename, seconds):
    query = 'INSERT INTO {} VALUES ("{}", {})'.format(table_name, filename, seconds)
    execute_query(settings.database, query)


def get_all_images(max_results=5):
    query = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {}'.format(table_name, time_column, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table()


def create_table():
    """Create a table"""
    queries = ["CREATE TABLE %s (%s VARCHAR(32) PRIMARY KEY, %s REAL)" % (table_name, filename_column, time_column),
               get_index_query(table_name, filename_column),
               get_index_query(table_name, time_column)]
    for query in queries:
        execute_query(settings.database, query)


