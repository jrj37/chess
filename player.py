from echiquier import *

def notation_to_coordinates(move):
    # Vérifie que le mouvement est valide
    if len(move) != 4 or not move[0].isalpha() or not move[2].isalpha() or not move[1].isdigit() or not move[3].isdigit():
        print("Mouvement invalide")
        return player()

    # Convertir la première et la deuxième lettre en indices de colonne (0-7)
    start_col = ord(move[0]) - ord('a')
    end_col = ord(move[2]) - ord('a')

    # Convertir le premier et le deuxième chiffre en indices de rangée (0-7)
    start_row = 8 - int(move[1])
    end_row = 8 - int(move[3])

    return (start_row, start_col), (end_row, end_col)

def check_color(start,color,echiquier):
    if (echiquier.piece(start[0],start[1]).color!=color):
        print("Mouvement invalide")
        return player(color)
    
def player(color):
    move= input("Enter your move: ")
    start,end =notation_to_coordinates(move)
    echiquier=Echiquier()
    
    echiquier.update_echiquier(start,end)
    echiquier.afficher_echiquier()
    print("done")
    return start,end

class Player:
    def __init__(self,color,echiquier) -> None:
        self.__color=color
        self.__echiquier=echiquier
        self.__start=None
        
    def play(self):
        move= input("Enter your move: ")
        start,end =notation_to_coordinates(move)
        self.__start=start
        self.check_piece()
        self.check_color()
        self.__echiquier.update_echiquier(start,end)
        self.__echiquier.afficher_echiquier()
        print("done")
    
    def check_color(self):
        if (self.__echiquier.piece[self.__start[0],self.__start[1]].color!=self.__color):
            print("Mouvement invalide")
            return player(self.__color)
        
    def check_piece(self):
        if self.__echiquier.piece[self.__start[0],self.__start[1]] is None:
            print("Ce n'est pas ton tour")
            return player(self.__color)
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def set_color(self,color):
        self.__color=color
       
    @property 
    def echiquier(self):
        return self.__echiquier
    
    @echiquier.setter
    def set_echiquier(self,echiquier):
        self.__echiquier=echiquier
        
    @property
    def start(self):
        return self.__start
    
    @start.setter
    def set_start(self,start):
        self.__start=start