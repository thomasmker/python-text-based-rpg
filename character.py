class Character():
    def __init__(self, char_name, char_description) -> None:
        self._name = char_name
        self._description = char_description
        self._conversation = None
    
    @property
    def conversation(self):
        return self._conversation

    @conversation.setter
    def conversation(self, conversation):
        self._conversation = conversation

    def describe(self):
        print("Monster:")
        print(f"{self._name} is here! {self._description}")
    
    def talk(self):
        if self._conversation is not None:
            print(f"[{self._name} says]: {self._conversation}")
        else:
            print("{self.name} doesn't want to tal to you")
    
    def fight(self):
        print(f"{self._name} doesn't want to fight with you")
        return True