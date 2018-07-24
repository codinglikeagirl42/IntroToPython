import time
from sys import exit
import classes

def action(choiceList):
    choice = ''
    i = 0
    valid = False
    while valid == False:
        choice = input("What do you choose? type " + str(choiceList))
        print(choice, i)
        if choice in choiceList or i > 10:
            valid = True
        i += 1
    if i >= 9 or choice == '':
        print("You are too bad at typing to play this game.")
        exit()
    return choice

def goHome():
    print("You look around. You've done that before.")
    time.sleep(1)
    print("Here are your options:")
    print("Look by the bed | Look in the dresser | Look at the window | Check out the door")
    choiceList = ['bed', 'dresser', 'window', 'door']
    choice = action(choiceList)
    if choice == 'bed':
        goBed()
    elif choice == 'dresser':
        goDresser()
    elif choice == 'window':
        goWindow()
    elif choice == 'door':
        goDoor()
    else:
        print("You broke it!")
        goHome()

def goBed():
    print("You see a halfheartedly made bed.")
    time.sleep(1)
    print("Here are your options:")
    print("Look under the bed | Look under the pillow | Look on the night stand")
    choiceList = ['underbed', 'pillow', 'stand', 'back up']
    choice = action(choiceList)
    if choice == 'underbed':
        goUnderbed()
    elif choice == 'pillow':
        goPillow()
    elif choice == 'stand':
        goStand()
    elif choice == 'back up':
        goHome()
    else:
        print("You broke it!")
        goBed()

def goUnderbed():
    print("You see a monster-shaped indent in the carpet.")
    time.sleep(1)
    goBed()

def goPillow():
    print("You see a key and the bottom of a pillow.")
    time.sleep(1)
    print("Here are your options:")
    print("Take the key")
    choiceList = ['take', 'back up']
    choice = action(choiceList)
    if choice == 'take':
        print("You took the key! I bet there is a lock out there waiting for it!")
        goBed()
    elif choice == 'back up':
        goBed()
    else:
        print("You broke it!")
        goPillow()

def goStand():
    print("You see a glass of water.")
    time.sleep(1)
    print("Here are your options:")
    print("Drink the water | Don't drink the water")
    choiceList = ['drink', 'back up']
    choice = action(choiceList)
    if choice == 'drink':
        print("The water has been sitting here for a while. Are you sure?")
        choiceList = ['yes', 'no']
        choice = action(choiceList)
        if choice == 'yes':
            print("You drank the water. You have died of dysentery.")
        elif choice == 'no':
            goStand()
        else:
            print("You broke it!")
            goStand()
    elif choice == 'back up':
        goBed()
    else:
        print("You broke it!")
        goStand()



def goDresser():
        print("You see dresser from IKEA.")
        time.sleep(1)
        print("Here are your options:")
        print("Look on top | Look in the upper drawer | Look in the bottom drawer")
        choiceList = ['top', 'upper', 'bottom', 'back up']
        choice = action(choiceList)
        if choice == 'top':
            goTopDresser()
        elif choice == 'upper':
            goUpDrawer()
        elif choice == 'bottom':
            goBotDrawer()
        elif choice == 'back up':
            goHome()
        else:
            print("You broke it!")
            goDresser()

def goTopDresser():
        print("You see a few weeks worth of dust buildup and a journal.")
        time.sleep(1)
        print("Here are your options:")
        print("Take journal")
        choiceList = ['take', 'back up']
        choice = action(choiceList)
        if choice == 'take':
            print("You took the journal, but it has a lock on it!")
            goDresser()
        elif choice == 'back up':
            goDresser()
        else:
            print("You broke it!")
            goTopDresser()

def goUpDrawer():
    goDresser()

def goBotDrawer():
    goDresser()

def goWindow():
    print("You see a window with a tree on the other side.")
    time.sleep(1)
    print("Here are your options:")
    print("Look through the window | Try to open the window")
    choiceList = ['look', 'open', 'back up']
    choice = action(choiceList)
    if choice == 'look':
        print("You see a tree.")
        time.sleep(1)
        goWindow()
    elif choice == 'open':
        print("It's stuck shut!")
        time.sleep(1)
        goWindow()
    elif choice == 'pry':
        print("The window only opened slightly, but you found a key! Totally normal hiding place.")
        time.sleep(1)
        goWindow()
    elif choice == 'break':
        print("You threw the lock box through the window.")
        time.sleep(1)
        print("You are FREEEEEEE!.. but your dad is piiiiiisssssssed....")
    elif choice == 'back up':
        goHome()
    else:
        print("You broke it!")
        goWindow()

def goDoor():
    print("You see a door. It use to be a tree.")
    time.sleep(1)
    print("Here are your options:")
    print("Try to open | Look through key slot")
    choiceList = ['open', 'look', 'back up']
    choice = action(choiceList)
    if choice == 'look':
        print("This is a new lock made since 1900. You can't see through it...")
        time.sleep(1)
        goDoor()
    elif choice == 'open':
        print("It's locked!")
        time.sleep(1)
        goDoor()
    elif choice == 'back up':
        goHome()
    else:
        print("You broke it!")
        goDoor()


def main():
    print("Escape Your Room: The Game: Exclamation Point!!")
    print("You were doing absolutely nothing. Now you are in a room with a locked door.")
    time.sleep(2)
    print("This is in build 0.0.0.0.a.dot.1, so most of the features don't work because we ran out of time.")
    time.sleep(2)
    goHome()


if __name__ == '__main__':
   main()
