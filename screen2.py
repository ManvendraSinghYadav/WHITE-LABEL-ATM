import os
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import pandas as pd
import sys
from PIL import Image, ImageTk
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Get username and password from screen1.py
username = sys.argv[1]
password = sys.argv[2]

# Create the main window
window = Tk()
window.title('PROCEED YOUR TRANSACTION SAFELY')
window.geometry('800x600')
window.configure(bg="#2E86C1")  # Modern blue background

# Set up background image
try:
    bg_image = Image.open("atm img.jpeg")  # Path to your image
    bg_photo = ImageTk.PhotoImage(bg_image.resize((800, 600)))
    bg_label = Label(window, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
except Exception:
    bg_label = Label(window, text="ATM Background Image", font=("Arial", 20), bg="#2E86C1", fg="white")
    bg_label.place(relwidth=1, relheight=1)

# Date and time
now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

# Styling for labels and entries
label_font = ("Helvetica", 14, "bold")
entry_font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")
entry_bg = "#ffffff"
entry_border = "#cccccc"
button_bg = "#1ABC9C"  # Modern green color
button_fg = "#ffffff"

# Tabs for SBI, ICICI, Cash Withdrawal, and Balance Inquiry
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control, style="TFrame")
tab2 = ttk.Frame(tab_control, style="TFrame")
tab3 = ttk.Frame(tab_control, style="TFrame")
tab4 = ttk.Frame(tab_control, style="TFrame")
tab_control.add(tab1, text='SBI')
tab_control.add(tab2, text='ICICI')
tab_control.add(tab3, text='Cash Withdrawal')
tab_control.add(tab4, text='Balance Inquiry')
tab_control.pack(expand=1, fill='both')

# Function to read user balances from user_balances.txt
def read_user_balances():
    users = []
    try:
        with open("user_balances.txt", "r") as file:
            next(file)  # Skip header
            for line in file:
                username, account_number, balance = line.strip().split(',')
                users.append((username, account_number, float(balance)))  # Convert to float
    except FileNotFoundError:
        messagebox.showerror("Error", "User balances file not found!")
    return users

# Function to update user balances in user_balances.txt
def update_user_balance(account_number, new_balance):
    users = read_user_balances()
    updated_users = []
    for user in users:
        if user[1] == account_number:
            updated_users.append((user[0], user[1], float(new_balance)))  # Ensure float
        else:
            updated_users.append(user)
    with open("user_balances.txt", "w") as file:
        file.write("Username,Account Number,Balance\n")
        for user in updated_users:
            file.write(f"{user[0]},{user[1]},{user[2]}\n")

# Function to play cash sound
def play_cash_sound():
    # List of possible sound file locations (relative and absolute paths)
    possible_sound_files = [
        "cash_sound.mp3",                     # Current directory
        "cash sound.mp3",                      # Current directory (original name)
        os.path.join("sounds", "cash_sound.mp3"),  # Sounds subdirectory
        os.path.join(os.path.dirname(__file__), "cash_sound.mp3"),  # Script directory
        r"C:\Users\user\Desktop\atm pro\cash sound.mp3"  # Original absolute path
    ]
    
    for sound_file in possible_sound_files:
        try:
            if os.path.exists(sound_file):
                print(f"Attempting to play sound from: {sound_file}")  # Debug message
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                return  # Exit if successful
            else:
                print(f"Sound file not found at: {sound_file}")  # Debug message
        except Exception as e:
            print(f"Error playing sound from {sound_file}: {e}")
    
    print("Cash sound file not found in any of these locations:")
    for path in possible_sound_files:
        print(f"- {path}")# Function to handle cash withdrawal
def withdraw_cash():
    account_number = account_entry.get()
    amount = amount_entry.get()

    if not account_number or not amount:
        messagebox.showerror("Error", "Please enter both account number and amount.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric amount.")
        return

    users = read_user_balances()
    for user in users:
        if user[1] == account_number:
            if user[2] >= amount:
                new_balance = user[2] - amount
                update_user_balance(account_number, new_balance)
                play_cash_sound()  # Play cash sound
                messagebox.showinfo("Success", f"Withdrawal successful!\nNew Balance: ₹{new_balance:.2f}")
                return
            else:
                messagebox.showerror("Error", "Insufficient balance in your account.")
                return
    messagebox.showerror("Error", "Account number not found.")

