import sys
import tkinter as tk
from tkinter import messagebox
import time
import pygame
from PIL import Image, ImageTk

pygame.mixer.init()
correct_sound = pygame.mixer.Sound("assets/Quizzes/correct.mp3")
wrong_sound = pygame.mixer.Sound("assets/Quizzes/wrong.mp3")
time_sound = pygame.mixer.Sound("assets/Quizzes/time.wav")
warning_sound = pygame.mixer.Sound("assets/Quizzes/5sec.mp3")
congratulations_sound = pygame.mixer.Sound("assets/Quizzes/congratulations.mp3")

# Set the volume for all sounds
volume_level = 0.1  # Adjust this value as needed
correct_sound.set_volume(volume_level)
wrong_sound.set_volume(volume_level)
time_sound.set_volume(volume_level)
warning_sound.set_volume(volume_level)
congratulations_sound.set_volume(volume_level)
# Initialize the background image index
background_index = -1

background_images = [
    "assets/Quizzes/b2.png",
    "assets/Quizzes/b3.png",
    "assets/Quizzes/b4.png",
    "assets/Quizzes/b5.png",
    "assets/Quizzes/b6.png",
    "assets/Quizzes/b7.png",
    "assets/Quizzes/b9.png",
]

questions = [
    "How many oceans are there in the world'? ___",
    "In which ocean is the Mariana Trench, the deepest point on Earth?",
    "Which ocean has the warmest waters? ___",
    "Which ocean surrounds Antarctica? ___",
    "Which ocean is mostly covered in ice?",
    "What percentage of the Earth's surface is covered by oceans? ___",
    "Where can you find the Gulf Stream, which influences climate patterns?",
]

choices = [
    ["  4  ", "  5  ", "  6  ", "  7  ", "  8  "],
    ["Pacific", "Atlantic", "Southern", "Arctic"],
    ["Southern", "Pacific", "Indian", "Arctic"],
    ["Pacific", "Southern", "Atlantic", "Arctic"],
    ["Pacific", "Atlantic", "Indian", "Arctic"],
    ["  50%  ", "  60%  ", "  70%  ", "  80%  "],
    ["Atlantic", "Pacific", "Indian", "Arctic"],
]

correct_choices = [1, 0, 2, 1, 3, 2, 0]

hints = [
    "There are several, but not as many as continents.",
    "This ocean is also the largest.",
    "This ocean is famous for its coral reef, the Great Barrier Reef.",
    "Think about the ocean that surrounds the southernmost continent.",
    "This ocean surrounds the North Pole.",
    "It's definitely above 60%.",
    "It's separating the Americas from Europe and Africa."
]


current_question = 0
score = 0
hint_used = 0
total_hints = 2
gold = 0

start_time = 0
timer_running = False
time_remaining = 30


# Function to change the background image
def change_background():
    global background_index
    background_index = (background_index + 1) % len(background_images)
    image_path = background_images[background_index]
    bg_image = Image.open(image_path)
    bg_image = bg_image.resize((900, 700))
    background_new = ImageTk.PhotoImage(bg_image)
    background_label.configure(image=background_new)
    background_label.image = background_new
    root.update()  # Update the root window to apply the new background


def start_timer():
    global start_time, timer_running
    start_time = time.time()
    timer_running = True


def stop_timer():
    global timer_running
    timer_running = False



def gold_update():
    global gold
    gold = gold + 10 + time_remaining
    gold_label.config(text=f"Gold: {gold}")


def check_answer(choice):
    global current_question, score, time_remaining
    if timer_running:
        stop_timer()
        if choice == correct_choices[current_question]:
            correct_sound.play()
            messagebox.showinfo("Correct!", "That's the right answer!")
            score += 1
            change_background()  # Change the background on correct answer
            gold_update()
            update_score_label()
        else:
            wrong_sound.play()
            messagebox.showerror("Incorrect", "Sorry, that's not correct. Try again.")
            update_score_label()
        current_question += 1
        if current_question < len(questions):
            show_question(current_question)
            start_timer()
            time_remaining = 30
            hint_button.config(state=tk.NORMAL)
        else:
            quiz_completed()
        update_timer_label()


