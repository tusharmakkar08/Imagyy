__author__ = 'tusharmakkar08'

import os
import unittest

from image_search.search_files.fb_search import facebook_image_search, _open_image_page, _open_profile_pic, \
    _open_public_images

# TODO: Need to make a test user
TEST_USERNAME = "Lakshaymakkar13"
TEST_USER_ID = "100009262030116"


class TestMain(unittest.TestCase):
    """
    For testing Main code
    """

    def tearDown(self):
        """
        Removing generated files
        :return:
        """
        if os.path.exists(TEST_USERNAME+".jpg"):
            os.remove(TEST_USERNAME+".jpg")

    def test_profile_image(self):
        """
        Profile image opens
        :return:
        """
        expected_output = _open_profile_pic(TEST_USER_ID)
        self.assertEqual(expected_output, 1)

    def test_graph_image(self):
        """
        Graph image opens up
        :return:
        """
        expected_output = _open_image_page(TEST_USER_ID)
        self.assertEqual(expected_output, 1)

    def test_public_image(self):
        """
        public image opens up
        :return:
        """
        expected_output = _open_public_images(TEST_USERNAME)
        self.assertEqual(expected_output, 1)

    def test_main(self):
        """
        Main
        :return:
        """
        expected_output = facebook_image_search(TEST_USERNAME)
        self.assertEqual(expected_output, 1)

if __name__ == '__main__':
    unittest.main()
