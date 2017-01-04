import subprocess


def scan():
    """ Scans local network using nmap and returns stdout and stderr. """
    cmd = 'nmap -sn 192.168.0.0/24'
    process = subprocess.Popen(cmd, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    return process.communicate()
