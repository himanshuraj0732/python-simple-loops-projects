while True:
    print("!! Welcome To Python Quiz !!")
    start = input("Do you want to start (yes/no): ").lower()
    score = 0

    if start != "yes":
        print("Okay, have a great day :)")
        break
    else:
        print("\nLet's start The Quiz!\n")

    answer = input("What RAM stands for?: ")
    if answer.lower() == "random access memory":
        print("Correct :)")
        score += 1
    else:
        print("Wrong!")

    answer2 = input("What ROM stands for?: ")
    if answer2.lower() == "read only memory":
        print("Correct :)")
        score += 1
    else:
        print("Wrong!")

    answer3 = input("What CPU stands for?: ")
    if answer3.lower() == "central processing unit":
        print("Correct :)")
        score += 1
    else:
        print("Wrong!")

    print(f"\nYour final score is: {score} out of 3")

    if score == 3:
        print("Excellent! 🎉")
    elif score >= 2:
        print("Good job!")
    else:
        print("Keep practicing!")

    print("\n----------------------------------\n")
