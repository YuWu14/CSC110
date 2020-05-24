# Edit this file for Assignment #3
# YU WU V00917423
# 10/18/2018

   # The rectangle function display a shape of rectangle.
def rectangle(symbol, height, width):
    # Create a while loop to build a rectangle.
	while height != 0:
      
    # Print each symbol width times.    
		i = 0
		while i < width:
			print(symbol+".", end="")
			i += 1
	
		print()
		height = height - 1
        
        
    # The square function display a shape of square.    
def square(symbol, width):
    # Create a while loop to print the square.
    n = 0
    while n < width:
        print((symbol+".")*width)
        n = n + 1   

        
    # The diamond function display a shape of diamond.         
def diamond(symbol, width):
    # First check if the input width is an odd number or an even number.
    # Then print the first part of the diamond.
    if width%2 == 0:
        i = 0
        while i < width:
            print("_." * ((width-i) // 2)+(symbol+".") * (i+1))
            i = i + 2
        i =i- 2
    # Print the second part of the diamond.
        while i >= 0:
            print("_." * ((width-i) // 2)+(symbol+"." )* (i+1))
            i = i -2
            
    # If the input width is an odd number, use a different method to create an diamond.         
    else:
        i = 0
        while i < width:
            print("_." * ((width-i) // 2)+(symbol+".") * (i+1))
            i = i + 2
        i =i- 3
        while i >= 0:
            print("_." * ((width-i) // 2)+(symbol+"." )* (i))
            i = i -2

            

    # The horizline function display a shape of horizline. 
def horizLine(symbol, length):
    
    # Print the symbol length times in horizontal ways.
    print((symbol+".")*length)

# The vertline function display a shape of vertline. 
def vertLine(symbol, length):
    
    # Print the symbol length times in Vertical ways.
    n = 0
    while n < length:
        print((symbol+"."))
        n = n + 1   


    # The leftTopTriangle function display a shape of leftTopTriangle. 
def leftTopTriangle(symbol, height):
    
    #  Create the loop to reduce the print numbers of shapes each times.
    while height != 0:
        for x in range(0,height):
            print(symbol+".", end="")
        
        print()
        height = height - 1

        
    # The rightBottomTriangle function display a shape of rightBottomTriangle. 
def rightBottomTriangle(symbol, height):
    
    # Create a while loop to build a Triangle in right side.
    # Replace the space by -..
    i = 1
    while i < height:
        print("_."*(height-i)+(symbol+".")*(i))
        i = i +1
    print((symbol+".")*height)




def main(): 
	# Print what this program suppose to do
    print("I N T E G E R F I G U R E S\n")
    print("   1: Rectangle")
    print("   2: Square")
    print("   3: Diamond")
    print("   4: Horizontal Line")
    print("   5: Vertical Line")
    print("   6: Triangle (top left)")
    print("   7: Triangle (bottom right)\n")
    print("Input Line 1: 1-7 specifies shape (0 to end)")
    print("Input Line 2: Symbol (0-9)")
    print("Input Line 3: Shape size (integer)")
    print("Input Line 4 (for rectangle): Shape width (integer)\n")
    
    # Create a loop to continuou.
    while True:
    
    
    # Ask the user to input the shape, symbol, height, width.
        shape = int(input("Line 1: "))
       
    
        # If the user wants the loop to stop.
        if shape == 0:
            break
       
    
        symbol = input("Line 2: ")
        height = int(input("Line 3: "))
        
        
        # If the shape is Rectangle, then ask the user to input the width and call the rectangle function
        if shape == 1:
            width = int(input("Line 4: "))
            print()
            rectangle(symbol, height, width)
            print()


       # If the shape is Square, call the rectangle function.
        if shape == 2:
            width = height
            print()
            square(symbol, width)
            print()
    
        # If the shape is Diamond, call the diamond function.
        if shape == 3:
            width = height
            print()
            diamond(symbol, width)
            print()
        
        
        # If the shape is Horizontal Line, call the horizontal function.
        if shape == 4:
            length = height
            print()
            horizLine(symbol, length)
            print()
        
        # If the shape is Vertical Line, call the vertical function.
        if shape == 5:
            length = height
            print()
            vertLine(symbol, length)
            print()
    
        # If the shape is Triangle (top left), call the Triangle (top left) function.
        if shape == 6:
            print()
            leftTopTriangle(symbol, height)
            print()
    
        # If the shape is Triangle (bottom right), call the Triangle (bottom right) function.
        if shape == 7:
            print()
            rightBottomTriangle(symbol, height)
            print()
    

# *** Do not edit anything below this line ***
if __name__ == "__main__":
	main()