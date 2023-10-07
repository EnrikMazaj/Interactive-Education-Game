import subprocess
import sys
import pygame.mixer
import pygame.freetype
import tkinter as tk
from tkinter import messagebox
import textwrap
from tkinter import simpledialog
import os
import ctypes

# Set the SDL_VIDEO_CENTERED environment variable to center the pygame window
os.environ['SDL_VIDEO_CENTERED'] = '1'
print("Current working directory:", os.getcwd())
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("./assets/Main/song.mp3")
pygame.mixer.music.play(-1)  # Loop for the song

# Dimensions of pygame window
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pirates of Knowledge")

# Get the window's HWND
hwnd = pygame.display.get_wm_info()["window"]

# Set the window as always on top
ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002 | 0x0020)


def images_load(path, width, height):
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (width, height))
    return image


# Define image variables
title_image = images_load('./assets/Main/title.png', 600, 400)
background_image = images_load('./assets/Main/bg.jpg', 900, 700)
pre_quiz_bg = images_load('./assets/Main/blue.jpg', 900, 700)
background1_image = images_load('./assets/Main/bg1.jpg', 900, 700)
background2_image = images_load('./assets/Main/bg2.jpg', 900, 700)
background3_image = images_load('./assets/Main/bg3.jpg', 900, 700)
background4_image = images_load('./assets/Main/bg4.jpg', 900, 700)
background5_image = images_load('./assets/Main/bg5.jpg', 900, 700)
background6_image = images_load('./assets/Main/bg6.jpg', 900, 700)
background7_image = images_load('./assets/Main/bg7.jpg', 900, 700)
background8_image = images_load('./assets/Main/bg8.jpg', 900, 700)
photo_bg1 = images_load('./assets/Main/blue1.jpg', 900, 700)
photo_bg2 = images_load('./assets/Main/blue2.jpg', 900, 700)
photo_bg3 = images_load('./assets/Main/blue3.jpg', 900, 700)
photo_bg4 = images_load('./assets/Main/blue4.jpg', 900, 700)
ending_bg = images_load('./assets/Main/end_screen.jpg', 900, 700)
pygame_icon = images_load('./assets/Main/ico.ico', 32, 32)
next_button_image = images_load('./assets/Main/button_next.png', 100, 50)
treasure_image = images_load('./assets/Prizes/gold.png', 80, 80)
locked_button_image = images_load('./assets/Main/locked_next.png', 100, 50)
back_button_image = images_load('./assets/Main/button_back.png', 100, 50)
start_button_image = images_load('./assets/Main/start.png', 200, 50)
start_quiz_image = images_load('./assets/Main/Quiz1.png', 150, 50)
achievements_image = images_load('./assets/Main/chest.png', 130, 120)
pirate_image = images_load('./assets/Main/pirate.png', 200, 200)
mute_button_image = images_load('./assets/Main/mute1.jpg', 40, 40)
volume_on = images_load('./assets/Main/volume_on.png', 45, 36)
volume_down = images_load('./assets/Main/minus.png', 30, 30)
volume_up = images_load('./assets/Main/plus.png', 30, 30)
prize1 = images_load('./assets/Prizes/Loot_1.png', 107, 107)
prize2 = images_load('./assets/Prizes/Loot_2.png', 110, 110)
prize3 = images_load('./assets/Prizes/Loot_3.png', 110, 110)
cursor = images_load('./assets/Main/cursor.png', 50, 50)
hand_cursor = images_load('./assets/Main/hand_cursor.png', 50, 50)


root = tk.Tk()
root.wm_withdraw()
root.iconbitmap("./assets/Main/locked.ico")
pygame.display.set_icon(pygame_icon)


# cursor
basic_cursor = pygame.cursors.Cursor((1, 1), cursor)
hand_cursor = pygame.cursors.Cursor((1, 1), hand_cursor)

# title coordinates
panel_width, panel_height = 500, 55


