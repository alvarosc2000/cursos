import unittest
from median_container import MedianContainer

class TestMedianContainer(unittest.TestCase):

    def test_add_and_median(self):
        mc = MedianContainer()
        mc.add_number(10)
        self.assertEqual(mc.get_median(), 10)
        mc.add_number(20)
        self.assertEqual(mc.get_median(), 15)
        mc.add_number(30)
        self.assertEqual(mc.get_median(), 20)

    def test_remove_and_median(self):
        mc = MedianContainer()
        mc.add_number(5)
        mc.add_number(10)
        mc.add_number(15)
        mc.remove_number(10)
        self.assertEqual(mc.get_median(), 10)
        mc.remove_number(5)
        self.assertEqual(mc.get_median(), 15)
        mc.remove_number(15)
        self.assertEqual(mc.get_median(), None)

if __name__ == "__main__":
    unittest.main()
