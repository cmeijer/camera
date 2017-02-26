import settings
import datetime
from dateutil.parser import parse

from dao_utils import execute_query, create_table

table_name = 'images'
time_column = 'time'
columns = ['filename', time_column]


def save_or_update(filename, seconds):
    query = 'INSERT INTO {} VALUES ("{}", "{}")'.format(table_name, filename, seconds)
    execute_query(settings.database, query)


def get_all_images(max_results=5):
    query = 'SELECT * FROM {} ORDER BY {} DESC LIMIT {}'.format(table_name, time_column, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table(settings.database, table_name, columns)
