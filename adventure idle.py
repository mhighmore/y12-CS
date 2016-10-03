#adding a pause this will allow sleep to occur
from time import sleep
import sys

# part 1 asking who the player is
hp=5 # this sets hit points
exp=0 # this sets experience points
name=input("Type in your adventurers name")
print("Welcome",name,"to the.....")# think of a name for your adventure


#adding a pause
sleep(3.0) # change the value to make the pause longer or shorter


# 2  the introduction

print("""
The floor of the cave is now mostly submerged
beneath inky black water. Your shoes give up the battle to keep the water out and you walk with a steady squelch.
""") # edit this to create an intro to your game


# choices edit this to make a choice for the player to make
print("You spot a fierce rat in the center of the tunnel")
event1 = input("Press s to sneak by. Press t to throw stone at it") 
if event1 == ("s"): # this will happen if s is pressed
    print("Carefully you edge past")
else:  # this will happen if s is not pressed
    print("You throw a stone at the rat and it runs off")

# another rat appears

# choices edit this to make a choice for the player to make
print("You spot ANOTHER VERY FIERCE rat in the center of the tunnel")
event1 = input("Press s to sneak by. Press t to throw stone at it") 
if event1 == ("s"):
    print("Carefully you edge past")
    exp=exp+2 # experience points are updated
else:
    print("You throw a stone at the rat")
    print("It attacks you")
    sleep(5.0) #pause to add tension to game
    print("After a struggle it runs off")
    exp=exp+1    # exp points updated
    hp=hp-1 # hit points decreased due to attack

#  updating the score of the game

print("You have",exp,"point")
print("You have",hp,"hit points left")

# showing what is in the players rucksack

rucksack = ["gold coin","rope","cheese roll"]

print("You have the following items in your rucksack: ")
print (rucksack)

# picking up an item

print("You spot a magical orb in the center of the tunnel")
event1 = input("Press p pick it up. Press w to walk past") 
if event1 == ("p"):
    print("magical orb now in your rucksack")
    rucksack.append("magical orb")
else:
    print("You foolishly walk past the orb")
    sleep(5.0) #pause to add tension to game

# showing the new item in the rucksack

print("You NOW have the following items in your rucksack: ")
print (rucksack) # this will show the rucksack at this stage

# choices edit this to make a choice for the player to make
print("You spot dragon in the tunnel, a magical orb will kill it")
event1 = input("Press o to use the orb, or n to not use it") 
if event1 == ("o"): # this happens if o is pressed
    if "magical orb" in rucksack: #checking that the orb is in your bag
        print("You have a magical orb, you made a good choice earlier!!")
    else:
        print("You don't have a magical orb, OOps!!")
    exp=exp+4   # exp points updated
    hp=hp+4 # hit points increased
else: # this happens if n is pressed
    print("The dragon....")
    sleep(5.0) #pause to add tension to game
    print("It attacks you")
    sleep(5.0) #pause to add tension to game
    print("After a struggle it runs off")
    exp=exp+1    # exp points updated
    hp=hp-2 # hit points decreased due to attack

#  updating the score of the game

print("You have",exp,"point")
print("You have",hp,"hit points left")

# giving more than 2 choices
print ("A giant hamster is now growling at you!!")
choice3 = input("Type a to attack, b to back away or c to creep past.") 
if choice3 == "a":
     print("You attack with your terrible sword")
     exp=exp+1    # exp points updated
     hp=hp-2 # hit points decreased due to attack
elif choice3 == "b":
     print("You back away quietly")
else:
     print("Carefully you sneak past")

#  updating the score of the game

print("You have",exp,"point")
print("You have",hp,"hit points left")

#ending the game
       
if hp <= 0:
    print("Your hero is dead")
    
else:
    print ("You are doing you have survived the terrible tunnel of doom!!!!")
  
