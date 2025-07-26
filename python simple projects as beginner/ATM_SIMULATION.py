balance = 100000
while True:

    print("Options:-\n 1.Check Balance\n 2.Deposit amount\n 3.Withdraw amount\n 4.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print(f"Your balance is ${balance}")
    
    elif choice == 2:
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
        print(f"${deposit} amount is added to your balance , Now your balance is ${balance}")
    
    elif choice == 3:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw < balance:
            balance -= withdraw
            print(f"your withdraw ${withdraw} from your balance , Now your balance is ${balance} ")
        else:
            print("Insufficiant amount")
    
    elif choice == 4:
        print("Exicting....")
        break
    
    else:
        print("Invalid option.")