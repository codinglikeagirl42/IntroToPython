import random
print "Welcome to Rock, Paper, Scissors, Lizard, Spok"
userpick = raw_input("Pick one: Rock, Paper, Scissors, Lizard, or Spok")
computerpick = random.choice(["Rock","Paper", "Scissors", "Lizard", "Spok"])
print (userpick)
print (computerpick)
if userpick == "Rock" and computerpick == "Scissors":
    print "You Win!"
elif userpick == "Rock" and computerpick == "Paper":
    print "Sorry, You Lose!"
elif userpick == "Rock" and computerpick == "Rock":
    print "You Tied!"
elif userpick == "Rock" and computerpick == "Spok":
    print "Sorry, You Lose!"
elif userpick == "Rock" and computerpick == "Lizard":
    print "You Win!"
elif userpick ==  "Paper" and computerpick == "Paper":
    print "You Tied!"
elif userpick == "Paper" and computerpick == "Rock":
    print "You Win!"
elif userpick == "Paper" and computerpick == "Scissors":
    print "Sorry, You Lose!"
elif userpick == "Paper" and computerpick == "Spok":
    print "You Win!"
elif userpick == "Paper" and computerpick == "Lizard":
    print "Sorry, You Lose!"
elif userpick == "Scissors" and computerpick == "Scissors":
    print "You Tied"
elif userpick == "Scissors" and computerpick == "Paper":
    print "You Win!"
elif userpick == "Scissors" and computerpick == "Rock" :
    print "Sorry, You Lose!"
elif userpick == "Scissors" and computerpick == "Spok":
    print "Sorry, You Lose!"
elif userpick == "Scissors" and computerpick == "Lizard":
    print "You Win!"
elif userpick == "Spok" and computerpick == "Rock":
    print "You Win!"
elif userpick == "Spok" and computerpick == "Paper":
    print "Sorry, You Lose!"
elif userpick == "Spok" and computerpick == "Scissors":
    print "You Win!"
elif userpick == "Spok" and computerpick == "Spok":
    print "You Tied"
elif userpick == "Spok" and computerpick == "Lizard":
    print "Sorry, You Lose!"
elif userpick == "Lizard" and computerpick == "Rock":
    print "Sorry, You Lose!"
elif userpick == "Lizard" and computerpick == "Scissors":
    print "Sorry, You Lose!"
elif userpick == "Lizard" and computerpick == "Paper":
    print "You Win!"
elif userpick == "Lizard" and computerpick == "Spok":
    print "You Win!"
elif userpick == "Lizard" and computerpick == "Lizard":
    print "You Tied!"
else :
    print "Try Again"