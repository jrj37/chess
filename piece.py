class Piece:
    def __init__(self,type,x,y,color,figure):
        self.__type=type
        self.__x=x
        self.__y=y
        self.__color=color
        self.__figure=figure
        
    def __str__(self) -> str:
        return self.__type+ f"\nx: {self.__x} \ny: {self.__y}"
      
    @property 
    def color(self):
        return self.__color
     
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def set_type(self,type):
        self.__type=type 
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y    
     
    @property	
    def position(self):
        return (self.__x,self.__y)
        
    def set_x(self,x):
        self.__x=x
        
    def set_y(self,y):
        self.__y=y
        
    @property
    def figure(self):
        return self.__figure
    
    @figure.setter
    def set_figure(self,figure):
        self.__figure=figure
        
    def move(self,x,y):
        self.set_x(x)
        self.set_y(y)
        
    def update_position(self,position):
        self.move(position[0],position[1])
        
        
class PieceAccessor:
        def __init__(self, board):
            self.__board = board

        def __getitem__(self, pos):
            x, y = pos
            return self.__board[x][y]

        def __setitem__(self, pos, value):
            x, y = pos
            self.__board[x][y] = value
        
        