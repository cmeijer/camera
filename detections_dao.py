import uuid
import settings

from dao_utils import execute_query, create_table

table_name = 'detections'
columns = ['id', 'image', 'object_type', 'boundingbox']


def save_or_update(filename, object_type, bounding_box=None):
    new_id = uuid.uuid4()
    query = 'INSERT INTO {} VALUES ("{}", "{}")'.format(table_name, new_id, filename, object_type, bounding_box)
    execute_query(settings.database, query)


def get_all_detections(max_results=5):  # TODO join with images and order by time
    query = 'SELECT * FROM {} DESC LIMIT {}'.format(table_name, max_results)
    results = execute_query(settings.database, query)
    return results


def setup():
    create_table(settings.database, table_name, columns)
