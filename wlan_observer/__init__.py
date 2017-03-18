import requests
import nmap
import settings
import time


class wlan_observer(object):
    def observe(self):
        """ Does a scan of the local network and records connected devices. """
        out, err = nmap.scan()
        reports = str(out).split('Nmap scan report for ')
        now = time.time()
        device_reports = reports[1:]
        for device_report in device_reports:
            ip = device_report.split('\\n')[0]
            mac = self.get_mac_address(device_report)
            description = self.get_device_description(device_report)
            data = {'ip': ip, 'mac': mac, 'time': now, 'description': description}
            address = 'http://' + settings.webservice_host + '/connections'
            requests.post(address, json=data)

    def get_mac_address(self, device_report):
        try:
            mac = device_report.split('MAC Address: ')[1].split(' ')[0]
        except IndexError as e:
            mac = None
        return mac

    def get_device_description(self, device_report):
        try:
            description = device_report.split('MAC Address: ')[1].split('(')[1].split(')\\n')[0]
        except IndexError as e:
            description = None
        return description
