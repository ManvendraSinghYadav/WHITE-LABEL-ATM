import os
from PIL import Image, ImageTk
import tkinter as tk

def display_atm_image():
    # Display ATM interface
    window = tk.Tk()
    window.title("Your Bank ATM")

    # Load ATM image
    img_path = "atm img.jpeg"  # Path to your image file
    image = Image.open(img_path)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=photo)
    label.pack()

    # Button to start Screen 1
    btn = tk.Button(window, text="Proceed to Login", command=lambda: [window.destroy(), open_screen1()])
    btn.pack()

    window.mainloop()

def open_screen1():
    os.system("python screen1.py")  # Runs screen1.py

if __name__ == "__main__":
    display_atm_image()
