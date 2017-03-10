import uuid
import settings

from dao_utils import execute_query, create_table
from images_dao import table_name as images_table_name
from images_dao import time_column as images_time_column

table_name = 'detections'
columns = ['id', 'image', 'object_type', 'boundingbox']


def save_or_update(filename, object_type, bounding_box=None):
    new_id = uuid.uuid4()
    query = 'INSERT INTO {} VALUES ("{}", "{}", "{}", "{}")'\
        .format(table_name, new_id, filename, object_type, bounding_box)
    execute_query(settings.database, query)
    return new_id


def get_all_detections(max_results=5):
    query = 'SELECT * FROM {} DESC LIMIT {}'.format(table_name, max_results)
    results = execute_query(settings.database, query)
    return results


def get_last_detections(max_results=5):
    query = 'SELECT * FROM {} INNER JOIN {} ON {}.image={}.filename ORDER BY {} DESC LIMIT {}'\
        .format(table_name, images_table_name, table_name, images_table_name, images_time_column, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table(settings.database, table_name, columns)
