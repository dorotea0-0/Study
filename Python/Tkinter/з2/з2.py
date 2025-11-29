import tkinter as tk
from tkinter import messagebox
import os

QUESTION_FILE = "questions.txt"

def parse_questions(filename):
    if not os.path.exists(filename):
        messagebox.showerror("Ошибка", f"Файл {filename} не найден!")
        return []

    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.rstrip() for line in f]

    questions = []
    current_question = None
    current_options = []
    current_correct = []

    for line in lines:
        if line.startswith("q:"):
            if current_question is not None:
                questions.append({
                    "text": current_question,
                    "options": current_options,
                    "correct": current_correct,
                    "multiple": len(current_correct) > 1
                })
            current_question = line[2:].strip()
            current_options = []
            current_correct = []
        elif line and line[0].isdigit() and '.' in line:
            option_text = line.split('.', 1)[1].strip()
            is_correct = option_text.endswith('+')
            if is_correct:
                option_text = option_text[:-1].rstrip()
                current_correct.append(len(current_options))
            current_options.append(option_text)
        elif not line.strip() and current_question:
            questions.append({
                "text": current_question,
                "options": current_options,
                "correct": current_correct,
                "multiple": len(current_correct) > 1
            })
            current_question = None
            current_options = []
            current_correct = []
    if current_question is not None:
        questions.append({
            "text": current_question,
            "options": current_options,
            "correct": current_correct,
            "multiple": len(current_correct) > 1
        })

    return questions


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Тестовая система")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.questions = parse_questions(QUESTION_FILE)
        if not self.questions:
            self.root.destroy()
            return

        self.current_index = 0
        self.score = 0
        self.total = len(self.questions)
        self.user_answers = [None] * self.total

        self.setup_ui()

    def setup_ui(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14), wraplength=550, justify="left")
        self.question_label.pack(pady=20)

        self.var_list = []
        self.checkbuttons = []

        self.next_button = tk.Button(self.root, text="Ответить", command=self.submit_answer, font=("Arial", 12))
        self.next_button.pack(side="bottom", pady=20)

        self.show_question()

    def show_question(self):
        for cb in self.checkbuttons:
            cb.destroy()
        self.checkbuttons.clear()
        self.var_list.clear()

        q = self.questions[self.current_index]
        self.question_label.config(text=f"Вопрос {self.current_index + 1} из {self.total}:\n{q['text']}")

        if q["multiple"]:
            for i, opt in enumerate(q["options"]):
                var = tk.BooleanVar()
                self.var_list.append(var)
                cb = tk.Checkbutton(self.root, text=opt, variable=var, font=("Arial", 12), anchor="w")
                cb.pack(anchor="w", padx=50, pady=2)
                self.checkbuttons.append(cb)
        else:
            self.radio_var = tk.IntVar(value=-1)
            for i, opt in enumerate(q["options"]):
                rb = tk.Radiobutton(self.root, text=opt, variable=self.radio_var, value=i, font=("Arial", 12), anchor="w")
                rb.pack(anchor="w", padx=50, pady=2)
                self.checkbuttons.append(rb)

    def submit_answer(self):
        q = self.questions[self.current_index]
        if q["multiple"]:
            selected = [i for i, var in enumerate(self.var_list) if var.get()]
        else:
            selected = [self.radio_var.get()] if self.radio_var.get() != -1 else []

        self.user_answers[self.current_index] = selected

        if set(selected) == set(q["correct"]):
            self.score += 1

        self.current_index += 1
        if self.current_index < self.total:
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        percent = (self.score / self.total) * 100
        result_text = f"Тест завершён!\n\nПравильных ответов: {self.score} из {self.total}\nПроцент: {percent:.1f}%"

        for widget in self.root.winfo_children():
            widget.destroy()

        result_label = tk.Label(self.root, text=result_text, font=("Arial", 16), justify="center")
        result_label.pack(expand=True)

        restart_button = tk.Button(self.root, text="Пройти снова", command=self.restart_quiz, font=("Arial", 12))
        restart_button.pack(pady=20)

    def restart_quiz(self):
        self.root.destroy()
        root = tk.Tk()
        app = QuizApp(root)
        root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
