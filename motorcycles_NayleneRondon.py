#Filename: motorcycles_NayleneRondon.py
#Author: Naylene Rondon
#Date: 03/06/17
#Purpose: Modifying lists

#Start

#Standard
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#Change A Value
motorcycles[0] = "ducati"
print(motorcycles)

#Add an item to list
motorcycles.append("ducati")
print(motorcycles)

#Insert an item to a specific position
motorcycles.insert(0, "harley")
print(motorcycles)

#Removing an Item using delete
del motorcycles[-1]
print(motorcycles)

#Removing an Item using POP
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Removing using POP, specific values
first_owned = motorcycles.pop(0)
print("The first motorcycle that I owned was a " + first_owned.title() + ".")

#Remove an item by value
motorcycles.remove("yamaha")
print(motorcycles)

#Resetted The List
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

#Remove an item by value using variables
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#End
