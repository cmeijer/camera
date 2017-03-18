import images_dao
import detections_dao
import wlan_dao


def create_database():
    images_dao.setup()
    detections_dao.setup()
    wlan_dao.setup()