def update_hint_label():
    hint_label.config(text=f"{total_hints - hint_used}/{total_hints}")


def use_hint():
    global hint_used
    if hint_used < total_hints:
        hint_index = current_question
        hint_message = hints[hint_index]
        messagebox.showinfo("Hint", hint_message)
        hint_used += 1
        update_hint_label()
        if hint_used == total_hints:
            hint_button.config(state=tk.DISABLED)


def show_question(question_number):
    question_text = questions[question_number]
    question_label.config(text=question_text, font=("Arial", 18))
    answer_buttons[0].config(text=choices[question_number][0])
    answer_buttons[1].config(text=choices[question_number][1])
    answer_buttons[2].config(text=choices[question_number][2])
    answer_buttons[3].config(text=choices[question_number][3])
    start_timer()
    update_timer_label()
    if hint_used == total_hints:
        hint_button.config(state=tk.DISABLED)


def update_score_label():
    score_label.config(text=f"Score: {score}/{len(questions)}")


def update_timer_label():
    timer_label.config(text=f"Time remaining: {time_remaining} seconds")


warning_sound_played = False


def check_timer():
    global timer_running, time_remaining, current_question, hint_used, warning_sound_played, start_time
    if timer_running:
        current_time = time.time()
        elapsed_time = current_time - start_time
        time_remaining = max(0, 30 - int(elapsed_time))
        if time_remaining == 0:
            stop_timer()
            time_sound.play()
            messagebox.showinfo("Time's Up!", "You ran out of time for this question.")
            current_question += 1
            if current_question < len(questions):
                show_question(current_question)
            else:
                quiz_completed()
            update_score_label()
            hint_button.config(state=tk.NORMAL)
            warning_sound_played = False
        elif time_remaining == 5 and not warning_sound_played:
            warning_sound.play()
            warning_sound_played = True
        update_timer_label()


perfect_quiz1 = False


def quiz_completed():
    global score, perfect_quiz1
    if score == len(questions):
        congratulations_sound.play()
        messagebox.showinfo("Congratulations!", f"You got {score}/{len(questions)} correct!\nQuiz Completed")

        if score == len(questions):
            perfect_quiz1 = True
            print("Gold:", gold)
            sys.exit(int(perfect_quiz1))
        else:
            answer = messagebox.askquestion("Quiz Completed", "Do you want to continue or redo the test?")
            if answer == 'yes':
                restart_quiz()
            else:
                root.destroy()
    else:
        messagebox.showinfo("Quiz Completed", f"You got {score}/{len(questions)} correct.")
        answer = messagebox.askquestion("Quiz Completed", "You didn't get the treasure try again?")
        if answer == 'yes':
            restart_quiz()
        else:
            root.destroy()


def restart_quiz():
    global current_question, score, hint_used, gold, background_index
    current_question = 0
    score = 0
    hint_used = 0
    gold = 0
    gold_label.config(text=f"Gold: {gold}")
    show_question(current_question)
    update_score_label()
    update_hint_label()
    set_initial_background()
    background_index = -1


root = tk.Tk()
root.title("")
root.overrideredirect(True)

# Variables for window dragging
dragging = False
start_x = 0
start_y = 0


def set_initial_background():
    global background_index
    background = Image.open("assets/Quizzes/b1.png")
    background = background.resize((900, 700))
    background_main = ImageTk.PhotoImage(background)
    background_label.configure(image=background_main)
    background_label.image = background_main
    background_index -= 1


# Define a function to handle mouse button press event
def on_mouse_press(event):
    global dragging, start_x, start_y
    dragging = True
    start_x = event.x_root - root.winfo_x()
    start_y = event.y_root - root.winfo_y()


