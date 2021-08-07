class Item():
    def __init__(self, item_name, item_description) -> None:
        self._name = item_name
        self._description =  item_description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
    
    def describe(self):
        print("Item:")
        print("The [" + self._name + "] is here - " + self._description)