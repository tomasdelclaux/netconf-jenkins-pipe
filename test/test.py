import random
import unittest
import xmlrunner
import paramiko
import time

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.remotePre = paramiko.SSHClient()
        self.remotePre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.remotePre.connect("192.168.33.56", username="admin", password="cisco", look_for_keys=False, allow_agent=False, timeout=15)

    def test_version(self):
        # make sure the shuffled sequence does not lose any elements
        conn = self.remotePre.invoke_shell()
        conn.send("show version\n")
        time.sleep(1)
        out = conn.recv(65535).decode('utf-8')
        print(out)
        self.assertIn("16.12.04a", out)
        conn.close()
    
    def test_ip_int_brief1(self):
        # make sure the shuffled sequence does not lose any elements
        conn = self.remotePre.invoke_shell()
        conn.send("show ip int brief\n")
        time.sleep(1)
        out = conn.recv(65535).decode('utf-8')
        print(out)
        self.assertIn("GigabitEthernet1       192.168.33.56   YES NVRAM  up                    up", out)
        conn.close()

    def test_ip_int_brief2(self):
        # make sure the shuffled sequence does not lose any elements
        conn = self.remotePre.invoke_shell()
        conn.send("show ip int brief\n")
        time.sleep(1)
        out = conn.recv(65535).decode('utf-8')
        print(out)
        self.assertIn("GigabitEthernet2       192.168.99.56   YES other  up                    up", out)
        conn.close()
    
    def __del__(self):
        self.remotePre.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)