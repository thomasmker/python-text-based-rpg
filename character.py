class Character():
    def __init__(self, char_name, char_description) -> None:
        self.name = char_name
        self.description = char_description
        self.conversation = None
    
    def describe(self):
        print(f"{self.name} is here!\n{self.description}")

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print("{self.name} doesn't want to tal to you")
    
    def fight(self):
        print(f"{self.name} doesn't want to fight with you")
        return True