# Button next coordinates
next_button_x, next_button_y = screen_width - 120, screen_height - 80

# Button start quiz coordinates
start_quiz_x, start_quiz_y = (screen_width - 100) / 2, (screen_height - 500)

# Button locked coordinates
locked_button_x, locked_button_y = screen_width - 120, screen_height - 80

# gold coin coordinates
treasure_image_x, treasure_image_y = (screen_width - 80) / 2, screen_height - 100

# Button back coordinates
back_button_x, back_button_y = 20, screen_height - 80

# title coordinates
title_image_x, title_image_y = (screen_width - 550) // 2, -100

#  pirate coordinates
pirate_image_x, pirate_image_y = (screen_width - 150) / 2, screen_height - 400

# pirate coordinates for ending screen
pirate1_image_x, pirate1_image_y = screen_width - 300, screen_height - 540

# prizes coordinates
prize1_x, prize1_y = screen_width - 830, screen_height - 400
prize2_x, prize2_y = screen_width - 700, screen_height - 400
prize3_x, prize3_y = screen_width - 570, screen_height - 400

# start coordinates
start_button_x, start_button_y = screen_width - 230, screen_height - 80

# achievements coordinates
achievements_x, achievements_y = screen_width - 140, screen_height - 720

# Coordinates x,y
volume_buttons_x, volume_buttons_y = 10, 10
volume_on_x, volume_on_y = 10, 10

# Define the coordinates for the volume up and down buttons
volume_up_x, volume_up_y = volume_buttons_x + 50, volume_buttons_y
volume_down_x, volume_down_y = volume_buttons_x + 80, volume_buttons_y


# Initial volume level (0.3 for 30% volume)
volume_level = 0.3
pygame.mixer.music.set_volume(volume_level)

# Create a font object
font = pygame.freetype.Font(None, 36)

# Chapters panel
panel_x, panel_y = (screen_width - panel_width) // 2, 10

# Font for coins number
number_font = pygame.freetype.Font(None, 35)
number_color = (255, 215, 0)  # Gold color


texts_to_display = [
    "Ahoy there, matey! Welcome aboard the adventure of a lifetime!",
    "I be Captain Knowledge, and you're about to embark on a quest to test your geography expertise.",
    "But before we hoist the anchor, what's your name, brave explorer?",
    "Alright, [Your Name], prepare to set sail into uncharted waters!",
    "A great pirate must know the lands well, so get ready for your first lesson."
]

texts_to_display_quiz1 = [
    "You have reached your first challenge!",
    "The lands and continents hold the keys to your path. Each one hides its own treasures and perils.",
    "Let's test your knowledge! You will have to answer 6 simple questions to proceed.",
    "If you succeed, you can check your loot at the top right and the coins you have gathered at the bottom.",
    "You can press the hint button if you need my help. Good Luck..."
]

texts_to_display_quiz2 = [
    "You have reached the Ocean Quiz!",
    "In the life of a pirate, the sea is their home. You must learn the ways of the oceans to navigate its mysteries.",
    "Prepare to test your knowledge of the vast and uncharted waters.      7 questions await you...!",
]

texts_to_display_quiz3 = [
    "You have reached the final and most demanding challenge.",
    "To sail these treacherous seas, you must be a master navigator.",
    "So understanding the climate is crucial to having a safe course.",
    "Let's see if you have the knowledge to become a legendary captain!"
]

texts_congratulations = [
    "Good job, Pirate [Your Name]! You made it."
]

texts_ending = [
    "Congratulations, you will be a worthy Captain! You have finished all the quests, Here are your prizes."
]

