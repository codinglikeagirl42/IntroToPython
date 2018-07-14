#create a program that will read the users fortune
#six options
ans1 = "You're a coding RockStar!!"
ans2 = "Consider eating more fortune cookies ;-)"
ans3 = "Help I'm traped in a fortune cookie factory"
ans4 = "Haven't you had enough cookies?"
ans5 = "COOOOKKKIEEE!"
ans6 = "You Have tamed the mighty Python, now you must free it onto the Great Spider's Web!"

ans = raw_input("Would you like to know your fortune? Y or N")
if ans == "Y":
    choice = raw_input("Pick a number between 1-6")
    if choice == 1:
        print(ans1)
    elif choice == 2:
        print(ans2)
    elif choice == 3:
        print(ans3)
    elif choice == 4:
        print(ans4)
    elif choice == 5:
        print(ans5)
    elif choice == 6:
        print(ans6)
else:
    print("You're loss")
    





