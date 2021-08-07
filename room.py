class Room():

    number_of_rooms = 0

    def __init__(self, room_name) -> None:
        self.__name = room_name
        self._description = None
        self.linked_rooms = {}
        self._character = None
        self._item = None
        Room.number_of_rooms += 1
    
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value    

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, value):
        self._character = value
    
    @property
    def item(self):
        return self._item
        
    @item.setter
    def item(self,value):
        self._item = value

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def describe(self):
        print(self._description)

    def get_details(self):
        print(self.__name)
        print("-"*60)
        print(self._description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")
    
    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self
    