import os

# Simulated database (username: password)
users = {
    "ruaa": "1234",
    "admin": "admin"
}

# File to store balance
BALANCE_FILE = "balance.txt"

# Check if balance file exists, if not create it
if not os.path.exists(BALANCE_FILE):
    with open(BALANCE_FILE, "w") as f:
        f.write("1000")

# Function to read balance from file
def read_balance():
    with open(BALANCE_FILE, "r") as f:
        return float(f.read())

# Function to write balance to file
def write_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

# Function to login user
def create_account():
        new_username = input("Enter a new username: ")
        new_password = input("Create a password: ")
        users[new_username] = new_password
        print("Account created successfully!")

def login():
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        if username_input in users and users[username_input] == password_input:
          print("✅ Login successful!")
          return True  # <-- Added return True on successful login
        else:
          print("❌ Invalid username or password.")
        return False  # <-- Added return False on failure

# Function to check balance
def check_balance():
    balance = read_balance()
    print(f"\n💰 Your current balance is: ${balance:.2f}")

# Function to withdraw
def withdraw():
    try:
        amount = float(input("Enter amount to withdraw: $"))
        balance = read_balance()
        if amount <= 0:
            print("⚠️ Enter a positive amount.")
        elif amount > balance:
            print("❌ Insufficient funds.")
        else:
            balance -= amount
            write_balance(balance)
            print(f"✅ ${amount:.2f} withdrawn successfully.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")

# Function to deposit
def deposit():
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("⚠️ Enter a positive amount.")
        else:
            balance = read_balance()
            balance += amount
            write_balance(balance)
            print(f"✅ ${amount:.2f} deposited successfully.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")

# Function to show the ATM menu
def atm_menu():
    while True:
        print("\n📋 --- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            check_balance()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            deposit()
        elif choice == '4':
            print("👋 Goodbye! Thank you for using Ruaa's ATM.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Main function
def main():
    print("🏦 Welcome to Ruaa's ATM Machine")
    if login():
        atm_menu()

# Run the program
main()
