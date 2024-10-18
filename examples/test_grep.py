import os
import unittest

from files import grep

FILE_CONTENT = """Beautiful is better than ugly.
Simple is better than complex.
Readability counts.
Special cases aren't special enough to break the rules.
Explicit is better than implicit.
Although practicality beats purity.
Errors should never pass silently.
"""


class GrepTestCase(unittest.TestCase):
    TEST_FILE_PATH = "testfile.txt"

    @classmethod
    def setUpClass(cls):
        with open(cls.TEST_FILE_PATH, "w") as f:
            f.write(FILE_CONTENT)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.TEST_FILE_PATH)

    def test_matching_lines_found(self):
        lines = grep("better", self.TEST_FILE_PATH)

        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 3)
        self.assertIn("Beautiful is better than ugly.\n", lines)
        self.assertIn("Simple is better than complex.\n", lines)
        self.assertIn("Explicit is better than implicit.\n", lines)

    def test_no_matching_lines_found(self):
        lines = grep("generator", self.TEST_FILE_PATH)

        self.assertListEqual(lines, [])

    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            grep("better", "nonexistent.txt")
