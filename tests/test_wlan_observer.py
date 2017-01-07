import unittest
import mock
from wlan_observer import wlan_observer


class PersonDetectionSuite(unittest.TestCase):
    """ Tests. """

    def test_instantiate_no_exc(self):
        """ Should instantiate without exceptions. """
        pass

    @mock.patch('wlan_observer.wlan_dao')
    @mock.patch('wlan_observer.nmap')
    def test_scan_doa_call(self, mock_nmap, mock_dao):
        """ Should trigger dao call without mac. """
        mock_nmap.scan.return_value = self.no_root_output

        self.observer.observe()
        mock_dao.save_or_update.assert_called_with('192.168.0.1', None, '2017-01-04 20:30 CET', None)

    @mock.patch('wlan_observer.wlan_dao')
    @mock.patch('wlan_observer.nmap')
    def test_scan_doa_call_root(self, mock_nmap, mock_dao):
        """ Should trigger dao call without mac. """
        mock_nmap.scan.return_value = self.root_output

        self.observer.observe()
        mock_dao.save_or_update.assert_called_with('192.168.0.1', 'aa:bb:cc:dd:ee:ff', '2017-01-04 21:28 CET', 'Technicolor USA')

    def setUp(self):
        self.observer = wlan_observer()
        self.no_root_output = (b'\nStarting Nmap 7.01 ( https://nmap.org ) at 2017-01-04 20:30 CET\nNmap scan report for 192.168.0.1\nHost is up (0.0038s latency).\nNmap done: 256 IP addresses (1 hosts up) scanned in 2.64 seconds\n', b'')
        self.root_output = (b'\nStarting Nmap 7.01 ( https://nmap.org ) at 2017-01-04 21:28 CET\nNmap scan report for 192.168.0.1\nHost is up (0.0036s latency).\nMAC Address: aa:bb:cc:dd:ee:ff (Technicolor USA)\nNmap done: 256 IP addresses (1 hosts up) scanned in 3.54 seconds\n',b'')
