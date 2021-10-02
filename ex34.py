# All the Code Written By Asif date 25th September 2021
# using more function and Branches
from sys import exit

def gold_room():
    print("This room is full of gold")

    choice = input("Enter: ")
    if "0" in choice or "1" in choice:
        how_much=int(choice)
    else:
        dead("MAN,learn to a number")    

    if how_much<50:
        print("nice you win")
        exit(0) 
    else:
        dead("you greedy basterd")    

def bear_room():
    print("how are you going to move bear?")     
    bear_moved = False

    while True:
        choice = input("Enter : ")
        if choice =="take honey":
            dead("the bear look at you than slaps you face off") 
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved from the door") 

            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets passed of and chew your leg off.") 
        elif choice == "open door"  and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")   

def cthuhlu_room():
    print("here you see the great evil cthulu.") 
    print("he,it,whatever at you and you go insane.")   

    choice = input("Enter: ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")   
    else:
        cthuhlu_room()

def dead(why):
    print(why,"Good job!")
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left") 
    print("which ine do you take?")


    choice = input("Enter:")

    if choice=="left":
        bear_room()
    elif choice == "right":
        cthuhlu_room() 
    else:
        dead("you stumble the room until you stravve.")    

start()                                      