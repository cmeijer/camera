import uuid
import settings

from dao_utils import execute_query
from images_dao import table_name as images_table_name
from images_dao import time_column as images_time_column
from images_dao import filename_column as images_filename_column

table_name = 'detections'
image_column = 'image'
id_column = 'id'
object_type_column = 'object_type'
bounding_box_column = 'boundingbox'
columns = [id_column, image_column, object_type_column, bounding_box_column]


def save_or_update(filename, object_type, bounding_box=None):
    new_id = uuid.uuid4()
    query = 'INSERT INTO {} VALUES ("{}", "{}", "{}", "{}")' \
        .format(table_name, new_id, filename, object_type, bounding_box)
    execute_query(settings.database, query)
    return new_id


def get_all_detections(max_results=5):
    query = 'SELECT * FROM {} DESC LIMIT {}'.format(table_name, max_results)
    results = execute_query(settings.database, query)
    return results


def get_last_detections(max_results=5):
    query = 'SELECT * FROM {} INNER JOIN {} ON {}.image={}.filename ORDER BY {} DESC LIMIT {}' \
        .format(table_name, images_table_name, table_name, images_table_name, images_time_column, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table()


def create_table():
    """Create a table"""
    foreign_key_query = 'FOREIGN KEY(%s) REFERENCES %s(%s)' % (image_column, images_table_name, images_filename_column)
    query = "CREATE TABLE %s (%s VARCHAR(32) PRIMARY KEY, %s VARCHAR(32), %s VARCHAR(64), %s VARCHAR(32), %s)" % (
        table_name, id_column, image_column, object_type_column, bounding_box_column, foreign_key_query)
    execute_query(settings.database, query)
