# Yu WU 
# V00917423
# 12/3/2018



import random

class Player:
	
	
	# Initializes the data attributes self.__name and self.__symbol, both should be empty strings. It also initializes the attribute self.__position to 1.

    def __init__(self):
        self.__name = " "
        self.__symbol = " "
        self.position = 1
        
	# Changes the attribute self.__name to the parameter passed as name	
    def set_name(self,name):
        self.__name = name
     
	# Changes the attribute self.__symbol to a random character in the range ‘a’ to ‘z’ (inclusive of both ‘a’ and ‘z’). 	
    def set_symbol(self):
        
        str1 = "abcdefghijklmnopqrstuvwxyz"
        
        randomletter = random.randint(0,25)
        self.__symbol=str1[randomletter]
    
	
	# returns the current value of the self.__name attribute
    def get_name(self):
        return self.__name
    
	# returns the current value of the self.__symbol attribute
    def get_symbol(self):
        return self.__symbol
	
	# Changes the attribute self.__position to the parameter passed as position
    def set_position(self,position):
        self.__position = position
    

    # returns the current value of the self.__position attribute
    def get_position(self):
        return self.__position
    
	# returns a string that contains the current value of each of the three attributes
	
    def __str__(self):
        # value of self.__name (value of self.__symbol): self.__position
        st = self.__name + " "+"(" + self.__symbol + ")" + ":" +" "+ str(self.__position)
        
        return st