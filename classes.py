'''
Created on Feb 27, 2017

@author: Kasey Oglesby
                                       
'''
'''
You are standing in a room. There is one visible door to the room. You see a three-drawer dresser, a twin-sized bed, and a small window above the bed.



'''

class Scene():
    
    def __init__(self, desc, objects, states):
        self.desc = desc
        self.objects = objects
        self.states = states
        
    def changeState(self, state, newState):
        self.states[state] = newState
        
    def changeObject(self, object, objectUpdate):
        self.objects[object] = objectUpdate
        


class Player():
    def __init__(self):
        self.inv = {"journal key": False, "journal": False, "screwdriver": False, "lockbox": False, "code": False, "door key": False}
        
    def getInv(self):
        invEmpty = True
        print("You are carrying:")
        for item in self.inv:
            if self.inv[item]:
                print(item)
                invEmpty = False
        if invEmpty:
            print("nothing")
                
    def addInv(self, item):
        self.inv[item] = True
    
    def dropInv(self, item):
        self.inv[item] = False


def main():
    
    player = Player()
    
    #window
    
    bedStates = {"pillow": False, "underneath": False}
    bed = Scene("A made bed with a pillow. Nothing remarkable.")
    
    dresserObjects = {}
    dresser = Scene("A three drawer dresser")
    
    room = "You are standing in a room. There is one visible door to the room. You see a three-drawer dresser, a twin-sized bed, and a small window above the bed."
    print(room)
    
    player.getInv()
    player.addInv("journal")
    player.getInv()
    
if __name__ == '__main__':
    main()