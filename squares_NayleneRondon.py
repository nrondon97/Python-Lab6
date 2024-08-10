#Filename: squares_NayleneRondon.py
#Author: Naylene Rondon
#Date: 03/08/17
#Purpose: Range

#Start

#Variable
squares = []  #Empty list

#Loop
for value in range(1,11):  #Add numbers 1 - 10
    square = value**2       #Square those numbers
    squares.append(square)  #Populate the List

print(squares)          #Print it out


#Variable
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#List Functions
print(min(digits)) #Find min of the list
print(max(digits)) #Find max of the list
print(sum(digits)) #Add all values of the list together

#End