# Flags
running = True
volume_muted = False
gold = 0
user_name = ""
prize_level = "0"
current_page = "main"
perfect_quiz1 = False
perfect_quiz2 = False
perfect_quiz3 = False
text_index_main = 0
text_index_quiz1 = 0
text_index_quiz2 = 0
text_index_quiz3 = 0
start_button_flag = False
num_texts_to_display = len(texts_to_display)
num_texts_to_display_quiz1 = len(texts_to_display_quiz1)
num_texts_to_display_quiz2 = len(texts_to_display_quiz2)
num_texts_to_display_quiz3 = len(texts_to_display_quiz3)
# Initialize bubble_rect
bubble_rect = pygame.Rect(0, 0, 0, 0)


def gold_update():
    global gold
    number_surface, _ = number_font.render(str(gold), number_color)
    number_x = treasure_image_x + treasure_image.get_width() + 10  # Adjust the position as needed
    number_y = treasure_image_y + 30  # Adjust the position as needed
    screen.blit(number_surface, (number_x, number_y))


def name_update():
    global user_name  # Declare user_name as a global variable
    while True:  # Keep prompting until a name is entered
        user_name = simpledialog.askstring("X", "What's your name?")
        # Check if the user entered a name
        if user_name:
            # Capitalize the first letter of the name if it's not already capitalized
            user_name = user_name.strip().capitalize()
            return user_name  # Return the entered name

        # If no name is entered, show an error message
        messagebox.showerror("Error", "You must enter a name to continue. Please try again.")
        user_name = "Anonymous"  # Set a default name (e.g., "Anonymous") if no name is entered


def adjust_volume(increase):
    global volume_level
    if increase:
        volume_level = min(1.0, volume_level + 0.1)
    else:
        volume_level = max(0.0, volume_level - 0.1)
    pygame.mixer.music.set_volume(volume_level)


def audio_button_check():
    global volume_muted, volume_level

    if volume_buttons_x <= mouse_x <= volume_buttons_x + 30 \
            and volume_buttons_y <= mouse_y <= volume_buttons_y + 30:
        if volume_muted:
            pygame.mixer.music.set_volume(volume_level)
            volume_muted = False
        else:
            pygame.mixer.music.set_volume(0.0)
            volume_muted = True

    # Check if the volume down button is clicked
    elif volume_buttons_x + 40 <= mouse_x <= volume_buttons_x + 70 \
            and volume_buttons_y <= mouse_y <= volume_buttons_y + 30:
        if volume_muted:
            pygame.mixer.music.set_volume(volume_level)  # volume on
            volume_muted = False
        else:
            adjust_volume(False)  # Decrease volume by 20%

    # Check if the volume up button is clicked
    elif volume_buttons_x + 80 <= mouse_x <= volume_buttons_x + 110 \
            and volume_buttons_y <= mouse_y <= volume_buttons_y + 30:
        if volume_muted:
            pygame.mixer.music.set_volume(volume_level)
            volume_muted = False
        else:
            adjust_volume(True)

    # Check if the down key is pressed
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        if volume_muted:
            pygame.mixer.music.set_volume(volume_level)
            volume_muted = False
        else:
            adjust_volume(False)

    # Check if the up key is pressed
    elif pygame.key.get_pressed()[pygame.K_UP]:
        if volume_muted:
            pygame.mixer.music.set_volume(volume_level)
            volume_muted = False
        else:
            adjust_volume(True)


