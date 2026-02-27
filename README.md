# RegEx Quiz

---

## Introduction

This project represents a **Minimum Viable Product (MVP)** designed to assess technical competencies. Specifically, this application was developed for **DEFRA (Department for Environment, Food & Rural Affairs)**, a vital UK government organisation tasked with managing large-scale environmental data and digital services.

Within DEFRA, developers frequently work across **Node.js and Python** ecosystems. A mastery of **Regular Expressions (Regex)** is essential for efficient data validation, parsing, and text processing. This application provides a structured way to evaluate this knowledge base.

---

### Purpose and Utility

The purpose of the application is to serve as an objective diagnostic tool. By engaging with the quiz, developers can gauge their own proficiency, while the organisation gains a high-level overview of technical gaps. This facilitates a data-driven approach to identifying specific **training needs**.

To ensure the application is both lightweight and accessible, it was built using a robust tech stack. The core logic is powered by **Python**, utilising its extensive libraries for file handling and data manipulation, while the user-facing elements rely on clear, functional programming principles to ensure a smooth user journey.

---

### Functional Scope of the MVP

As an MVP, the current iteration prioritises core functionality and data integrity over aesthetic complexity. The application focuses on three critical pillars:

1. **Name Validation:** Ensuring user identity is captured accurately.
2. **Input Collection:** Gathering responses through an intuitive interface.
3. **Data Storage:** Writing and appending assessment results to a **CSV file** .

At the conclusion of each session, the application calculates and **displays the user’s score**, providing immediate feedback to the participant.

### Flexibility and Future-Proofing

One of the most usefull features of this application is its **data-driven design**. Rather than hard-coding questions into the logic, the app pulls its content from an external CSV file. This design choice ensures that the tool is entirely subject-agnostic. While it is currently configured for Regex assessment, DEFRA can easily repurpose the platform to check knowledge on any subject, simply by updating the data within the source CSV file.

---

## Design

---

### GUI Design

**Figure 1** is the wireframe representing the planned user journey through the quiz. It was mainly used to plan screen layout and does not represent the look of the final application.

<img width="1102" height="903" alt="Wireframe" src="https://github.com/user-attachments/assets/b3af7a21-2eab-4fba-b37a-155b6343ef94" />

**Figure 1:** Wireframe

---

### Functional and Non-functional requirements

#### Functional Requirements


*These define the specific features and workflows the application must provide.*

| ID | Feature | Description | Source File |
| --- | --- | --- | --- |
| **FR-01** | **User Validation** | Must validate that usernames are alphanumeric and between 3–15 characters. | `models.py` |
| **FR-02** | **Dynamic Loading** | Must parse quiz questions, four options, and the correct answer from `questions.csv`. | `models.py` |
| **FR-03** | **Quiz Interface** | Must display questions one-by-one with a progress indicator (e.g., "Question 1/10"). | `app.py` |
| **FR-04** | **Input Enforcement** | Must prevent users from proceeding to the next question without selecting an option. | `app.py` |
| **FR-05** | **Data Persistence** | Must append the username, score, and a timestamp to `results.csv` upon completion. | `models.py` |

---

#### Non-functional Requirements

*These define the performance, usability, and reliability standards of the system.*

| Category | Requirement | Specification |
| --- | --- | --- |
| **Usability** | **Consistent UI** | The GUI must use the "Clam" theme with Segoe UI fonts for a modern look. |
| **Reliability** | **Error Handling** | If `questions.csv` is missing, the system must provide a fallback "Error" question to prevent a crash. |
| **Portability** | **File Handling** | The system must use relative paths for CSV files to ensure it runs on different machines. |
| **Maintainability** | **Modular Design** | Logic (Models) must be kept separate from the Interface (App) to allow for unit testing. |
| **Performance** | **Instant Feedback** | GUI transitions between questions should occur without noticeable latency. |

---

#### Tech Stack Outline

