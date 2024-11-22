import sys

# Initialize default user details
user_pin = "1234"
user_balance = 5000.0
transaction_history = []

# Function to validate PIN
def validate_pin():
    for _ in range(3):
        pin = input("Enter your 4-digit PIN: ")
        if pin == user_pin:
            return True
        else:
            print("Incorrect PIN. Try again.")
    print("Too many incorrect attempts. Exiting.")
    sys.exit()

# Function for withdrawing money
def withdraw_money():
    global user_balance
    try:
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > 0:
            if amount <= user_balance:
                user_balance -= amount
                transaction_history.append(f"Withdrawn: ${amount:.2f}")
                print(f"Withdrawal successful! Remaining balance: ${user_balance:.2f}")
            else:
                print("Insufficient balance.")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Function for depositing money
def deposit_money():
    global user_balance
    try:
        amount = float(input("Enter the amount to deposit: $"))
        if amount > 0:
            user_balance += amount
            transaction_history.append(f"Deposited: ${amount:.2f}")
            print(f"Deposit successful! Updated balance: ${user_balance:.2f}")
        else:
            print("Amount must be greater than zero.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Function for changing the ATM PIN
def change_pin():
    global user_pin
    current_pin = input("Enter current PIN: ")
    if current_pin == user_pin:
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            user_pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Invalid PIN format. Must be 4 digits.")
    else:
        print("Incorrect current PIN.")

# Function to check balance
def check_balance():
    print(f"Your current balance is: ${user_balance:.2f}")

# Function to print receipt
def print_receipt():
    print("\n--- Receipt ---")
    for transaction in transaction_history:
        print(transaction)
    print(f"Final Balance: ${user_balance:.2f}")
    print("Thank you for using our ATM!\n")

# Main ATM menu
def atm_menu():
    while True:
        print("\n1. Withdraw Money")
        print("2. Deposit Money")
        print("3. Change ATM PIN")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            withdraw_money()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            change_pin()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            print_receipt()
            print("Exiting. Thank you!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

# Validate PIN before showing the menu
if validate_pin():
    atm_menu()
