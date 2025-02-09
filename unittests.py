import unittest
import dpkt
from pcap_parser import create_mimishark_json, ip_protocol_prop

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = create_mimishark_json
        self.ip_prop = ip_protocol_prop
        self.pcap = dpkt.pcap.Reader(open('temp/testsforparser.pcap','rb'))
        self.ip = "bad ip"
    def test_prot_prop(self):
        self.assertEqual(self.ip_prop(self.ip), "No protocol")  
if __name__ == "__main__":
    unittest.main()
