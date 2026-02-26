import unittest
import os
import csv
from models import validate_username


class TestRegexQuiz(unittest.TestCase):

    def test_smoke(self):
        """
        Simple smoke test to ensure the system runs.
        """
        self.assertTrue(True)

    def setUp(self):
        """
        Creates a temporary CSV for testing engine logic
        """
        self.test_file = 'test_questions.csv'
        self.test_results_file = 'test_results.csv'

        with open(self.test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["prompt","o1","o2","o3","o4","answer"])  
            writer.writerow(["test q", "a","b","c","d","a"])

    def tearDown(self):
        """
        Cleans up all temporary files after tests run.
        """
        for file in [self.test_file, self.test_results_file]:
            if os.path.exists(file):
                os.remove(file)      

    def test_username_validation_valid(self):
        """
        Test that valid usernames return True.
        """
        self.assertTrue(validate_username("DevUser23"))
        self.assertTrue(validate_username("Coder"))            



if __name__ == "__main__":
    unittest.main()
