__author__ = 'tusharmakkar08'

import unittest

from main import main, open_image_page, open_profile_pic

# TODO: Need to make a test user
TEST_USERNAME = "Lakshaymakkar13"
TEST_USER_ID = "100009262030116"


class TestMain(unittest.TestCase):
    """
    For testing Main code
    """

    def test_profile_image(self):
        """
        Profile image opens
        :return:
        """
        expected_output = open_profile_pic(TEST_USER_ID)
        self.assertEqual(expected_output, 1)

    def test_graph_image(self):
        """
        Graph image opens up
        :return:
        """
        expected_output = open_image_page(TEST_USER_ID)
        self.assertEqual(expected_output, 1)

    def test_main(self):
        """
        Main
        :return:
        """
        expected_output = main(TEST_USERNAME)
        self.assertEqual(expected_output, 1)

if __name__ == '__main__':
    unittest.main()
