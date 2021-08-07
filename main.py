
from rpginfo import RPGInfo
from game import Game

def main():
    RPGInfo.info()
    spooky_castle = RPGInfo("The Spooky Castle")
    spooky_castle.welcome()
    Game.start()
    RPGInfo.credits()

if __name__ == "__main__":
    main()