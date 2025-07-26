while True:
    print("choose:-\n1.sum(+)\n2.product(*)3.divide(/)\n4.subtract(-)\n5.Exit")
    choice = input("enter your choice: ")

    if choice == "5":
        print("Exiting....")
        break


    
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

    if choice == "+":
        result = num1+num2
    
    elif choice == "*":
        result = num1*num2
    
    elif choice == "/":
        result = num1/num2
    
    elif choice == "-":
        result = num1-num2
    
    
    else:
        print("invalid input!!, Please try again.")

    print("result:- ", result)