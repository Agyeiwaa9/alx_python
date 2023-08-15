def raise_exception_msg(message=""):
from main_0 import raise_exception_msg
    class Main:
        def __init__(self, message):
            self.message = message
        
        def __repr__(self):
            return self.message
    
    if __name__ == "__main__":
        raise Main(message)

try:
    raise_exception_msg("C is fun")
except Main as m:
    result = m

print(result)

