from echiquier import *
from player import *

def update_game():
    
    player1 =Player("white",Echiquier())
    player2 = Player("black",Echiquier())
    # Exemple d'utilisation
    while(True):
        print("Les blancs jouent")
        player1.play()
        player2.set_echiquier=player1.echiquier
        print("Les noirs jouent")
        player2.play()
        player1.set_echiquier=player2.echiquier


if __name__== "__main__":
    update_game()