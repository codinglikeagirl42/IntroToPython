from random import randint


t = ["Rock", "Paper", "Scissors","Lizard", "Spock", "Spiderman", "Batman", "Wizard", "Glock"]


computer = t[randint(0,8)]


player = False

while player == False:
#set player to True
    player = raw_input("Rock, Paper, Scissors, Lizard, Spock, Spiderman, Batman, Wizard, Glock! ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        if computer == "Spock":
            print("You lose!", computer, "vaporizes", player)
        if computer == "Batman":
            print("You lose...", computer, "explodes", player)
        if computer == "Glock":
            print("You lose...", computer, "breaks", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        if computer == "Lizard":
            print("You lose!", computer, "eats", player)
        if computer == "Spiderman":
            print("You lose...", computer, "rips", player)
        if computer == "Wizard":
            print("You lose...", computer, "burns", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        if computer == "Spock":
            print("You lose...", computer, "vaporizes", player)
        if computer == "Batman":
            print("You lose...", computer, "dismantles", player)
        if computer == "Glock":
            print("You lose...", computer, "dents", player)
        else:
            print("You win!", player, "cut", computer)
    elif player == "Lizard":
        if computer == "Rock":
            print("You lose...", computer, "crushes", player)
        if computer == "Scissors":
            print("You lose...", computer, "decapitates", player)
        if computer == "Wizard":
            print("You lose...", computer, "transforms", player)
        if computer == "Spiderman":
            print("You lose...", computer, "defeats", player)
        else:
            print("You win!", player, "poisons", computer)
    elif player == "Spock":
        if computer == "Paper":
            print("You lose...", computer, "disproves", player)
        if computer == "Lizard":
            print("You lose...", computer, "poisons", player)
        if computer == "Batman":
            print("You lose...", computer, "hangs", player)
        if computer == "Glock":
            print("You lose...", computer, "shoots", player)
        else:
            ("You win!", player, "vaporizes", computer)
    elif player == "Spiderman":
        if computer == "Batman":
            print("You lose...", computer, "scares", player)
        if computer == "Spock":
            print("You lose...", computer, "befuddles", player)
        if computer == "Rock":
            print("You lose...", computer, "knocks out", player)
        if computer == "Scissors":
            print("You lose...", computer, "cut", player)
        else:
            print("You win!", player, "defeats", computer)
    elif player == "Batman":
        if computer == "Wizard":
            print("You lose...", computer, "stuns", player)
        if computer == "Lizard":
            print("You lose...", computer, "confuses", player)
        if computer == "Glock":
            print("You lose...", computer, "kills", player)
        if computer == "Paper":
            print("You lose...", computer, "delays", player)
        else:
            print("You win!", player, "defeats", computer)
    elif player == "Wizard":
        if computer == "Spock":
            print("You lose...", computer, "zaps", player)
        if computer == "Rock":
            print("You lose...", computer, "interrupts", player)
        if computer == "Scissors":
            print("You lose...", computer, "cut", player)
        if computer == "Spiderman":
            print("You lose...", computer, "annoys", player)
        else:
            print("You win!", player, "burns", computer)
    elif player == "Glock":
        if computer == "Spiderman":
            print("You lose...", computer, "disarms", player)
        if computer == "Paper":
            print("You lose...", computer, "jams", player)
        if computer == "Lizard":
            print("You lose...", computer, "is too small for", player)
        if computer == "Wizard":
            print("You lose...", computer, "melts", player)
        else:
            print("You win!", player, "shoots", computer)
            
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,8)]
