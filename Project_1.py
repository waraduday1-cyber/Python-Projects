
#Q1
balance = 10000
correct_pin = "1234"
history = []

#stage 1 : Pin Check
attempts = 3
logged_in = False
while attempts>0:
    user_pin = input("Enter Pin: ")
    if user_pin == correct_pin:
        logged_in = True
        break
    attempts -= 1
    if attempts > 0:
        print(f"Wrong PIN. Attempts left: {attempts}")

if not logged_in:
    print("Card blocked.")
else:
    #Stage 2: Menu
    while True:
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        user_option = int(input("Enter Option: "))
        if user_option == 1:
            print(f"Balance: {balance}")
        elif user_option == 2:
            deposit = int(input("Enter Money: "))
            if deposit > 0:
                balance = balance + deposit
                print(f"New balance: {balance}")
                history.append(f"Deposit {deposit}")
            else:
                print("Amount Must be above 0")
        elif user_option == 3:
            withdraw = int(input("Enter Money: "))
            if withdraw>balance:
                print("Insufficient balance")
            elif withdraw <= 0:
                print("Amount must be above 0")
            else:   
                print(f"New balance: {balance-withdraw}")
                balance = balance - withdraw
                history.append(f"Withdraw {withdraw}")
        elif user_option == 4:
            print("Thank you!")
            for item in history:
                print(item)
            break
        else:
            print("Invalid Input, please enter correct input")
