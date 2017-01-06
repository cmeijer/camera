import unittest
import wlan_dao
from datetime import datetime
import mock
import os

class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """

    def test_setup_teardown(self):
        """ Setup and teardown should not raise any exceptions. """
        pass

    def test_save(self):
        """ Save should raise no exceptions. """
        ip = '123.123.123.123'
        mac = 'a1.a2.a3.a4.a5.a6'
        time_stamp = datetime(2017, 1, 1, 9, 45, 15)
        wlan_dao.save_or_update(ip, mac, time_stamp)

    def test_save_load(self):
        """ Save and load should return same time as original. """
        ip = '123.123.123.123'
        mac = 'a1.a2.a3.a4.a5.a6'
        time_stamp = datetime(2017, 1, 1, 9, 45, 15)
        wlan_dao.save_or_update(ip, mac, time_stamp)
        result = wlan_dao.get_time_by_mac(mac)
        assert time_stamp is result

    @mock.patch('wlan_dao.settings')
    def setUp(self, settings_mock):
        self.testdb_name = 'test_db'
        settings_mock.configure_mock(database=self.testdb_name)
        wlan_dao.setup()

    def tearDown(self):
        os.remove(self.testdb_name)