from unittest import TestCase

class TestFoo(TestCase):

    def test_equal(self):
        self.assertEqual('foo', 'foo')
    
    def test_greater(self):
        self.assertGreater(1, 0)
    
    def test_true(self):
        self.assertTrue(True)
    
    def test_false(self):
        self.assertFalse(False)