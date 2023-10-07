import tkinter as tk
from PIL import Image, ImageTk
import os

# Create a tkinter window
window = tk.Tk()
window.title("Treasure Loot")
window.iconbitmap('assets/Prizes/achievements.ico')

window.configure(bg='light blue')

# Make the window non-resizable
window.resizable(width=False, height=False)

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the x and y coordinates for the window to be centered
x = (screen_width - 430) // 2
y = (screen_height - 400) // 2

# Set the window's size and position
window.geometry("550x260+{}+{}".format(x, y))

# Retrieve the value of the environment variable
level_check = os.environ.get("Prize Level")


def get_image(i):
    if level_check == "1":
        if i == 1:
            return Image.open('assets/Prizes/Loot_1.png').resize((130, 130))
        else:
            return Image.open('assets/Prizes/locked.png').resize((150, 150))
    elif level_check == "2":
        if i <= 2:
            if i == 1:
                return Image.open('assets/Prizes/Loot_1.png').resize((130, 130))
            else:
                return Image.open('assets/Prizes/Loot_2.png').resize((140, 140))
        else:
            return Image.open('assets/Prizes/locked.png').resize((155, 155))
    elif level_check == "3":
        if i == 1:
            return Image.open('assets/Prizes/Loot_1.png').resize((130, 130))
        elif i == 2:
            return Image.open('assets/Prizes/Loot_2.png').resize((140, 140))
        elif i == 3:
            return Image.open('assets/Prizes/Loot_3.png').resize((150, 150))
    else:
        return Image.open('assets/Prizes/locked.png').resize((150, 150))


# Load and resize the three images or locked image based on the environment variable
image1 = ImageTk.PhotoImage(get_image(1))
image2 = ImageTk.PhotoImage(get_image(2))
image3 = ImageTk.PhotoImage(get_image(3))

label1 = tk.Label(window, image=image1, bg="light blue")
label2 = tk.Label(window, image=image2, bg="light blue")
label3 = tk.Label(window, image=image3, bg="light blue")

# Use the pack method with 'side' set to 'left' to arrange them horizontally
label1.pack(side="left", padx=20)
label2.pack(side="left", padx=20)
label3.pack(side="left", padx=20)

# Create labels for the text "Level 1," "Level 2," and "Level 3" with styling
font_style = ("Helvetica", 12, "bold")
text_color = "#333333"  # Dark gray color


# Function to determine label text based on the environment variable
def get_label_text(i):
    if level_check == "1" and i == 1:
        return "Land Discoverer"
    elif level_check == "2" and i <= 2:
        if i == 1:
            return "Land Discoverer"
        elif i == 2:
            return "Sea Explorer"
    elif level_check == "3":
        if i == 1:
            return "Land Discoverer"
        elif i == 2:
            return "Sea Explorer"
        elif i == 3:
            return "Pirate Captain"
    return "Locked"


level_label1 = tk.Label(window, text=get_label_text(1), font=font_style, foreground="blue", bg="light blue")
level_label2 = tk.Label(window, text=get_label_text(2), font=font_style, foreground="green", bg="light blue")
level_label3 = tk.Label(window, text=get_label_text(3), font=font_style, foreground="red", bg="light blue")

# Use the place method to specify positions for the text labels relative to image labels
level_label1.place(in_=label1, relx=0.5, rely=-0.2, anchor="center")
level_label2.place(in_=label2, relx=0.5, rely=-0.2, anchor="center")
level_label3.place(in_=label3, relx=0.5, rely=-0.2, anchor="center")

# Create three additional labels with different text and styling
level_label4 = tk.Label(window, text="Level 1", font=font_style, foreground=text_color, bg="light blue")
level_label5 = tk.Label(window, text="Level 2", font=font_style, foreground=text_color, bg="light blue")
level_label6 = tk.Label(window, text="Level 3", font=font_style, foreground=text_color, bg="light blue")

# Use the place method to specify positions for the additional text labels relative to image labels
level_label4.place(in_=label1, relx=0.5, rely=1.2, anchor="center")
level_label5.place(in_=label2, relx=0.5, rely=1.2, anchor="center")
level_label6.place(in_=label3, relx=0.5, rely=1.2, anchor="center")



# Run the tkinter main loop
window.mainloop()
