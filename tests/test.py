import unittest
import conversor

class Test(unittest.TestCase):
   def test_conversion(self):
    self.assertEqual(conversor.conversor("colombianos", 3875, 1000), 0.26)
    
