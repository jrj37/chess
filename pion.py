from piece import Piece 

class Pion(Piece):
    def __init__(self,x,y,color):
        super().__init__("Pion",x,y,color,figure="♙" if color=="white" else "♟")
    
    def mouvement_haut(self):
        super().set_y(self._Piece__y+1)
        return True
    
    def mouvement_bas(self):
        super().set_y(self._Piece__y-1)
        return True
        
    def mouvement_droite(self):
        super().set_x(self._Piece__x+1)
        return True
        
    def mouvement_gauche(self):
        super().set_x(self._Piece__x-1)
        return True
    
    def move(self,x,y):
        if self._Piece__color=="white":
            print(self._Piece__color)
            if x==self._Piece__x-1 and y==self._Piece__y:
                self.mouvement_haut()
                return True
            else:
                return False
        else:
            if x==self._Piece__x+1 and y==self._Piece__y:
                self.mouvement_bas()
                return True
            else:
                return False
              
    def __str__(self):
        return super().__str__()  
      
      