# Cash Withdrawal Tab
Label(tab3, text='Account Number:', font=label_font, bg="#2E86C1", fg="white").grid(row=0, column=0, pady=10, padx=20)
account_entry = Entry(tab3, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
account_entry.grid(row=0, column=1, pady=10, padx=10)

Label(tab3, text='Amount:', font=label_font, bg="#2E86C1", fg="white").grid(row=1, column=0, pady=10, padx=20)
amount_entry = Entry(tab3, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
amount_entry.grid(row=1, column=1, pady=10, padx=10)

Button(tab3, text='Withdraw Cash', command=withdraw_cash, bg=button_bg, fg=button_fg, font=button_font).grid(
    row=2, column=1, pady=20
)

# Function to display balance
def display_balance():
    account_number = balance_account_entry.get()
    users = read_user_balances()
    for user in users:
        if user[1] == account_number:
            messagebox.showinfo("Balance", f"Your current balance is ₹{user[2]:.2f}")
            return
    messagebox.showerror("Error", "Account number not found.")

# Balance Inquiry Tab
Label(tab4, text='Account Number:', font=label_font, bg="#2E86C1", fg="white").grid(row=0, column=0, pady=10, padx=20)
balance_account_entry = Entry(tab4, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
balance_account_entry.grid(row=0, column=1, pady=10, padx=10)

Button(tab4, text='Check Balance', command=display_balance, bg=button_bg, fg=button_fg, font=button_font).grid(
    row=1, column=1, pady=20
)

# Function to save transaction history
def save_transaction(bank_name, username, password, account_no, to_account_no, amount, deducted_amount):
    # Define the file path
    file_path = "user_transaction_history.xlsx"

    # Create a dictionary with the transaction data
    transaction_data = {
        "Bank Name": [bank_name],
        "User Name": [username],
        "Password": [password],
        "Account No.": [account_no],
        "To (Account No.)": [to_account_no],
        "Time": [datetime.now().strftime("%H:%M:%S")],
        "Amount": [amount],
        "Deducted Amount": [deducted_amount]
    }

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(transaction_data)

    # Check if the file exists
    if not os.path.exists(file_path):
        # Create a new file with headers
        df.to_excel(file_path, index=False)
    else:
        try:
            # Read the existing file
            existing_df = pd.read_excel(file_path)
            # Append the new transaction data
            updated_df = pd.concat([existing_df, df], ignore_index=True)
            # Save the updated DataFrame to the Excel file
            updated_df.to_excel(file_path, index=False)
        except PermissionError:
            messagebox.showerror("Error", "Permission denied. Please close the file and try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to complete transaction
def complete_transaction(bank_name, account_entry, to_account_entry, amount_entry):
    try:
        amount = float(amount_entry.get())
    except ValueError:
        messagebox.showerror('Error', 'Please enter a valid numeric amount.', icon='error')
        return

    # Check if amount exceeds ₹20,000
    if amount > 20000:
        deducted_amount = round(amount * 0.05, 2)  # 5% deducted amount
        actual_amount = amount - deducted_amount  # Actual amount transferred
        proceed = messagebox.askyesno(
            'Transaction Limit Exceeded',
            f'Transaction amount exceeds ₹20,000.\nA deduction of 5% (₹{deducted_amount:.2f}) will be applied.\nActual Amount Transferred: ₹{actual_amount:.2f}\nDo you want to proceed?',
        )
        if not proceed:
            return
    else:
        deducted_amount = 0  # No deduction
        actual_amount = amount  # Full amount transferred

    # Validate all fields
    if account_entry.get() and to_account_entry.get() and amount_entry.get():
        messagebox.showinfo(
            'Transaction Successful!',
            f'Your transaction of ₹{amount:.2f} has been successfully completed!\nDeducted Amount: ₹{deducted_amount:.2f}\nActual Amount Transferred: ₹{actual_amount:.2f}',
            icon='info',
        )
        save_transaction(bank_name, username, password, account_entry.get(), to_account_entry.get(), amount, deducted_amount)
    else:
        messagebox.showerror(
            'Error',
            'All fields are required to complete the transaction.',
            icon='error',
        )

# SBI Tab
Label(tab1, text='Account No.:', font=label_font, bg="#2E86C1", fg="white").grid(row=0, column=0, pady=10, padx=20)
account_entry_sbi = Entry(tab1, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
account_entry_sbi.grid(row=0, column=1, pady=10, padx=10)

Label(tab1, text='To (Account No.):', font=label_font, bg="#2E86C1", fg="white").grid(row=1, column=0, pady=10, padx=20)
to_account_entry_sbi = Entry(tab1, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
to_account_entry_sbi.grid(row=1, column=1, pady=10, padx=10)

Label(tab1, text='Amount:', font=label_font, bg="#2E86C1", fg="white").grid(row=2, column=0, pady=10, padx=20)
amount_entry_sbi = Entry(tab1, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
amount_entry_sbi.grid(row=2, column=1, pady=10, padx=10)

Button(tab1, text='Complete Transaction', command=lambda: complete_transaction("SBI", account_entry_sbi, to_account_entry_sbi, amount_entry_sbi), bg=button_bg, fg=button_fg, font=button_font).grid(
    row=3, column=1, pady=20
)

# ICICI Tab
Label(tab2, text='Account No.:', font=label_font, bg="#2E86C1", fg="white").grid(row=0, column=0, pady=10, padx=20)
account_entry_icici = Entry(tab2, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
account_entry_icici.grid(row=0, column=1, pady=10, padx=10)

Label(tab2, text='To (Account No.):', font=label_font, bg="#2E86C1", fg="white").grid(row=1, column=0, pady=10, padx=20)
to_account_entry_icici = Entry(tab2, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
to_account_entry_icici.grid(row=1, column=1, pady=10, padx=10)

Label(tab2, text='Amount:', font=label_font, bg="#2E86C1", fg="white").grid(row=2, column=0, pady=10, padx=20)
amount_entry_icici = Entry(tab2, bg=entry_bg, highlightbackground=entry_border, highlightthickness=1, font=entry_font)
amount_entry_icici.grid(row=2, column=1, pady=10, padx=10)

Button(tab2, text='Complete Transaction', command=lambda: complete_transaction("ICICI", account_entry_icici, to_account_entry_icici, amount_entry_icici), bg=button_bg, fg=button_fg, font=button_font).grid(
    row=3, column=1, pady=20
)

# Run main loop
window.mainloop()