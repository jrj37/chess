from piece import Piece 

class Fou(Piece):
    def __init__(self,x,y,color):
        super().__init__("Fou",x,y,color,figure="♗" if color=="white" else "♝")
    
    def mouvement_haut(self):
        super().set_y(self.__y+1)
        return True
    
    def mouvement_bas(self):
        super().set_y(self.__y-1)
        return True
        
    def mouvement_droite(self):
        super().set_x(self.__x+1)
        return True
        
    def mouvement_gauche(self):
        super().set_x(self.__x-1)
        return True
        
    def __str__(self):
        return super().__str__()