| Dependency | Purpose |
| --- | --- |
| **Python 3** | Core programming language. |
| **Tkinter** | Library used for the graphical user interface. |
| **Tkinter.ttk** | Styling: Used to apply the "clam" theme. |
| **Unittest** | Framework used for the automated test suite. |
| **CSV Module** | Used for reading question data and writing user results. |
| **re** | regular expressions. |
| **datetime** | Used to capture the date and time a user completes the quiz. |

---

#### Code Design

<img width="583" height="1056" alt="image" src="https://github.com/user-attachments/assets/5510f45c-9199-41a9-a0da-0c0350b571d4" />

**Figure 2:** Class diagram

---

## Development

This project is built using a **modular architecture**, which is a software design technique that separates the functionality of a programme into independent, interchangeable modules. By splitting the code into different files based on their specific responsibilities, the application becomes significantly easier to read, maintain, and expand, even for those who are just beginning their journey with Python.

---

### 1. The Data Logic (`models.py`)

Think of this file as the **"Brain"** of the application. It handles the internal rules and data processing without needing to know what the buttons or windows look like.

#### Validating the User

Before the quiz begins, the system must ensure the user provides an appropriate username. The `validate_username` function acts as a gatekeeper. It checks that the input is "alphanumeric" (only letters and numbers) and falls between 3 and 15 characters in length. If a user tries to enter a name that is too short or contains special symbols like `@` or `!`, the function returns `False`, and the app will prevent them from starting the quiz.

```python
def validate_username(name: str) -> bool:
    """
    Checks if the name is alphanumeric and 3-15 chars long.
    """
    if not name:
        return False
    # isalnum() checks for letters and numbers only
    return name.isalnum() and 3 <= len(name) <= 15

```

#### Organising Questions with Objects

Instead of managing a messy list of text, we use a **Class** called `Question`. A class acts as a blueprint or template. Every time the app loads a question from the file, it creates a new "Object" based on this template, holding the question text, the four possible choices, and the correct answer in one neat package.

```python
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt      # The actual question text
        self.options = options    # A list of 4 possible answers
        self.answer = answer      # The correct answer string

```

#### The Quiz Engine

The `QuizEngine` class is responsible for the heavy lifting of file management. It uses Python's built-in `csv` module to read the `questions.csv` file. A vital part of professional development is "Error Handling". The engine is programmed to catch a `FileNotFoundError` if the questions file is missing, instead of the programme crashing and vanishing. The engine creates a "fallback" alternative question to tell the user what went wrong. It also handles "Exporting," where it appends the final score and a timestamp to a results file so the data is saved forever (persistant data storage).

```python
def export_results(self, username, score):
    # Get the current date and time
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
    # 'a' means 'append' - it adds a new line without deleting old results
    with open('results.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username, score, timestamp])

```

---

### 2. The Interface (`app.py`)

While `models.py` is the brain, `app.py` is the **"Face"** of the application. It uses a library called `Tkinter`, which is Python’s standard tool for creating windows and buttons.

#### Building the Visuals

The application is built using "Frames". You can think of a Frame as a transparent container that holds different parts of the UI, like labels and text boxes. When you move from the Login screen to the Quiz screen, the app "destroys" the login frame and "packs" a new question frame into the window. This makes the app feel like it is changing pages, even though it is all happening inside one window.

```python
def setup_login_ui(self):
    self.frame = tk.Frame(self.root, bg="#f5f5f5")
    self.frame.pack(fill="both", expand=True)

    # Adding a title label
    tk.Label(self.frame, text="RegEx Knowledge Quiz", 
             font=("Segoe UI", 22, "bold"), bg="#f5f5f5").pack(pady=40)

    # Creating an entry box for the username
    self.user_entry = tk.Entry(self.frame, font=("Segoe UI", 14), width=30)
    self.user_entry.pack(pady=10)

```

#### Managing User Input

