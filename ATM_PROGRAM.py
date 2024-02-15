import random

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def change_pin(self, new_pin):
        self.pin = new_pin
        return True

print("Welcome to Canara Bank!")
card_inserted = input("Please insert your card (yes/no): ")
if card_inserted.lower() == "yes":
    pin = int(input("Enter your PIN: "))
    if pin == 1234:  # Replace 1234 with the correct PIN
        print("PIN accepted. Transaction in progress.")
        acc = Account(1000)  # Starting balance of 1000, change as needed
        while True:
            print("\n1 - Balance Inquiry\n2 - Withdrawal\n3 - Deposit\n4 - PIN Change\n5 - Exit")
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("Your balance is:", acc.get_balance())
            elif choice == 2:
                amount = int(input("Enter the amount to withdraw: "))
                withdrawn_amount = acc.withdraw(amount)
                if withdrawn_amount > 0:
                    print("Please collect your cash:", withdrawn_amount)
                else:
                    print("Insufficient balance or invalid amount.")
            elif choice == 3:
                amount = int(input("Enter the amount to deposit: "))
                if acc.deposit(amount):
                    print("Deposit successful.")
                else:
                    print("Invalid amount.")
            elif choice == 4:
                new_pin = int(input("Enter your new PIN: "))
                if acc.change_pin(new_pin):
                    print("PIN changed successfully.")
                else:
                    print("Failed to change PIN. Please try again.")
            elif choice == 5:
                print("Thank you for banking with us.")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Incorrect PIN. Please try again.")
else:
    print("Card not inserted. Exiting.")
