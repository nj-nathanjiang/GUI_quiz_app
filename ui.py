from tkinter import *
from PIL import ImageTk, Image
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"),
                                                     width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = ImageTk.PhotoImage(Image.open("images/true.jpg"))
        false_image = ImageTk.PhotoImage(Image.open("images/false.jpg"))
        self.true_button = Button(image=true_image,
                                  highlightthickness=0,
                                  command=self.user_input_true)
        self.false_button = Button(image=false_image,
                                   highlightthickness=0,
                                   command=self.user_input_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.question_number == 10:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You are at the end\n"
                                        f"Your final score was: {self.quiz.score}/{self.quiz.question_number}",
                                   justify="center")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

    def user_input_true(self):
        self.quiz.check_answer("True")
        self.give_feedback()

    def user_input_false(self):
        self.quiz.check_answer("False")
        self.give_feedback()

    def give_feedback(self):
        self.canvas.itemconfig(self.question_text, text="Your answer has been recorded.")
        self.window.after(1000, self.get_next_question)
