class RPGInfo():
    author = "Anonymous"

    def __init__(self, game_title) -> None:
        self.title = game_title

    def welcome(self):
        castle = """
                 |~  _
            [_]--'--[_]
            |'|""`""|'|
            | | /^\ | |
            |_|_|I|_|_|
        """
        print(castle)
        print(f"Welcome to {self.title}")
        input("Press any key to continue.")

    @staticmethod
    def info():
        print("Made using the OOP RPG game creator (c) me")

    @classmethod
    def credits(cls):
        print("Thank you for playing")
        print(f"Created by " + cls.author)