When a user clicks an answer, the app uses a `StringVar` to keep track of which "Radio Button" was selected. When the "Next" button is pressed, the code compares the user's choice against the correct answer stored in the `QuizEngine`. If they match, the score is increased by one. This interaction between the visual button and the logic in the engine is the core of how the software functions.

```python
for opt in question.options:
    # Radiobuttons allow the user to pick only one option at a time
    ttk.Radiobutton(self.q_frame,
                    text=opt,
                    value=opt,
                    variable=self.selected).pack(anchor="w", pady=3)

```

---

### 3. Automated Testing (`test_quiz.py`)

A major part of software development is ensuring that new changes don't break old features. This project includes a dedicated testing file that uses the `unittest` framework.

#### Why We Test

The tests act like a robotic user. For instance, one test tries to log in with a name that is far too long to see if the `validate_username` function correctly blocks it. Another test checks the `QuizEngine` by creating a temporary "fake" CSV file, loading it, and making sure the data comes out exactly as it went in. This gives developers the confidence to change the code, knowing that if they make a mistake, the tests will catch it immediately.

```python
def test_username_validation_invalid(self):
    # This should return False because "Jo" is only 2 characters long
    self.assertFalse(validate_username("Jo"), "Too short")
    
    # This should return False because it contains a symbol
    self.assertFalse(validate_username("User!@#"), "Contains symbols")

```

#### Cleanup (Teardown)

A unique feature of this test suite is the `tearDown` method. After the tests finish running, this function automatically deletes any temporary files created during the process. This ensures the project folder stays clean and doesn't get cluttered with "junk" data files used only for testing.

---

### Summary of Component Interaction

The lifecycle of the programme follows a clear path: the **App** launches the window and asks for a name; the **Logic** validates that name; the **Engine** loads the questions from a file; and the **App** displays them to the user. Finally, once the last question is answered, the **Engine** saves the results to a permanent record. Every piece works together to create a seamless experience for the user while keeping the code organised for the developer.


## Testing

To ensure the reliability and quality of the RegEx Knowledge Quiz, a comprehensive testing strategy was adopted. This approach combines automated unit testing with systematic manual testing to verify both the internal logic and the user-facing interface.

---

### 1. Testing Strategy and Methodology

The project utilises a dual-layered testing methodology to ensure the application is robust and user-friendly.

#### Automated Unit Testing

We use Python's built-in `unittest` framework to validate the "brain" of the application (the `models.py` file). This is a **strategic approach** because it allows us to test critical logic such as **username validation** and **CSV data parsing** in isolation from the graphical interface.

**Justification:**

* **Efficiency:** Tests can be executed in seconds, providing immediate feedback during development.
* **Reliability:** Automated tests use "Set Up" and "Tear Down" routines to create temporary test files, ensuring that the real project data is never corrupted during testing.
* **Edge Case Coverage:** It allows us to easily test boundary conditions, such as usernames that are exactly 3 or 15 characters long, which might be missed during casual manual use.

#### Manual System Testing

While unit tests handle the logic, manual testing is essential for verifying the **User Experience (UX)**. This involves following a structured test plan to interact with the Tkinter interface as a real user would.

**Justification:**

* **Visual Verification:** Automated tests cannot easily "see" if a window is centred or if a font looks correct; manual testing ensures the `clam` theme and Segoe UI styling are applied properly.
* **Usability:** It confirms that the flow from the login screen to the final results dialog is intuitive and that the application closes cleanly without leaving "ghost" processes.

---

### 2. Outcomes of Application Testing

#### 2.1 Manual Testing Outcomes

The following table outlines the systematic manual tests performed on the Tkinter application.

#### 📋 Manual Testing Table for Tkinter RegEx Quiz App

