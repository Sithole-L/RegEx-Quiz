import unittest
import os
import csv
from models import validate_username, QuizEngine, Question


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
        self.results_file = 'results.csv' 

        with open(self.test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["prompt","o1","o2","o3","o4","answer"])  
            writer.writerow(["test q", "A","B","C","D","A"])

    def tearDown(self):
        """
        Cleans up all temporary files after tests run.
        """
        for file in [self.test_file, self.results_file]:
            if os.path.exists(file):
                os.remove(file)      

    def test_username_validation_valid(self):
        """
        Test that valid usernames return True.
        """
        self.assertTrue(validate_username("DevUser23"))
        self.assertTrue(validate_username("Jon"))            

    def test_username_validation_invalid(self):
        """
        Test that invalid usernames (short, long, symbols) return False.
        """
        self.assertFalse(validate_username("Jo"), "Too short")
        self.assertFalse(validate_username("ThisNameIsWayWayTooLong"), "Too long")
        self.assertFalse(validate_username("User!@#"), "Contains symbols")
        self.assertFalse(validate_username(""), "Empty string")

    def test_quiz_engine_loading(self):
        """
        Test if the QuizEngine correctly reads from the CSV.
        """
        engine = QuizEngine(self.test_file)
        self.assertEqual(len(engine.questions), 1)
        self.assertEqual(engine.questions[0].answer, "A")  

    def test_question_object_creation(self):
        """
        Test if the Question class initialises correctly.
        """
        q = Question("Prompt", ["1", "2", "3", "4"], "1")
        self.assertEqual(q.prompt, "Prompt")
        self.assertEqual(len(q.options), 4)
        self.assertEqual(q.answer, "1")   

    def test_export_results(self):
        """
        Test if the export_results method correctly appends data to results.csv.
        """
        engine = QuizEngine(self.test_file)
        test_user = "DevUser23"
        test_score = 9
        
        # Trigger the export
        engine.export_results(test_user, test_score)
        
        # Verify the file was created
        self.assertTrue(os.path.exists(self.results_file))
        
        # Read the file to verify content
        with open(self.results_file, 'r', newline='') as f:
            reader = csv.reader(f)
            rows = list(reader)
            last_row = rows[-1]
            
            self.assertEqual(last_row[0], test_user)
            self.assertEqual(last_row[1], str(test_score))
            # Timestamp check (verifying it exists)
            self.assertIsNotNone(last_row[2])       


if __name__ == "__main__":
    unittest.main()
