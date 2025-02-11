import tkinter as tk
from tkinter import messagebox
import time
import threading

quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Madrid", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A) Python", "B) JavaScript", "C) C++", "D) Java"],
        "answer": "B"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A) 6", "B) 8", "C) 7", "D) 9"],
        "answer": "B"
    }
]

SCORE_FILE = "quiz_scores.txt"

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Application")
        self.question_index = 0
        self.score = 0
        self.time_left = 10  

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 12), width=20, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.timer_label = tk.Label(root, text=f"Time left: {self.time_left}s", font=("Arial", 12), fg="red")
        self.timer_label.pack(pady=20)

        self.next_question()

    def next_question(self):
        if self.question_index < len(quiz_data):
            self.time_left = 15
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.update_timer()
            
            q_data = quiz_data[self.question_index]
            self.question_label.config(text=q_data["question"])
            for i, option in enumerate(q_data["options"]):
                self.option_buttons[i].config(text=option, state=tk.NORMAL)
        else:
            self.end_quiz()

    def check_answer(self, index):
        correct_answer = quiz_data[self.question_index]["answer"]
        user_choice = self.option_buttons[index].cget("text")[0]

        if user_choice == correct_answer:
            self.score += 1
            
        else:
            messagebox.showerror("Result", f"❌ Wrong! Correct answer: {correct_answer}")

        self.question_index += 1
        self.next_question()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time left: {self.time_left}s")
            self.root.after(2000, self.update_timer)
        else:
            messagebox.showwarning("Time's Up!", "⏳ You ran out of time!")
            self.question_index += 1
            self.next_question()

    def end_quiz(self):
        messagebox.showinfo("Quiz Over", f"🎉 Your score: {self.score}/{len(quiz_data)}")
        self.save_score()
        self.root.quit()

    def save_score(self):
        with open(SCORE_FILE, "a") as file:
            file.write(f"Score: {self.score}/{len(quiz_data)}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
