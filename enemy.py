from character import Character

class Enemy(Character):
    def __init__(self, char_name, char_description) -> None:
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer")
            return False