def draw_speech_bubble(content, pirate_x, pirate_y, text_index, maximum, max_width=300, font_size=24):
    global bubble_rect
    if text_index == maximum:
        return  # Stop drawing if the current text index exceeds the end index
    text = content[text_index].replace("[Your Name]", user_name)
    wrapped_text = textwrap.fill(text, 35)
    lines = wrapped_text.split('\n')

    max_line_width = max([pygame.font.Font(None, font_size).size(line)[0] for line in lines])
    bubble_width = max(max_width, max_line_width + 2 * 10)
    bubble_height = len(lines) * font_size + 2 * 10

    if pirate_x == (screen_width - 300):
        bubble_rect = pygame.Rect(pirate_x - 50, pirate_y - 80, bubble_width, bubble_height)
    else:
        bubble_rect = pygame.Rect(pirate_x + 155, pirate_y - 120, bubble_width, bubble_height)
    pygame.draw.rect(screen, (0, 0, 0), bubble_rect)

    polygon_points = [
        (bubble_rect.left, bubble_rect.bottom),
        (bubble_rect.left + 30, bubble_rect.bottom),
        (bubble_rect.left, bubble_rect.bottom + 20)
    ]
    pygame.draw.polygon(screen, (0, 0, 0), polygon_points)

    y_offset = 1
    for line in lines:
        text = pygame.font.Font(None, font_size).render(line, True, (255, 250, 250))
        screen.blit(text, (bubble_rect.left + 10, bubble_rect.top + 10 + y_offset))
        y_offset += font_size


def handle_page_transition(next_lesson, prev_lesson, current):
    global current_page
    if back_button_x <= mouse_x <= back_button_x + 150 and back_button_y <= mouse_y <= back_button_y + 70:
        current_page = prev_lesson

    if next_button_x <= mouse_x <= next_button_x + 150 and next_button_y <= mouse_y <= next_button_y + 70:
        current_page = next_lesson

    if achievements_x <= mouse_x <= achievements_x + 130 and achievements_y <= mouse_y <= achievements_y + 120:
        current_page = "Prizes"
        result = subprocess.Popen(["python", "Prizes.py"], env={"Prize Level": prize_level},
                                  creationflags=subprocess.CREATE_NO_WINDOW)
        result.wait()
        if result.returncode == 0:
            current_page = current


def handle_pre_quiz_transition(current, next_lesson, prev_lesson, start_quiz_flag, text_index, max_index):
    global current_page
    if back_button_x <= mouse_x <= back_button_x + 150 and back_button_y <= mouse_y <= back_button_y + 70:
        current_page = prev_lesson
    if achievements_x <= mouse_x <= achievements_x + 130 and achievements_y <= mouse_y <= achievements_y + 120:
        current_page = "Prizes"
        result = subprocess.Popen(["python", "Prizes.py"], env={"Prize Level": prize_level},
                                  creationflags=subprocess.CREATE_NO_WINDOW)
        result.wait()
        if result.returncode == 0:
            current_page = current
    if not start_quiz_flag and (text_index == max_index):
        if start_quiz_x <= mouse_x <= start_quiz_x + 150 and start_quiz_y <= mouse_y <= start_quiz_y + 70:
            current_page = "Quiz" + current_page[-1]

    if globals().get("perfect_quiz" + current_page[-1]):
        if next_button_x <= mouse_x <= next_button_x + 150 and next_button_y <= mouse_y <= next_button_y + 70:
            current_page = next_lesson
    else:
        if locked_button_x <= mouse_x <= locked_button_x + 150 and locked_button_y <= mouse_y <= locked_button_y + 70:
            messagebox.showinfo('Locked Stage', 'You have to get the prize to continue!')