| **ID** | **Functionality** | **Test Description** | **Expected Result** | **Actual Result** | **Pass/Fail** |
| --- | --- | --- | --- | --- | --- |
| **1** | **Initial Launch** | Launch the application and verify UI scaling and title. | Window titled “RegEx Knowledge Quiz” opens. UI is centred and responsive. | As expected; UI rendered correctly. | **Pass** |
| **2** | **Valid Login** | Enter a valid username (e.g., `DevUser23`) and click **Start Quiz**. | Name is accepted; login frame disappears; first question loads instantly. | System transitioned to quiz frame. | **Pass** |
| **3** | **Input Validation** | Attempt to start with an invalid name (too short or special characters). | Error dialogue appears; user is prevented from starting until fixed. | Warning displayed; login blocked. | **Pass** |
| **4** | **CSV Question Load** | Start the quiz with a valid `questions.csv` file. | Questions and four radio-button options populate correctly from the file. | Data parsed and displayed accurately. | **Pass** |
| **5** | **Quiz Interaction** | Select an answer and click **Next**. | Selection is registered; score updates internally; next question appears. | Smooth transition; score tracked. | **Pass** |
| **6** | **Selection Logic** | Click **Next** without selecting any radio button. | A warning dialogue appears; user remains on the current question. | Logic enforced; no skipped questions. | **Pass** |
| **7** | **RegEx Rendering** | View questions containing complex symbols (e.g. `^[A-Z]+$`). | Special characters and backslashes render clearly without formatting errors. | Characters displayed correctly. | **Pass** |
| **8** | **Quiz Completion** | Finish the final question in the set. | Final score is displayed in a summary dialogue with a "Results saved" message. | Completion screen appeared. | **Pass** |
| **9** | **Data Persistence** | Check the `results.csv` file after a completed session. | A new row is appended with the `username`, `score`, and `timestamp`. | Row added; previous data preserved. | **Pass** |
| **10** | **Process Exit** | Close the application via the "OK" button or window 'X'. | Application window closes and the Python process terminates fully. | Clean exit; no ghost processes. | **Pass** |
---

#### 2.2 Unit Testing Outcomes

The automated suite in `test_quiz.py` successfully validates the core business logic of the application.

* **Username Validation:** Confirmed that the `validate_username` function correctly identifies valid strings and rejects empty inputs, symbols, and incorrect lengths.
* **Data Object Integrity:** Verified that the `Question` class correctly stores prompts and maps the four options to their corresponding index.
* **Engine Performance:** The `QuizEngine` successfully loads data from CSV rows into `Question` objects and maintains the correct count.
* **Result Exportation:** Verified that the `export_results` method successfully creates the `results.csv` file and writes the username, integer score, and a valid timestamp string.

```python
# Example of a successful test case from the suite
def test_export_results(self):
    engine = QuizEngine(self.test_file)
    engine.export_results("DevUser23", 9)
    
    # Confirms the file was created and contains the correct data
    self.assertTrue(os.path.exists(self.results_file))

```

All **6 automated tests** passed successfully, ensuring the foundation of the application is stable.

<img width="940" height="319" alt="image" src="https://github.com/user-attachments/assets/0b1ed341-c27c-43e9-aded-3124adbea175" />


## Documentation
---

This section provides comprehensive guidance for both the end users of the RegEx Knowledge Quiz and the technical staff responsible for its maintenance and development.

---

### 1. User Documentation

This guide explains how staff members can launch the application and navigate the quiz interface.

#### Launching the Application

To start the quiz, navigate to the project directory in your terminal and run the main application file:

```bash
python app.py

```

The application window will open with the title "RegEx Knowledge Quiz!" and a fixed size of 550x420 pixels to ensure all elements are clearly visible.

#### The Login Process

* **Username Entry**: Upon launching, you will be prompted to enter a username.


* **Validation Rules**: Your name must be between 3 and 15 characters long and consist only of letters and numbers.


* **Start**: Click the **Start Quiz** button to begin. If the name is invalid, a dialogue box will appear asking for a valid input.

#### Navigating the Quiz

* **Answering Questions**: Each screen displays a single question with four multiple-choice options.


* **Selection**: You must select one radio button before clicking **Next**. If you attempt to proceed without a selection, a warning will appear.


