#CSC 110 201809 Assignment 5
# YU WU
# V00917423
# 22/11/2018
import re


# A function that count the total word numbers in file.
def wordTotal(wordlist):
    # Input: a 1 dimensional list of words
    # Returns: an integer, the number of words
    num = 0
    for x in wordlist:
        num += 1
    return num

# A function that count each word numbers in file.    
def wordFrequency(wordlist):
    # Input: a 1 dimensional list of words
    # Returns: a dictionary with key = word (string)
    # and value = number of occurrences
    wordlist = sorted(wordlist,key = str.lower)
    wordfrequency = {}
    for word in wordlist:
        keys = wordfrequency.keys()
        if word in keys:
            wordfrequency[word] += 1
        else:
            wordfrequency[word] = 1
    return wordfrequency

# A function that count the total upper and lower letter numbers in file.
def letterCount(wordlist):
    # Input: a 1 dimensional list of words
    # Returns: two integers: count of lower case letters
    # and count of upper case letters
    upper = 0
    lower = 0
    for word in wordlist:
        for letter in word:
            if letter.isupper():
                upper += 1
            if letter.islower():
                lower += 1

    return upper,lower
    
# A function that count each upper and lower letter numbers in file.    
def letterFrequency(wordlist):
    # Input: a 1 dimensional list of words
    # Returns: a dictionary with key = alpha-numeric
    # letters and value = number of occurrences
    wordlist.sort()
    letterfrequency= {}
    for word in wordlist:
        for letter in word:
            keys = letterfrequency.keys()
            if letter in keys:
                letterfrequency[letter] += 1
            else:
                letterfrequency[letter] = 1
    letterfrequency = sorted(letterfrequency.items())
    letterfrequency = dict(letterfrequency)

    return letterfrequency

    
    
    
def main():
	# Open the file and output the 1 dimensional list.
    with open ("storyIn.txt")as f:
        inputlist = []
        for x in re.split(r'[^A-Za-z0-9]', f.read()):
            if x:
                inputlist.append(x)
	# Call the function to get the results
    num = wordTotal(inputlist)
    wordfreq = wordFrequency(inputlist)
    upper,lower = letterCount(inputlist)
    letterfreq = letterFrequency(inputlist)
	
	
	# Write the resule into the file.
    with open ("analysisOut.txt","w")as w:
        w.write("Word:" + str(num)+"\n")
        for x,y in sorted(wordfreq.items()):
            w.write("{}: {}\n".format(x,y))
        w.write("Upper Case Letters:" + str(upper))
        w.write("\nLower Case Letters:" + str(lower)+"\n") 
        for x,y in sorted(letterfreq.items()):
            w.write("{}: {}\n".format(x,y))

# Do not change *anything* below this line
if __name__ == "__main__":
	main()
	