def render_lesson_page(page_background, title_text):
    # Clear the screen
    screen.fill((0, 0, 0))
    # Draw the background image
    screen.blit(page_background, (0, 0))
    screen.blit(achievements_image, (achievements_x, achievements_y))
    screen.blit(treasure_image, (treasure_image_x, treasure_image_y))
    gold_update()
    # Draw the panel
    pygame.draw.rect(screen, (10, 26, 60, 255), (panel_x, panel_y, panel_width, panel_height), border_radius=25)
    # Draw the title text
    text_surface, _ = font.render(title_text, (255, 255, 255))
    screen.blit(text_surface, (panel_x + (panel_width - text_surface.get_width()) // 2,
                               panel_y + (panel_height - text_surface.get_height()) // 2))
    # Draw common buttons
    screen.blit(back_button_image, (back_button_x, back_button_y))
    screen.blit(next_button_image, (next_button_x, next_button_y))
    if volume_muted:
        screen.blit(mute_button_image, (volume_buttons_x, volume_buttons_y))
    else:
        screen.blit(volume_on, (volume_buttons_x, volume_buttons_y))
    screen.blit(volume_down, (volume_buttons_x + 48, volume_buttons_y))
    screen.blit(volume_up, (volume_buttons_x + 85, volume_buttons_y))


def render_pre_quiz_page(content, lesson_title, finished, text_index, max_index):
    screen.blit(pre_quiz_bg, (0, 0))
    pygame.draw.rect(screen, (34, 52, 66, 255), (panel_x, panel_y, panel_width, panel_height), border_radius=25)
    text_surface, _ = font.render(lesson_title, (255, 255, 255))
    screen.blit(text_surface, (panel_x + (panel_width - text_surface.get_width()) // 2,
                               panel_y + (panel_height - text_surface.get_height()) // 2))
    screen.blit(back_button_image, (back_button_x, back_button_y))
    screen.blit(achievements_image, (achievements_x, achievements_y))
    screen.blit(treasure_image, (treasure_image_x, treasure_image_y))
    screen.blit(pirate_image, (pirate_image_x, pirate_image_y))
    draw_speech_bubble(content, pirate_image_x, pirate_image_y, text_index, max_index)
    # Render and blit the number next to the treasure image
    if volume_muted:
        screen.blit(mute_button_image, (volume_buttons_x, volume_buttons_y))
    else:
        screen.blit(volume_on, (volume_buttons_x, volume_buttons_y))
    screen.blit(volume_down, (volume_buttons_x + 48, volume_buttons_y))
    screen.blit(volume_up, (volume_buttons_x + 85, volume_buttons_y))
    gold_update()
    if not finished and text_index == max_index:
        screen.blit(start_quiz_image, (start_quiz_x, start_quiz_y))
    if finished:
        draw_speech_bubble(texts_congratulations, pirate_image_x, pirate_image_y, 0, 1)
        screen.blit(next_button_image, (next_button_x, next_button_y))
    else:
        screen.blit(locked_button_image, (locked_button_x, locked_button_y))


def render_quiz_page(program, current, variable):
    global gold, current_page, prize_level, perfect_quiz1, perfect_quiz2, perfect_quiz3, screen
    temp_gold = 0  # Initialize temp_gold with a default value
    # Minimize the Pygame window
    process = subprocess.Popen(
        ["python", program], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True, shell=True)
    pygame.display.update()  # Update the Pygame window
    pygame.time.delay(1000)  # Wait for 1000 milliseconds (1 second)
    pygame.display.set_mode((900, 700), flags=pygame.HIDDEN)
    stdout, stderr = process.communicate()
    process.wait()  # Wait for the quiz script to complete
    screen = pygame.display.set_mode((900, 700), flags=pygame.SHOWN)
    # Set the Pygame window as always on top again
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002 | 0x0020)

    if process.returncode == 1:
        # Extract the 'gold' value from the stdout of the quiz script
        output_lines = stdout.split('\n')
        for line in output_lines:
            if line.startswith("Gold: "):
                try:
                    temp_gold = int(line.split(": ")[1])
                except ValueError:
                    temp_gold = 0  # Set a default value if parsing fails
                break

            # Update the corresponding flag based on the quiz being taken
        if variable == "1":
            perfect_quiz1 = True
        elif variable == "2":
            perfect_quiz2 = True
        elif variable == "3":
            perfect_quiz3 = True

        gold = temp_gold + gold
        prize_level = variable
        current_page = current

    else:
        # Show the "Locked" button
        current_page = current
        screen.blit(locked_button_image, (locked_button_x, locked_button_y))


def end_screen_info():
    # Define the text and its properties
    info_text_pirate = f"Pirate: {user_name}"
    info_text_gold = f"Gold: {gold}"
    text_color = (0, 0, 0)  # Black color for the text
    text_font = pygame.freetype.Font(None, 24)  # You can adjust the font size

    # Calculate the text size and position for Pirate name
    text_surface_pirate, _ = text_font.render(info_text_pirate, text_color)
    text_x_pirate = 70
    text_y_pirate = screen_height - 550

    # Calculate the text size and position for Gold information
    text_surface_gold, _ = text_font.render(info_text_gold, text_color)
    text_x_gold = 70
    text_y_gold = text_y_pirate + text_surface_pirate.get_height() + 20  # Add some spacing

    # Draw the Pirate name text directly on the screen
    screen.blit(text_surface_pirate, (text_x_pirate, text_y_pirate))

    # Draw the Gold information text below Pirate name
    screen.blit(text_surface_gold, (text_x_gold, text_y_gold))


def text_management(index, texts_num):
    if pirate_image_x <= mouse_x <= pirate_image_x + pirate_image.get_width() \
            and pirate_image_y <= mouse_y <= pirate_image_y + pirate_image.get_height():
        # Clicked on pirate image
        index += 1
        if index >= texts_num:
            index = texts_num  # make index equal to texts num

    elif bubble_rect.collidepoint(mouse_x, mouse_y):
        # Clicked inside the text area
        index += 1
        if index >= texts_num:
            index = texts_num  # make index equal to texts num
    return index


default_coordinates = [
    (volume_up_x, volume_up_x + 30, volume_up_y, volume_up_y + 30),
    (volume_buttons_x, volume_buttons_x + 35, volume_buttons_y, volume_buttons_y + 35),
    (volume_down_x, volume_down_x + 30, volume_down_y, volume_down_y + 30)
]

main_page_coordinates = default_coordinates + [
    (start_button_x, start_button_x + 200, start_button_y, start_button_y + 50),
    (pirate_image_x, pirate_image_x + 200, pirate_image_y, pirate_image_y + 200)
]

pre_quiz_coordinates = default_coordinates + [
    (start_quiz_x, start_quiz_x + 150, start_quiz_y, start_quiz_y + 50),
    (achievements_x, achievements_x + 130, achievements_y, achievements_y + 120),
    (back_button_x, back_button_x + 100, back_button_y, back_button_y + 50),
    (pirate_image_x, pirate_image_x + 200, pirate_image_y, pirate_image_y + 200),
    (locked_button_x, locked_button_x + 100, locked_button_y, locked_button_y + 50),
]

# Define coordinate sets for lesson pages
lesson_page_coordinates = default_coordinates + [
    (next_button_x, next_button_x + 100, next_button_y, next_button_y + 50),
    (back_button_x, back_button_x + 100, back_button_y, back_button_y + 50),
    (achievements_x, achievements_x + 130, achievements_y, achievements_y + 120),
]

end_page_coordinates = default_coordinates + [
    (back_button_x, back_button_x + 100, back_button_y, back_button_y + 50),
]


while running:
    pygame.time.delay(100)  # Delay for 100 milliseconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            cursor_changed = False  # Initialize a flag to track cursor changes
            if current_page == "main":
                for x1, x2, y1, y2 in main_page_coordinates:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        pygame.mouse.set_cursor(hand_cursor)
                        cursor_changed = True
                        break
            elif current_page in ["Pre-Quiz1", "Pre-Quiz2", "Pre-Quiz3"]:
                for x1, x2, y1, y2 in pre_quiz_coordinates:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        pygame.mouse.set_cursor(hand_cursor)
                        cursor_changed = True
                        break
            elif current_page.startswith("Lesson"):
                for x1, x2, y1, y2 in lesson_page_coordinates:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        pygame.mouse.set_cursor(hand_cursor)
                        cursor_changed = True
                        break
            elif current_page == "Ending-Screen":
                for x1, x2, y1, y2 in end_page_coordinates:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        pygame.mouse.set_cursor(hand_cursor)
                        cursor_changed = True
                        break

            if not cursor_changed:
                pygame.mouse.set_cursor(basic_cursor)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            audio_button_check()

            if current_page == "main":
                if text_index_main == 2:
                    name_update()
                if text_index_main == 4:
                    start_button_flag = True
                text_index_main = text_management(text_index_main, num_texts_to_display)
                if start_button_flag and start_button_x <= mouse_x <= start_button_x + 200 \
                        and start_button_y <= mouse_y <= start_button_y + 70:
                    current_page = "Lesson1-a"

            elif current_page == "Lesson1-a":
                handle_page_transition("Lesson1-b", "main", "Lesson1-a")
            elif current_page == "Lesson1-b":
                handle_page_transition("Lesson1-c", "Lesson1-a", "Lesson1-b")
            elif current_page == "Lesson1-c":
                handle_page_transition("Lesson1-d", "Lesson1-b", "Lesson1-c")
            elif current_page == "Lesson1-d":
                handle_page_transition("Pre-Quiz1", "Lesson1-c", "Lesson1-d")
            elif current_page == "Pre-Quiz1":
                text_index_quiz1 = text_management(text_index_quiz1, num_texts_to_display_quiz1)
                handle_pre_quiz_transition(current_page, "Lesson2-a", "Lesson1-d", perfect_quiz1, text_index_quiz1,
                                           num_texts_to_display_quiz1)

            elif current_page == "Lesson2-a":
                handle_page_transition("Lesson2-b", "Pre-Quiz1", "Lesson2-a")
            elif current_page == "Lesson2-b":
                handle_page_transition("Lesson2-c", "Lesson2-a", "Lesson2-b")
            elif current_page == "Lesson2-c":
                handle_page_transition("Pre-Quiz2", "Lesson2-b", "Lesson2-c")
            elif current_page == "Pre-Quiz2":
                text_index_quiz2 = text_management(text_index_quiz2, num_texts_to_display_quiz2)
                handle_pre_quiz_transition(current_page, "Lesson3-a", "Lesson2-c", perfect_quiz2, text_index_quiz2,
                                           num_texts_to_display_quiz2)

            elif current_page == "Lesson3-a":
                handle_page_transition("Lesson3-b", "Pre-Quiz2", "Lesson3-a")
            elif current_page == "Lesson3-b":
                handle_page_transition("Lesson3-c", "Lesson3-a", "Lesson3-b")
            elif current_page == "Lesson3-c":
                handle_page_transition("Lesson3-d", "Lesson3-b", "Lesson3-c")
            elif current_page == "Lesson3-d":
                handle_page_transition("Lesson3-e", "Lesson3-c", "Lesson3-d")
            elif current_page == "Lesson3-e":
                handle_page_transition("Pre-Quiz3", "Lesson3-d", "Lesson3-e")
            elif current_page == "Pre-Quiz3":
                text_index_quiz3 = text_management(text_index_quiz3, num_texts_to_display_quiz3)
                handle_pre_quiz_transition(current_page, "Ending-Screen", "Lesson3-e", perfect_quiz3, text_index_quiz3,
                                           num_texts_to_display_quiz3)
            elif current_page == "Ending-Screen":
                if back_button_x <= mouse_x <= back_button_x + 150 and back_button_y <= mouse_y <= back_button_y + 70:
                    current_page = "Pre-Quiz3"

    # Handle content based on the current page
    if current_page == "main":
        screen.blit(background_image, (0, 0))
        if volume_muted:
            screen.blit(mute_button_image, (volume_buttons_x, volume_buttons_y))
        else:
            screen.blit(volume_on, (volume_buttons_x, volume_buttons_y))
        screen.blit(volume_down, (volume_buttons_x + 48, volume_buttons_y))
        screen.blit(volume_up, (volume_buttons_x + 85, volume_buttons_y))
        if start_button_flag:
            screen.blit(start_button_image, (start_button_x, start_button_y))
        screen.blit(title_image, (title_image_x, title_image_y))
        screen.blit(pirate_image, (pirate_image_x, pirate_image_y))
        draw_speech_bubble(texts_to_display, pirate_image_x, pirate_image_y, text_index_main, num_texts_to_display)

    elif current_page == "Lesson1-a":
        # content
        render_lesson_page(background1_image, "Lesson 1.1: Continents")

    elif current_page == "Lesson1-b":
        render_lesson_page(background3_image, "Lesson 1.2: Continents")

    elif current_page == "Lesson1-c":
        render_lesson_page(background2_image, "Lesson 1.3: Continents")

    elif current_page == "Lesson1-d":
        render_lesson_page(photo_bg1, "Lesson 1.4: Continents")

    elif current_page == "Pre-Quiz1":
        # content
        render_pre_quiz_page(texts_to_display_quiz1, "Lesson 1: Quiz", perfect_quiz1, text_index_quiz1,
                             num_texts_to_display_quiz1)

    elif current_page == "Quiz1":
        render_quiz_page("q1.py", "Pre-Quiz1", "1")

    elif current_page == "Lesson2-a":
        render_lesson_page(background4_image, "Lesson 2.1: Oceans")

    elif current_page == "Lesson2-b":
        render_lesson_page(background5_image, "Lesson 2.2: Oceans")

    elif current_page == "Lesson2-c":
        render_lesson_page(photo_bg2, "Lesson 2.3: Oceans")

    elif current_page == "Pre-Quiz2":
        # content
        render_pre_quiz_page(texts_to_display_quiz2, "Lesson 2: Quiz", perfect_quiz2, text_index_quiz2,
                             num_texts_to_display_quiz2)

    elif current_page == "Quiz2":
        render_quiz_page("q2.py", "Pre-Quiz2", "2")

    elif current_page == "Lesson3-a":
        render_lesson_page(background6_image, "Lesson 3.1: Climates")

    elif current_page == "Lesson3-b":
        render_lesson_page(background7_image, "Lesson 3.2: Climates")

    elif current_page == "Lesson3-c":
        render_lesson_page(background8_image, "Lesson 3.3: Climates")

    elif current_page == "Lesson3-d":
        render_lesson_page(photo_bg3, "Lesson 3.4: Climates")

    elif current_page == "Lesson3-e":
        render_lesson_page(photo_bg4, "Lesson 3.5: Climates")

    elif current_page == "Pre-Quiz3":
        # content
        render_pre_quiz_page(texts_to_display_quiz3, "Lesson 3: Quiz", perfect_quiz3, text_index_quiz3,
                             num_texts_to_display_quiz3)

    elif current_page == "Quiz3":
        render_quiz_page("q3.py", "Pre-Quiz3", "3")

    elif current_page == "Ending-Screen":
        screen.blit(ending_bg, (0, 0))
        screen.blit(pirate_image, (pirate1_image_x, pirate1_image_y))
        if volume_muted:
            screen.blit(mute_button_image, (volume_buttons_x, volume_buttons_y))
        else:
            screen.blit(volume_on, (volume_buttons_x, volume_buttons_y))
        screen.blit(volume_down, (volume_buttons_x + 48, volume_buttons_y))
        screen.blit(volume_up, (volume_buttons_x + 85, volume_buttons_y))
        screen.blit(back_button_image, (back_button_x, back_button_y))
        screen.blit(prize1, (prize1_x, prize1_y))
        screen.blit(prize2, (prize2_x, prize2_y))
        screen.blit(prize3, (prize3_x, prize3_y))
        draw_speech_bubble(texts_ending, pirate1_image_x, pirate1_image_y, 0, 1)
        end_screen_info()

    pygame.display.flip()

# Quit Pygame
pygame.mixer.music.stop()
pygame.quit()
sys.exit(0)
