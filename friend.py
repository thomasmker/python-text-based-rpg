from character import Character

class Friend(Character):
    def __init__(self, char_name, char_description) -> None:
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        print(f"{self.name} hugs you back!")