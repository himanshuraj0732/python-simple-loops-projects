import random

score = 0

while True:
    print("Welcome to Rock Paper Scissor Game !!")
    choice = input("Do you want to play this game (yes/no): ").lower()

    if choice == "yes":
        print("Let's start the game!")
    elif choice == "no":
        print("Ok bye!")
        break
    
    
    your_move = input("Enter your move: ").lower()
    
    if your_move not in ["rock", "paper", "scissor"]:
        print("Invalid move! Please type rock, paper, or scissor.")
        continue

    bot = random.choice(["rock", "scissor", "paper"]).lower() 
    

    if your_move == bot:
        print("It's a tie!")

    elif your_move == "rock":
        if bot == "scissor":
            print("You win!")
            score +=1
        else:
            print("You lose!")

    elif your_move == "paper":
        if bot == "rock":
            print("You win!")
            score +=1
        else:
            print("You lose!")

    elif your_move == "scissor":
        if bot == "paper":
            print("You win!")
            score +=1
        else:
            print("You lose!")
   

    print(f"your score is : {score}")
print(f"your final score is : {score}")
    