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
elif userpick ==  "Paper" and computerpick == "Paper":
    print "You Tied!"
elif userpick == "Paper" and computerpick == "Rock":
    print "You Win!"
elif userpick == "Paper" and computerpick == "Scissors":
    print "Sorry, You Lose!"
elif userpick == "Scissors" and computerpick == "Scissors":
    print "You Tied"
elif userpick == "Scissors" and computerpick == "Paper":
    print "You Win!"
elif userpick == "Scissors" and computerpick == "Rock" :
    print "Sorry, You Lose!"
else :
    print "Try Again"