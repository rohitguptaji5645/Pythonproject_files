Balance = 100000
pin = 9999
chances = 3

# PIN verification 
while chances > 0:
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == pin:
        print("PIN verified successfully")
        break
    else:
        chances -= 1
        print("Wrong PIN!")
        if chances > 0:
            print(f"Attempts left: {chances}")

# If all attempts are used
if chances == 0:
    print("Your card is blocked.")
else:
    # ATM menu
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit ATM")

        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            print("Your current balance is:", Balance)

        elif choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            Balance += deposit
            print("Updated balance:", Balance)

        elif choice == 3:
            withdraw = int(input("Enter amount to withdraw: "))
            if withdraw <= Balance:
                Balance -= withdraw
                print("Withdrawal successful")
                print("Remaining balance:", Balance)
            else:
                print("Insufficient balance")

        elif choice == 4:
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm your PIN: "))
            if new_pin == confirm_pin:
                pin = new_pin
                print("PIN has been changed successfully")
            else:
                print("PIN change failed! Pins do not match")

        elif choice == 5:
            print("Thank you for using District Bank ATM")
            break

        else:
            print("Invalid choice, try again.")