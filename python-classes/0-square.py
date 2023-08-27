class Square:
    def __init__(self, size):
        self.__size = size
    
    @property
    def dict_(self):
        
mysquare = Square(3)
print(type(mysquare))

