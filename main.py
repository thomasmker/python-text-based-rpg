from room import Room

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

    dininghall.get_details()

if __name__ == "__main__":
    main()