* **Progress Tracking**: The top of the screen displays your current progress (e.g., "Question 1/10").

#### Completion and Results

* **Final Score**: After the last question, a message box will display your total score.


* **Data Storage**: The system automatically saves your username, final score, and a timestamp to a local file named `results.csv` for administrative records.

---

### 2. Technical Documentation

This guide is for developers to understand the codebase, troubleshoot issues, and run local tests.

---

#### Codebase Overview

The project is divided into three main components to ensure a clean separation of concerns:

* **`app.py` (The View)**: Manages the Tkinter GUI. The `RegExQuizApp` class handles the lifecycle of the interface, from the login screen to the dynamic rendering of questions.

* **`models.py` (The Logic)**: Contains the `QuizEngine` and `Question` classes.

* `QuizEngine`: Responsible for reading the `questions.csv` data and appending results to `results.csv`.

* `Question`: A simple data structure that holds the prompt, a list of options, and the correct answer.

* **`test_quiz.py` (The Tests)**: A suite of automated unit tests to verify that the logic in `models.py` functions as expected.

---

#### Running Tests Locally

Automated tests should be run whenever changes are made to the logic or data structures. To execute the tests, run:

```bash
python test_quiz.py

```

The test suite performs several critical checks:

* **Username Validation**: Ensures the `validate_username` function correctly identifies valid and invalid strings.

* **Engine Loading**: Verifies that the `QuizEngine` can correctly parse a CSV file into `Question` objects.

* **Result Persistence**: Confirms that data is correctly appended to the results file in the expected format.

---

#### Troubleshooting

* **Missing `questions.csv**`: If the application cannot find the question file, the `QuizEngine` is designed to catch the error and load a "fallback" question to prevent a system crash.

* **Malformed CSV**: If the input CSV is missing columns like `prompt` or `answer`, a "KeyError" message will be printed to the console to assist in debugging the data format.


* **GUI Not Launching**: Ensure that the `tkinter` library is installed on your system. On some Linux distributions, this requires a separate package (e.g., `sudo apt-get install python3-tk`).

---

#### Key Logic Example: Data Handling

The `QuizEngine` uses Python's `csv` module to handle data input and output reliably:

```python
def load_questions(self):
    try:
        with open(self.data_file, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Dynamically building objects from CSV rows
                q = Question(row['prompt'], 
                             [row['o1'], row['o2'], row['o3'], row['o4']], 
                             row['answer'])
                self.questions.append(q)
    except FileNotFoundError:
        # Graceful degradation if file is missing
        self.questions.append(Question("Error: questions.csv not found.", 
                             ["N/A", "N/A", "N/A", "N/A"], "N/A"))

```

---

## Evaluation

Reflecting on the development of this RegEx Quiz application, I am pleased with the outcome of the **MVP**. Successfully reaching a stage where the application is fully functional, with all **Continuous Integration (CI) tests** passing, provides a strong sense of achievement. Ensuring that the automated testing suite remains green was a priority, as it guarantees the stability of the core logic as the project evolves.

The process of bringing this application to life was admittedly lengthy. I invested a significant amount of time cross-referencing official documentation and various learning resources to ensure the internal processes like CSV handling, and frame transitions, behaved exactly as intended. This research was useful, as it allowed me to bridge the gap between initial concepts and a working solution.

One of the most challenging aspects of the project was the design phase. I have always found that I prefer the 'build' phase. That is taking an established design and making it a reality rather than conceptualising the layout from scratch. However, through this process, I have come to **recognise the vital importance of design**. Understanding how a user interacts with an interface is fundamental to being a well-rounded developer, and this project has helped me appreciate that prototyping is just as important as writing code.

Looking forward, I am aware that there is substantial room for refinement. I intend to implement **stricter name validation** to prevent edge-case errors and enhance the overall robustness of the input collection. One of the barriers to refactoring my code is the need to update all the documentation for the app including this document.I plan to revisit and develop these features further to transform this MVP into a more sophisticated app. 

---
