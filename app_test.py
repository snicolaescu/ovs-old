import unittest
from app import server


class OvsTest(unittest.TestCase):
    def testRoot(self):
        name = "yourname"
        result= self.applications.get('/' + name)
        
        #assert "OK" == "OK"
        assert "Hello World from " + name  + " !" == result.data
    
    
    def setUp(self):
        self.applications = server.test_client()
        
if __name__ == '__main__':
    unittest.main()
    