from room import Room
from enemy import Enemy
from friend import Friend

def main():
    # Creating rooms
    kitchen = Room("kitchen")
    kitchen.set_description("A dank and dirty room buzzing with flies")

    ballroom = Room("ballroom")
    ballroom.set_description("A vast room with shiny wooden floor. huge candlesticks guard the entrance")

    dininghall = Room("dining hall")
    dininghall.set_description("A large room with ornate golden decorations on each wall")
    
    # Linking rooms
    kitchen.link_room(dininghall,"south")
    ballroom.link_room(dininghall, "east")
    dininghall.link_room(kitchen,"north")
    dininghall.link_room(ballroom,"west")

    # Create character
    dave = Enemy("Dave", "A zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("cheese")

    elizabeth = Friend("Elizabeth", "A skeleton")
    elizabeth.set_conversation("Hihihi")
    
    # Add char to the room
    dininghall.set_character(dave)

    current_room = kitchen
    dead = False
    while not dead:
        print("\n")
        current_room.get_details()

        inhabitant = current_room.get_character()
        if inhabitant is not None:
            inhabitant.describe()

        command = input("> ")
        if command == "exit":
            break
        elif command in ["north", "south", "east", "west"]:
            current_room = move_room(current_room, command)
        elif command == "talk":
            talk(inhabitant)
        elif command == "fight":
            dead = fight(current_room, inhabitant)
        elif command == "hug":
            hug(inhabitant)

def move_room(current_room, direction):
    return current_room.move(direction)

def talk(inhabitant):
    if inhabitant is not None:
        inhabitant.talk()
    else:
        print("There is nobody to talk")

def fight(current_room, inhabitant):
    dead = False
    if inhabitant is not None:
        if isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if inhabitant.fight(fight_with):
                print("Hooray, you won the fight!")
                current_room.set_character(None)
            else:
                print("Oh dear, you lost the fight.")
                print("That's the end of the game")
                dead = True
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

if __name__ == "__main__":
    main()