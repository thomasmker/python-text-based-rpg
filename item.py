class Item():
    def __init__(self, item_name) -> None:
        self.name = item_name
        self.description =  None

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description