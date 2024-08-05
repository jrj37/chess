import numpy as np 
from piece import PieceAccessor
from roi import Roi
from pion import Pion
from tour import Tour 
from cavalier import Cavalier
from fou import Fou
from reine import Reine

class Echiquier:
    def __init__(self)->None:
        self.__board = self.fill_echiquier()
        self.__piece=None
        self.__start=None
        self.__end=None
    
    @property
    def board(self):
        return self.__board

    def fill_pawn(self,color):
        if color.endswith("white"):
            L=[Pion(6,i,"white") for i in range(8)]
        else:
            L=[Pion(1,i,"black") for i in range(8)]
        pawns=np.array(L)
        return pawns
        
    def fill_rook(self,color):
        if color.endswith("white"):
            L=[Tour(7,0,"white"),Tour(7,7,"white")]
        else:
            L=[Tour(0,0,"black"),Tour(0,7,"black")]
        rooks=np.array(L)
        return rooks

    def fill_knight(self,color):
        if color.endswith("white"):
            L=[Cavalier(7,1,"white"),Cavalier(7,6,"white")]
        else:
            L=[Cavalier(0,1,"black"),Cavalier(0,6,"black")]
        knights=np.array(L)
        return knights

    def fill_bishop(self,color):
        if color.endswith("white"):
            L=[Fou(7,2,"white"),Fou(7,5,"white")]
        else:
            L=[Fou(0,2,"black"),Fou(0,5,"black")]
        bishops=np.array(L)
        return bishops

    def fill_queen(self,color):
        if color.endswith("white"):
            L=[Reine(7,3,"white")]
        else:
            L=[Reine(0,3,"black")]
        queens=np.array(L)
        return queens

    def fill_king(self,color):
        if color.endswith("white"):
            L=[Roi(7,4,"white")]
        else:
            L=[Roi(0,4,"black")]
        kings=np.array(L)
        return kings

    def fill_pieces(self,color):
        pawns=self.fill_pawn(color)
        rooks=self.fill_rook(color)
        knights=self.fill_knight(color)
        bishops=self.fill_bishop(color)
        queens=self.fill_queen(color)
        kings=self.fill_king(color)
        pieces=np.concatenate((pawns,rooks,knights,bishops,queens,kings))
        return pieces

    def fill_board(self):
        white=self.fill_pieces("white")
        black=self.fill_pieces("black")
        board=np.concatenate((white,black))
        return board

    def print_board(self):
        for piece in self.board:
            print(piece)

    def afficher_echiquier(self):
        # Définir les dimensions de l'échiquier
        taille = 8

        # Définir les caractères pour les bordures et les cases
        case_blanche = '   '
        case_noire = '###'
        bordure_horizontale = '+' + ('---+' * taille)

        for i in range(taille):
            print(bordure_horizontale)
            ligne = ''
            for j in range(taille):
                if self.board and self.board[i][j] is not None:
                    ligne += '| ' + self.board[i][j].figure + ' '
                else:
                    if (i + j) % 2 == 0:
                        ligne += '|' + case_blanche
                    else:
                        ligne += '|' + case_noire
            ligne += '|'
            print(ligne)
        print(bordure_horizontale)


    def fill_echiquier(self):
        echiquier = [[None for _ in range(8)] for _ in range(8)]
        board=self.fill_board()
        for piece in board:
            echiquier[piece.x][piece.y]=piece
        
        return echiquier
      
    def check_move(self):
        self.__piece=self.__board[self.__start[0]][self.__start[1]]
        if not self.__piece.move(self.__end[0],self.__end[1]) and self.__piece is None:
            return False
        else:
            return True
        
    def update_echiquier(self,start,end):
        self.__start,self.__end=start,end
        
        if self.check_move():
            self.__piece.move(self.__end[0],self.__end[1])
            self.__board[self.__end[0]][self.__end[1]]=self.__piece
            self.__board[self.__start[0]][self.__start[1]]=None
                    
        return self.board
        
    @property   
    def piece(self):
        return PieceAccessor(self.__board)
