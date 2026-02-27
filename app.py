import tkinter as tk                                # for creating the GUI
from tkinter import messagebox, ttk                 # for styling and messagebox
from models import QuizEngine, validate_username    # quiz logic & username validation
from datetime import datetime                       # record quiz completion timestamp
import csv                                          # read csv

class RegExQuizApp:
    """
    A GUI application for testing Regular Expression (RegEx) knowledge.
    
    class manages the lifecycle of the quiz, that is user login, 
    question rendering, and result exportation.
    """

    def __init__(self, root):
        """
        Initializes the application window and quiz engine.

        Args:
            root (tk.Tk): The main root window for the Tkinter application.
        """
        self.root = root
        self.root.title("RegEx Knowledge Quiz!")
        self.root.geometry("550x420")
        self.root.configure(bg="#f5f5f5")

        self.engine = QuizEngine('questions.csv')
        self.current_q_index = 0
        self.score = 0

        self.configure_styles()
        self.setup_login_ui()

    # ---------------------------------------------------------------------------
    # UI STYLING
    # ---------------------------------------------------------------------------

    def configure_styles(self):
        """
        Defines the visual theme and styles for the ttk widgets.
        
        Configures font, padding, and colors for TButton, TRadiobutton, and TLabel.
        """
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton",
                        font=("Segoe UI", 14),
                        padding=6,
                        relief="flat",
                        background="#4a90e2",
                        foreground="white")
        style.map("TButton",
                  background=[("active", "#357ABD")])

        style.configure("TRadiobutton",
                        font=("Segoe UI", 14),
                        padding=4)

        style.configure("TLabel",
                        font=("Segoe UI", 16))  

    # ------------------------------------------------------------------------------
    # LOGIN SCREEN
    # ------------------------------------------------------------------------------

    def setup_login_ui(self):
        """
        Renders the initial login screen widgets.
        
        Prompts the user to enter a username and renders a start button.
        """
        self.frame = tk.Frame(self.root, bg="#f5f5f5")
        self.frame.pack(fill="both", expand=True)

        tk.Label(self.frame,
                 text="RegEx Knowledge Quiz",
                 font=("Segoe UI", 22, "bold"),
                 bg="#f5f5f5").pack(pady=(40, 10))

        tk.Label(self.frame,
                 text="Enter Username (Alphanumeric, 3–15 chars):",
                 bg="#f5f5f5",
                 font=("Segoe UI", 14)).pack()

        self.user_entry = tk.Entry(self.frame,
                                    font=("Segoe UI", 14),
                                    width=30,
                                    relief="solid",
                                    borderwidth=2)
        self.user_entry.pack(pady=10)

        ttk.Button(self.frame, text="Start Quiz",
                    command=self.start_quiz).pack(pady=20)   

    def start_quiz(self):
        """
        Validates the username and transitions the UI to the questions.
        Shows an error message if the username does not pass validation.
        """
        username = self.user_entry.get()
        if validate_username(username):
            self.username = username
            self.frame.destroy()
            self.show_question()
        else:
            messagebox.showerror("Invalid Input",
                                 "Please enter a valid username.")      
            
    # --------------------------------------------------------------------------------
    # QUESTION SCREEN
    # --------------------------------------------------------------------------------
    def show_question(self):
        """
        Dynamically generates and displays the current quiz question and its answer options.
        """
        self.q_frame = tk.Frame(self.root, bg="#ffffff")
        self.q_frame.pack(fill="both", expand=True, padx=20, pady=20)

        question = self.engine.questions[self.current_q_index]

        tk.Label(self.q_frame,
                 text=f"Question {self.current_q_index + 1}/{len(self.engine.questions)}",
                 font=("Segoe UI", 14, "bold"),
                 bg="#ffffff").pack(anchor="w")

        tk.Label(self.q_frame,
                 text=question.prompt,
                 wraplength=475,
                 justify="left",
                 bg="#ffffff",
                 font=("Segoe UI", 14)).pack(pady=15, anchor="w")

        self.selected = tk.StringVar(value="")

        for opt in question.options:
            ttk.Radiobutton(self.q_frame,
                            text=opt,
                            value=opt,
                            variable=self.selected).pack(anchor="w", pady=3)

        ttk.Button(self.q_frame,
                    text="Next",
                    command=self.next_question).pack(pady=25)     

    # ---------------------------------------------------------------------------
    # NEXT QUESTION LOGIC
    # ---------------------------------------------------------------------------
   
    def next_question(self):
        """
        Processes the selected answer and uses the engine to save results.
        """
        chosen = self.selected.get()

        if chosen == "":
            messagebox.showwarning("No Selection", "Please choose an answer.")
            return

        # Check answer
        if chosen == self.engine.questions[self.current_q_index].answer:
            self.score += 1

        self.current_q_index += 1

        # Check if quiz is over
        if self.current_q_index >= len(self.engine.questions):
            # Hand off data storage to the engine
            self.engine.export_results(self.username, self.score)
            
            messagebox.showinfo("Success", f"Quiz Complete! Score: {self.score}\nResults saved.")
            self.root.destroy()
            return

        self.q_frame.destroy()
        self.show_question()       


if __name__ == "__main__":
    root = tk.Tk()
    app = RegExQuizApp(root)
    root.mainloop()        