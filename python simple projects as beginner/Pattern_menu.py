
while True:
    print("Choose Patterns:- ")
    print("1.Square")
    print("2.Right Triangle")
    print("3.Pyramid")
    print("4.Daimond")
    print("5.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("The Pattern ")
        n=4
        for i in range(n):
            for j in range(n):
                print("*",end=" ")
            print()

    elif choice == 2:
        print("The Pattern ")
        n=5
        for i in range(n):
            for j in range(i+1):
                print("*",end=" ")
            print()

    elif choice == 3:
       print("The Pattern ")
       n=6
       for i in range(n):
           for j in range(i,n):
               print(" ",end=" ")
           for j in range(i):
               print("*" , end=" ")
           for j in range(i+1):
               print("*", end=" ")
           print()

    elif choice == 4:
        n=5
        for i in range(n-1):
            for j in range(i,n):
                print(" ",end=" ")
            for j in range(i):
                print("*" , end=" ")
            for j in range(i+1):
                print("*", end=" ")
            print()  
        for i in range(n):
            for j in range(i+1):
                print(" ",end=" ")
            for j in range(i,n-1):
                print("*",end=" ")
            for j in range(i,n):
                print("*",end=" ")
            print()


    elif choice == 5:
        print("exicting....")
        break

    else:
        print("Invalid choice")

