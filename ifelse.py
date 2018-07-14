myfavoriteicecream = raw_input("What is you favorite icecream?")
if myfavoriteicecream == "Honey Lavendar":
    print("That is my favorite too!")
    
elif myfavoriteicecream in["vanilla", "blackberry", "watermelon sherbert"]:
    print("I like that flavor too :)")
    
else:
    print("yuck, you have horrible taste")
    
myname = raw_input("What is your name")
myinfo = ["Angela","Fred","Trudy", "Kris", "Mark" ]
myinfo.append(myname)
for name in myinfo:
    if name == "Trudy":
        print("Hello")
        if name != "Fred":
            print("You are not Fred")
        else:
            print("Hello Fred")
    else:
        print("Go Away")
        
x = int(raw_input("please imput a whole number:"))
if x > 0:
    print(x)
else:
    print(-x)