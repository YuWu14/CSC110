import random

class Die:
  
    ThrowDice = random.randint(1,6)
	
    # Initializes the data attribute self.__faceUp
    def __init__(self):
        self.__faceUp = " "
    
	# Uses a random number generate to change the __faceUp attribute    
    def throw(self):
        self.__faceUp = Die.ThrowDice
        
	# Returns the current value of the __faceUp attribute. 	
    def get_faceUp(self):
        return self.__faceUp