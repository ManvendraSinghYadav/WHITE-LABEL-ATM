import random

# Generate 50 users with random balances
users = []
for i in range(1, 51):
    username = f"user{i}"
    account_number = f"123456789{i:02d}"  # 10-digit account number
    balance = random.randint(0, 10000)  # Random balance between 0 and 10,000
    users.append((username, account_number, balance))

# Save to a text file
with open("user_balances.txt", "w") as file:
    file.write("Username,Account Number,Balance\n")
    for user in users:
        file.write(f"{user[0]},{user[1]},{user[2]}\n")

print("user_balances.txt file created successfully!")