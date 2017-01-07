import unittest
import wlan_dao
from datetime import datetime
from datetime import timedelta
import mock
import os


class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """

    @mock.patch('wlan_dao.settings')
    def test_setup_teardown(self, settings_mock):
        """ Setup and teardown should not raise any exceptions. """
        settings_mock.configure_mock(database=self.testdb_name)
        pass

    @mock.patch('wlan_dao.settings')
    def test_save(self, settings_mock):
        """ Save should raise no exceptions. """
        settings_mock.configure_mock(database=self.testdb_name)
        wlan_dao.save_or_update(self.ip, self.mac, self.time_stamp, self.description)

    @mock.patch('wlan_dao.settings')
    def test_save_load(self, settings_mock):
        """ Save and load should return same time as original. """
        settings_mock.configure_mock(database=self.testdb_name)
        wlan_dao.save_or_update(self.ip, 'other.mac1', self.time_stamp + timedelta(hours=2), self.description)
        wlan_dao.save_or_update(self.ip, self.mac, self.time_stamp, self.description)
        wlan_dao.save_or_update(self.ip, 'other.mac2', self.time_stamp + timedelta(hours=4), self.description)
        result = wlan_dao.get_time_by_mac(self.mac)
        self.assertEqual(self.time_stamp, result)

    @mock.patch('wlan_dao.settings')
    def setUp(self, settings_mock):
        self.description = 'My test device'
        self.ip = '123.123.123.123'
        self.mac = 'a1.a2.a3.a4.a5.a6'
        self.time_stamp = datetime(2017, 1, 1, 9, 45, 15)
        self.testdb_name = 'test_db'
        settings_mock.configure_mock(database=self.testdb_name)
        wlan_dao.setup()

    def tearDown(self):
        os.remove(self.testdb_name)
