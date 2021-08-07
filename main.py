from room import Room
from character import Character

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
    dave = Character("Dave", "A zombie")
    dave.set_conversation("What's up, dude?")
    dave.describe()

    current_room = kitchen
    while True:
        print("\n")
        current_room.get_details()
        command = input("> ")
        if command == "exit":
            break
        current_room = current_room.move(command)

if __name__ == "__main__":
    main()