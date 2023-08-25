from tkinter import *
import pandas as pd
import random

# Initial constants
BLACK = '#1e1f22'
ORANGE = '#b86b43'
GRAY = '#2b2d30'
FONT_NAME = "Arial"
BLUE = '#487ab4'
PURPLE = '#2a4e9a'

data = pd.read_csv('spanish_words.csv')
word_dict = data.to_dict(orient='records')
words_list = []
user_list = []
right_words = []
counter = 0
countdown = None


# Functions
def text_creation():
    global words_list
    for i in range(0, 51):
        rand_data = random.choice(word_dict)
        text_box.insert(END, f"{rand_data['English']} ")
        words_list.append(rand_data['English'])
    text_box.config(state='disabled')


def typing(event):
    global user_list, counter
    entry.focus()
    new_element = entry.get()
    if new_element != ' ':
        user_list.append(new_element.strip())
        entry.delete(0, END)
        check(new_element.strip())
        counter += 1
    else:
        print('Invalid')
        check(new_element.strip())
        counter += 1


def check(element):
    global user_list, words_list, right_words
    n_word_min = round(len(user_list))
    if element == words_list[counter]:
        right_words.append(element)
        print(element)
    else:
        print('False')
    count_word_min(n_word_min)


def timer(time):
    global countdown
    if time < 0:
        entry.config(state='disabled')
        window.after_cancel(countdown)
        count_chr_min(user_list)
        accuracy()
        print(f'User list: {user_list}')
        print()
    else:
        countdown = window.after(1000, timer, time - 1)
        time_label.config(text=f'Time: {time}')


def start_timer():
    global user_list
    entry.focus()
    count_word_min(0)
    timer(60)


def count_word_min(number):
    word_min.config(text=f'word/min: {number}')


def count_chr_min(char_list):
    char_count = 0
    for word in char_list:
        for letter in word:
            char_count += 1
    char_min.config(text=f'char/min: {char_count}')


def accuracy():
    global user_list, right_words
    percentage = round((len(right_words) / len(user_list))*100, 2)
    accuracy_label.config(text=f"%acc: {percentage}")


# Styling the window
window = Tk()
window. title('Typing Speed Test')
window.config(pady=100, padx=50, bg=BLACK)
window.geometry('600x600')

# Labels
title_1 = Label(text='Typing speed test')
title_1.config(fg='white', bg=BLACK, font=(FONT_NAME, 13))
title_1.grid(row=0, column=1, columnspan=4)

title_2 = Label(text='Test your typing skills')
title_2.config(fg=ORANGE, bg=BLACK, font=(FONT_NAME, 35))
title_2.grid(row=1, column=1, columnspan=4)

time_label = Label(text='Time: 00')
time_label.config(fg=BLUE, bg=BLACK, font=(FONT_NAME, 10))
time_label.grid(row=2, column=1, columnspan=1, pady=20)

word_min = Label(text='word/min: 0')
word_min.config(fg=BLUE, bg=BLACK, font=(FONT_NAME, 10))
word_min.grid(row=2, column=2, columnspan=1)

char_min = Label(text='char/min: 0')
char_min.config(fg=BLUE, bg=BLACK, font=(FONT_NAME, 10))
char_min.grid(row=2, column=3, columnspan=1)

accuracy_label = Label(text='%acc: 0')
accuracy_label.config(fg=BLUE, bg=BLACK, font=(FONT_NAME, 10))
accuracy_label.grid(row=2, column=4, columnspan=1)

# Text
text_box = Text(height=7, width=55)
text_box.config(fg='white', bg=GRAY, font=25, pady=15, padx=15, wrap=WORD)
text_box.grid(row=3, column=1, columnspan=4)
text_creation()

# Entry
entry = Entry(width=25)
entry.config(bg=GRAY, fg='white', insertbackground='white')
entry.grid(row=4, column=1, columnspan=4, pady=20,)
window.bind("<space>", typing)

start_btn = Button(text='Start', command=start_timer)
start_btn.grid(row=5, column=1, columnspan=4)

window.mainloop()
