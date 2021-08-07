from room import Room
from enemy import Enemy
from friend import Friend
from item import Item
import random

class Game():
    def __init__(self) -> None:
        pass

    @staticmethod
    def start():
        rooms = create_rooms()        
        characters = create_characters()    
        items = create_item()
    
        add_character_to_room(rooms, characters)
        add_item_to_room(rooms, items)
        
        # Random start room
        current_room = random.choice(rooms)
        backpack = []

        dead = False
        while not dead:
            print("\n")
            current_room.get_details()

            inhabitant = current_room.character

            item = current_room.item

            command = input("> ")
            if command == "exit":
                break
            elif command in ["north", "south", "east", "west"]:
                current_room = move_room(current_room, command)
            elif command == "talk":
                talk(inhabitant)
            elif command == "fight":
                dead = fight(current_room, inhabitant, backpack)
            elif command == "hug":
                hug(inhabitant)
            elif command == "take":
                take(current_room, item, backpack)                    
            else:
                print("Invalid command. The list of commands are: exit, talk, fight, hug, take, north, south, east, west")

def create_rooms():
    """ Method to create the rooms/map """
    rooms = []

    kitchen = Room("kitchen")
    kitchen.description = "A dank and dirty room buzzing with flies"
    
    ballroom = Room("ballroom")
    ballroom.description = "A vast room with shiny wooden floor. huge candlesticks guard the entrance"

    dininghall = Room("dining hall")
    dininghall.description = "A large room with ornate golden decorations on each wall"

    # Linking rooms
    kitchen.link_room(dininghall,"south")
    ballroom.link_room(dininghall, "east")
    dininghall.link_room(kitchen,"north")
    dininghall.link_room(ballroom,"west")

    rooms.append(kitchen)
    rooms.append(ballroom)
    rooms.append(dininghall)

    # print("There are " + str(Room.number_of_rooms) + " rooms to explore.")
    return rooms

def create_characters():
    """ Method to create enemies and friends """
    characters = []

    dave = Enemy("Dave", "A hungry zombie")
    dave.conversation = "Brrlgrh... rgrhl... brains..."
    dave.weakness = "cheese"
    characters.append(dave)

    joe = Enemy("Joe", "A dirty werewolf")
    joe.conversation = "woof woof"
    joe.weakness = "soap"
    characters.append(joe)

    elizabeth = Friend("Elizabeth", "A skeleton")
    elizabeth.conversation = "Hihihi"
    characters.append(elizabeth)

    return characters

def create_item():
    """ Method to create items """
    items = []
    items.append(Item("cheese", "A large and smelly block of cheese"))
    items.append(Item("book", "A really good book entitled 'Knitting for dummies'"))
    items.append(Item("soap", "A sulfur soap"))

    return items

def add_character_to_room(rooms, characters):
    random.shuffle(characters)
    for i in range(len(rooms)):
        rooms[i].character = characters[i]

def add_item_to_room(rooms, items):
    random.shuffle(items)
    for i in range(len(rooms)):
        rooms[i].item = items[i]

def move_room(current_room, direction):
    return current_room.move(direction)

def talk(inhabitant):
    if inhabitant is not None:
        inhabitant.talk()
    else:
        print("There is nobody to talk")

def fight(current_room, inhabitant, backpack):
    dead = False
    if inhabitant is not None:
        if isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with):
                    print("Hooray, you won the fight!")
                    current_room.character = None
                else:
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            inhabitant.fight()
    else:
        print("There is nobody to fight")
    return dead

def hug(inhabitant):
    if inhabitant is not None:
        if isinstance(inhabitant, Enemy):
            print("I wouldn't do that if I were you...")
        else:
            inhabitant.hug()
    else:
        print("There is nobody to hug")

def take(current_room, item, backpack):
    if item is not None:
        print("You put the " + item.name + " in your backpack")
        backpack.append(item.name)
        current_room.item = None
    else:
        print("Nothing to take")