# Dependencies
import tkinter as tk
from tkinter import messagebox
from csv import DictReader
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"


# Random word selector
def random_word():
    word = random.choice(wordlist)
    return word["French"]


# Insert random word into canvas
def insert_random_word():
    word = random_word()
    card_canvas.itemconfig(canvas_text, text=word)


# Read CSV and load as list of dictionaries for use in program
try:
    with open("data/french_words.csv", "r") as file:
        wordlist = list(DictReader(file))
except FileNotFoundError:
    messagebox.showerror(
        title="Error!",
        message="Program aborted.\nWord list not found.\n\n"
                "Did you delete the list or the data folder?"
    )
else:
    # UI
    # Initialization
    root = tk.Tk()
    root.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
    root.title("Flashy")

    # PhotoImages
    card_back_img = tk.PhotoImage(file="images/card_back.png")
    card_front_img = tk.PhotoImage(file="images/card_front.png")
    right_img = tk.PhotoImage(file="images/right.png")
    wrong_img = tk.PhotoImage(file="images/wrong.png")

    # Card
    card_canvas = tk.Canvas(
        width=800,
        height=526,
        highlightthickness=0,
        bg=BACKGROUND_COLOR
    )
    card_canvas.create_image(400, 263, image=card_front_img)
    canvas_title = card_canvas.create_text(
        400,
        150,
        text="French",
        fill="black",
        font=("Arial", 40, "italic")
    )
    canvas_text = card_canvas.create_text(
        400,
        263,
        text=random_word(),
        fill="black",
        font=("Arial", 60, "bold")
    )
    card_canvas.grid(columnspan=2, column=0, row=0)

    # Buttons
    wrong_button = tk.Button(
        image=wrong_img,
        height=95,
        width=95,
        highlightthickness=0,
        borderwidth=0,
        command=insert_random_word
    )
    wrong_button.grid(column=0, row=1)

    right_button = tk.Button(
        image=right_img,
        height=95,
        width=95,
        highlightthickness=0,
        borderwidth=0,
        command=insert_random_word
    )
    right_button.grid(column=1, row=1)

    # Start loop
    root.mainloop()
