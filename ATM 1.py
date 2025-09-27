import csv
from datetime import datetime

# File to store user data and transaction history
USER_FILE = "atm_data.csv"

# Load user data from CSV
def load_users():
    try:
        with open(USER_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

# Save user data to CSV
def save_users(users):
    with open(USER_FILE, mode="w", newline="") as file:
        fieldnames = ["Username", "Password", "Balance", "Transactions"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

# Add a new transaction to the user's history
def add_transaction(user, transaction_type, amount, recipient=None):
    now = datetime.now()
    transaction_time = now.strftime("%d/%m/%Y %H:%M:%S")
    transaction = {
        "Type": transaction_type,
        "Amount": amount,
        "Recipient": recipient,
        "Time": transaction_time
    }
    if "Transactions" not in user:
        user["Transactions"] = []
    user["Transactions"].append(transaction)

# Display transaction history
def show_history(user):
    if "Transactions" not in user or not user["Transactions"]:
        print("No transactions found.")
    else:
        print("\nTransaction History:")
        for transaction in user["Transactions"]:
            print(f"{transaction['Time']} - {transaction['Type']} of ₹{transaction['Amount']} "
                  f"{'to ' + transaction['Recipient'] if transaction['Recipient'] else ''}")

# Login function
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users = load_users()
    for user in users:
        if user["Username"] == username and user["Password"] == password:
            print("\nLogin successful!")
            return user
    print("\nInvalid username or password.")
    return None

# Main ATM function
def atm():
    user = login()
    if not user:
        return

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Transaction History")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":  # Check Balance
            print(f"\nYour balance is ₹{user['Balance']}")

        elif choice == "2":  # Deposit
            amount = float(input("Enter amount to deposit: "))
            user["Balance"] = str(float(user["Balance"]) + amount)
            add_transaction(user, "Deposit", amount)
            print(f"\n₹{amount} deposited successfully.")

        elif choice == "3":  # Withdraw
            amount = float(input("Enter amount to withdraw: "))
            if float(user["Balance"]) >= amount:
                user["Balance"] = str(float(user["Balance"]) - amount)
                add_transaction(user, "Withdraw", amount)
                print(f"\n₹{amount} withdrawn successfully.")
            else:
                print("\nInsufficient balance.")

        elif choice == "4":  # Transfer
            recipient = input("Enter recipient's username: ")
            amount = float(input("Enter amount to transfer: "))
            users = load_users()
            recipient_user = next((u for u in users if u["Username"] == recipient), None)
            if recipient_user:
                if float(user["Balance"]) >= amount:
                    user["Balance"] = str(float(user["Balance"]) - amount)
                    recipient_user["Balance"] = str(float(recipient_user["Balance"]) + amount)
                    add_transaction(user, "Transfer", amount, recipient)
                    add_transaction(recipient_user, "Received", amount, user["Username"])
                    save_users(users)
                    print(f"\n₹{amount} transferred to {recipient}.")
                else:
                    print("\nInsufficient balance.")
            else:
                print("\nRecipient not found.")

        elif choice == "5":  # View Transaction History
            show_history(user)

        elif choice == "6":  # Exit
            users = load_users()
            for u in users:
                if u["Username"] == user["Username"]:
                    u.update(user)
                    break
            save_users(users)
            print("\nThank you for using the ATM. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please try again.")

# Run the ATM program
if __name__ == "__main__":
    atm()