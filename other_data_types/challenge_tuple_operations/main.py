# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#Count how many times apples appear in the shelf tuple & store in apple count
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

#Find the index of the first occurrence of bananas is the shelf
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)

#Check if the number of apples is less than 5 - <5 print restocked else print Apples are sufficiently stokced
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
    
#Count how many times grapes appear in the shelf tuple. If once print restocked
grapes_count = shelf.count("grapes")
#print("Number of Gapes:", grapes_count)
if grapes_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

#Check oranges exist in the shelf and print Index
#orange_index = shelf.index("oranges")
#print("Oranges are at index:", orange_index)
#orange_count = shelf.count("oranges")
#print("Number of Oranges", orange_count)
#if orange_count < 1:
 #   print("Oranges are out of stock.")

#OTHER OPTION
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock.")
    