# Define a function to handle mouse motion event (dragging)
def on_mouse_motion(event):
    if dragging:
        x = event.x_root - start_x
        y = event.y_root - start_y
        root.geometry(f"+{x}+{y}")


# Define a function to handle mouse button release event
def on_mouse_release(event):
    global dragging
    dragging = False


# Bind mouse events to the root window
root.bind("<ButtonPress-1>", on_mouse_press)
root.bind("<ButtonRelease-1>", on_mouse_release)
root.bind("<B1-Motion>", on_mouse_motion)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.resizable(False, False)

image = Image.open("assets/Quizzes/b1.png")
image = image.resize((900, 700))
background_image = ImageTk.PhotoImage(image)

background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)


window_width = 900
window_height = 700
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

hint_image = Image.open("assets/Quizzes/hint.jpg")
hint_image = hint_image.resize((40, 40))
hint_photo = ImageTk.PhotoImage(hint_image)

question_label = tk.Label(root, text="", font=("Arial", 20), bg="black", fg="white", bd=2, relief=tk.SOLID, padx=20,
                          pady=10)
question_label.pack(pady=20)


answer_buttons = []
for i in range(4):
    answer_button = tk.Button(root, text="", font=("Arial", 16), bd=3, relief=tk.SOLID,
                              command=lambda i=i: check_answer(i))
    answer_button.pack(pady=7)
    answer_buttons.append(answer_button)

score_label = tk.Label(root, text="Score: 0/7", font=("Arial", 18), bg="lightblue", fg="black", bd=2, relief=tk.SOLID)
score_label.place(relx=0.95, rely=0.30, anchor="se")


gold_label = tk.Label(root, text="Gold: 0", font=("Arial", 18), bg="gold", fg="black", bd=2, relief=tk.SOLID)
gold_label.pack(side=tk.TOP, pady=140)

timer_label = tk.Label(root, text="Time remaining: 30 seconds", font=("Arial", 18), bg="brown", fg="white", bd=2,
                       relief=tk.SOLID)
timer_label.pack(side=tk.BOTTOM, pady=10)

hint_frame = tk.Frame(root, bd=2, relief=tk.SOLID, bg="white")
hint_frame.place(relx=0.95, rely=0.15, anchor="ne")

hint_button = tk.Button(hint_frame, image=hint_photo, command=use_hint,  bd="0", bg="white")
hint_button.image = hint_photo
hint_button.pack(side=tk.LEFT)

hint_label = tk.Label(hint_frame, text=f"{total_hints - hint_used}/{total_hints}", font=("Helvetica", 14),
                      fg="black", bg="white")
hint_label.pack(side=tk.RIGHT)

question_label.pack(pady=20)

show_question(current_question)


def close_window():
    confirm = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit the quiz?")
    if confirm:
        root.destroy()


def restart_button():
    confirm = messagebox.askyesno("Confirm Restart", "Are you sure you want to restart the quiz?")
    if confirm:
        restart_quiz()


# redo button
redo_image = Image.open("assets/Quizzes/redo.png")
redo_image = redo_image.resize((50, 50))
redo_photo = ImageTk.PhotoImage(redo_image)

redo_button = tk.Button(root, image=redo_photo, command=restart_button, bd=4, bg="white", relief=tk.SOLID)
redo_button.image = redo_photo
redo_button.place(relx=1, rely=0, anchor="ne")

# exit button
close_image = Image.open("assets/Quizzes/close.png")
close_image = close_image.resize((50, 50))
close_photo = ImageTk.PhotoImage(close_image)

close_button = tk.Button(root, image=close_photo, command=close_window, bd=4, bg="white", relief=tk.SOLID)
close_button.image = close_photo
close_button.place(relx=0, rely=0, anchor="nw")


def update_timer():
    check_timer()
    root.after(1000, update_timer)


update_timer()


root.mainloop()
