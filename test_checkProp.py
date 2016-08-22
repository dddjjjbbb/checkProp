import unittest
from checkProp import findPropDupes


class TestDuplicates(unittest.TestCase):

    def setUp(self):
        self.PROPERTIES_WITH_DUPES = 'with_dupes.properties'

        def tearDown(self):
            pass

    def test_function_finds_dupes(self):
        expected = 2
        self.assertEqual(findPropDupes(self.PROPERTIES_WITH_DUPES), expected)


if __name__ == '__main__':
    unittest.main()
