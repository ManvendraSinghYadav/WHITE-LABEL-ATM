from tkinter import *
from tkinter import messagebox, ttk
from datetime import datetime
import subprocess
from PIL import Image, ImageTk
import pygame
import os
import sys

# Initialize pygame mixer with robust error handling
try:
    pygame.mixer.init()
    sound_initialized = True
    print("Sound system initialized successfully")
except Exception as e:
    print(f"Could not initialize sound system: {e}")
    sound_initialized = False

# Function to read user credentials from atm.txt
def read_user_credentials(file_path):
    users = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                if "username:" in line and "password:" in line:
                    parts = line.strip().split()
                    username = parts[1]
                    password = parts[3]
                    users.append((username, password))
    except FileNotFoundError:
        messagebox.showerror("Error", "User credentials file not found!")
    return users

# Function to play sound on keypress with multiple fallback options
def play_sound(event=None):
    if not sound_initialized:
        return
        
    # Define possible sound file names and locations
    sound_files = [
        "atm_press_sound.mp3",  # Current directory
        "atm press sound.mp3",  # Current directory (original name)
        "sounds/atm_press_sound.mp3",  # Sounds subdirectory
        os.path.join(os.path.dirname(__file__), "atm_press_sound.mp3"),  # Script directory
        r"C:\Users\user\Desktop\atm pro\atm press sound.mp3"  # Absolute path
    ]
    
    for sound_file in sound_files:
        try:
            if os.path.exists(sound_file):
                print(f"Attempting to load sound from: {sound_file}")
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                print("Sound played successfully")
                return
        except Exception as e:
            print(f"Error with sound file {sound_file}: {e}")
    
    print("Sound file not found in any of these locations:")
    for sf in sound_files:
        print(f"- {sf} (exists: {os.path.exists(sf) if isinstance(sf, str) else 'N/A'})")

# Create the main window
window = Tk()
window.title('User Login')
window.geometry('600x600')
window.configure(bg="#2E86C1")  # Modern blue background

# Set the ATM image as background with error handling
try:
    img_files = [
        "atm_img.jpg",
        "atm_img.jpeg",
        "atm.jpg",
        os.path.join(os.path.dirname(__file__), "atm_img.jpg"),
        r"C:\Users\user\Desktop\atm pro\atm img.jpeg"
    ]
    
    bg_image = None
    for img_file in img_files:
        try:
            if os.path.exists(img_file):
                bg_image = Image.open(img_file)
                break
        except Exception as e:
            print(f"Error loading image {img_file}: {e}")
    
    if bg_image:
        bg_photo = ImageTk.PhotoImage(bg_image.resize((650, 650)))
        bg_label = Label(window, image=bg_photo)
        bg_label.place(relwidth=1, relheight=1)
    else:
        raise FileNotFoundError("No suitable background image found")
except Exception as e:
    print(f"Background image error: {e}")
    bg_label = Label(window, text="ATM Background Image", font=("Arial", 20), bg="#2E86C1", fg="white")
    bg_label.place(relwidth=1, relheight=1)

# Styles for modern look
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10, foreground='white', background='blue')
style.configure('TLabel', font=('Helvetica', 12), foreground='white', background='DarkGrey')
style.configure('TEntry', font=('Helvetica', 12), padding=5)
style.configure('TCheckbutton', font=('Helvetica', 10), foreground='white', background='DarkGrey')

# Date and time
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")

# Title
title_label = Label(window, text="Secure ATM Login", font=("Arial", 20, "bold"), bg="DarkGrey", fg="white")
title_label.place(x=180, y=50)

# Username and password fields
ttk.Label(window, text='Username:', font=('Helvetica', 12), background="#2E86C1", foreground="white").place(x=150, y=200)
username_entry = ttk.Entry(window)
username_entry.place(x=250, y=200, width=200)

ttk.Label(window, text='Password:', font=('Helvetica', 12), background="#2E86C1", foreground="white").place(x=150, y=250)
password_entry = ttk.Entry(window, show='*')
password_entry.place(x=250, y=250, width=200)

# Bind keypress event to play sound
username_entry.bind("<Key>", play_sound)
password_entry.bind("<Key>", play_sound)

# Checkbox
chk = IntVar()
ttk.Checkbutton(window, text='I am not a robot', variable=chk, style='TCheckbutton').place(x=250, y=300)

# Button function
def clicked():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if not entered_username or not entered_password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    if chk.get() != 1:
        messagebox.showerror("Error", "Please confirm you are not a robot.")
        return

    users = read_user_credentials(r"C:\Users\user\Desktop\atm pro\atm.txt")

    for user in users:
        if entered_username == user[0] and entered_password == user[1]:
            success_popup = Toplevel(window)
            success_popup.title("Login Successful")
            success_popup.geometry("300x200")
            success_popup.configure(bg="lightgreen")
            ttk.Label(success_popup, text=f"Welcome {entered_username}!", font=("Helvetica", 14, "bold"), foreground="black").pack(pady=20)
            ttk.Button(success_popup, text="Proceed", command=lambda: [success_popup.destroy(), open_screen2(entered_username, entered_password)]).pack(pady=20)
            return

    messagebox.showerror("Error", "Invalid username or password.")

def open_screen2(username, password):
    try:
        subprocess.run(["python", "screen2.py", username, password])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open next screen: {e}")
    window.destroy()

# Proceed Button
proceed_btn = ttk.Button(window, text='Proceed', command=clicked)
proceed_btn.place(x=250, y=350)

# Run the main loop
window.mainloop()