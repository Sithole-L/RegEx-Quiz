import csv
import re
from datetime import datetime

def validate_username(name: str) -> bool:
    """
    Validates user input.
    Returns True if name is alphanumeric and 3-15 chars.
    """
    if not name:
        return False
    return name.isalnum() and 3 <= len(name) <= 15

class QuizEngine:
    """
    Handles the logic of loading questions and calculating scores.
    """
    def __init__(self, data_file):
        self.data_file = data_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """
        Reads questions from a CSV file.
        """    
        try:
            with open(self.data_file, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Ensures all required columns exist in the CSV row
                    q = Question(
                        row['prompt'], 
                        [row['o1'], row['o2'], row['o3'], row['o4']], 
                        row['answer']
                    )
                    self.questions.append(q)
        except FileNotFoundError:
            # Creates an alt question so the app doesn't crash if file is missing/not found
            self.questions.append(Question("Error: questions.csv not found.", ["N/A", "N/A", "N/A", "N/A"], "N/A"))
        except KeyError as e:
            print(f"CSV Formatting Error: Missing column {e}")

    def export_results(self, username, score):
        """
        Appends the user's results to a local CSV file.
        """
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        with open('results.csv', mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([username, score, timestamp])   

class Question:
    """
    Represents a single Multiple Choice Question.
    """
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options  # List of strings
        self.answer = answer    # The correct string                