#CSC 110 201809 Assignment 4
# YU WU  V00917423
# 11/8/2018


# Function that returns a 2-dimensional list: the sum of one + theOther
def addMatrix(one, theOther):
    addMatrix = []
    list1 = []
    for x in range(len(one)):
        for y in range(len((one)[x])):
            sum1 = one[x][y]+theOther[x][y]
            list1.append(sum1)

    n1 = 0
    for x in range(len(one)):
        addMatrix.extend([list1[n1:n1+len(one[0])]])
        n1 = n1+len(one[0])
    return addMatrix




def subtractMatrix(one, theOther):
# Functions that returns a 2-dimensional list: the difference: one - theOther
    subMatrix = []
    list1 = []
    for x in range(len(one)):
        for y in range(len((one)[x])):
            sub1 = one[x][y]-theOther[x][y]
            list1.append(sub1)

    n1 = 0
    for x in range(len(one)):
        subMatrix.extend([list1[n1:n1+len(one[0])]])
        n1 = n1+len(one[0])
    return subMatrix


def scalarMultiply(scalar, matrix):
#Functions that returns the matrix product of (scalar value) * matrix
    mulMatrix = []
    list1 = []
    n = scalar
    for x in range(len(matrix)):
        for y in range(len((matrix)[x])):
            mul1 = n*matrix[x][y]
            list1.append(mul1)

    n1 = 0
    for x in range(len(matrix)):
        mulMatrix.extend([list1[n1:n1+len(matrix)]])
        n1 = n1+len(matrix)
    return mulMatrix
    
def dot(one, theOther):
#Functions that returns the matrix dot product: one <dot> theOther
    list1 = []
    dotMatrix = []
    for x in range(len(one)):
        for y in range((len(theOther[0]))):
            n = 0
            for m in range(len(one[x])):
                n = n + one[x][m]*theOther[m][y]
            list1.append(n)
    n1 = 0
    for x in range(len(one)):
        dotMatrix.extend([list1[n1:n1+len(theOther[0])]])
        n1 = n1+len(theOther[0])    
    return dotMatrix

def outputMatrix(name, matrix, outFileHandle):
#Functions that writes the name, an ‘=’ and a matrix to the opened file 
    outFileHandle.write(name + " = ")
    for x in matrix:
        outFileHandle.write("\t" + str(x) +"\n")
    return outFileHandle


    
def MatrixIn(list1):
# Functions that returns a 2 dimensional list that contains1 matrix’s data into a 2 dimensional list
    n1 = list1[0]
    A = []
    for x in range(list1[0]):
        A.extend([list1[n1:n1+list1[1]]])
        n1 = n1+list1[1]
    return A

def main():

	print("MATRIX ARITHMETIC")
	
	print("\nInputting Matrices A, B and D and scalar c . . . . . .")
	print(". . . . Result Written to file: MatrixResult.txt")



	# Open the file to read the data
	with open('MatrixIn.txt') as f:
		input_list = []
		for line in f:
			line = line.split() 
			if line:            
				line = [int(i) for i in line]
				input_list.append(line)
    # Call the function to create 2 dimensional list
		A = MatrixIn(input_list[0])
		B = MatrixIn(input_list[1])
		c = int(input_list[2][0])
		D = MatrixIn(input_list[3])
			
		add = addMatrix(A,B)
		sub = subtractMatrix(A,B)
		mul = scalarMultiply(c,A)
		dot1= dot(A,D)
		 

	# Output the result into the point file
		with open ("MatrixResult","a")as file_write:
			outputMatrix("A",A,file_write)
			outputMatrix("B",B,file_write)
			file_write.write("c=\t"+str(c)+"\n")
			outputMatrix("D",D,file_write)

			outputMatrix("A+B",add,file_write)
			outputMatrix("A-B",sub,file_write)
			outputMatrix("c*A",mul,file_write)            
			outputMatrix("A dot D",dot1,file_write)
				
			
# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	