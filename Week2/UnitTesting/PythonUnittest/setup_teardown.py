import unittest

class TestExample(

unittest.TestCase):

    def setUp(self):

        print("Before Test")

    def tearDown(self):

        print("After Test")

    def test_one(self):

        self.assertTrue(True)