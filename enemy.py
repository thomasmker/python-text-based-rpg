from character import Character

class Enemy(Character):
    def __init__(self, char_name, char_description) -> None:
        super().__init__(char_name, char_description)
        self._weakness = None
    
    @property
    def weakness(self):
        return self._weakness
    
    @weakness.setter
    def weakness(self, weakness):
        self._weakness = weakness

    def fight(self, combat_item):
        if combat_item == self._weakness:
            print(f"You fend {self._name} off with the {combat_item}")
            return True
        else:
            print(f"{self._name} crushes you, puny adventurer")
            return False