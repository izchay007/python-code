import random
import tkinter as tk
from tkinter import ttk, Entry, Button, Label

def pick_random_word(word_array):
    return random.choice(word_array)

def should_stop():
    user_input = input_entry.get().strip()
    return user_input.lower() == 'stop'

def pick_and_display_word():
    global picked_words
    if picked_words == len(words):
        print("All inputs have been selected.")
        output_label.config(text="All words have been picked.")
        input_entry.config(state=tk.DISABLED)
        stop_button.config(state=tk.DISABLED)
    else:
        while True:
            word = pick_random_word(words)
            if word not in picked_words:
                picked_words.append(word)
                break

        result_label.config(text=f"Random word: {word}")

# Sample word array
words = ["洗厕所", "吸地上", "扫楼梯"]

# Global variable to keep track of picked words
picked_words = []

# Create Tkinter window
window = tk.Tk()
window.title("Random Word Picker")

# Create and pack widgets
input_label = Label(window, text="Enter 'stop' to stop:")
input_label.pack(pady=5)

input_entry = Entry(window)
input_entry.pack(pady=5)

result_label = Label(window, text="")
result_label.pack(pady=10)

stop_button = Button(window, text="Pick Random Word", command=pick_and_display_word)
stop_button.pack(pady=10)

# Bind the Enter key to the stop button
window.bind('<Return>', lambda event=None: stop_button.invoke())

# Set focus on the entry widget
input_entry.focus()

# Start the Tkinter main loop
window.mainloop()