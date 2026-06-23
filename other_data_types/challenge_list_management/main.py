#list of deli items
meat = ["Ham", "3.99", "50", "Sliced"]
cheese = ["Cheddar", "5.49", "100", "Sharp"]
condiment = ["Mustard", "1.99", "75", "Spicy"]
#combine into one main list
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
#restock item

#add seasonal meat
seasonal_meat = ["Turkey", "4.50", "100", "Sliced"]
#append deli_dept to seasonal_meat
seasonal_meat.append(deli_dept)
#remove condiment from deli_dept
deli_dept.remove(condiment)
#sort deli_dept
deli_dept.sort()
print("Updated Deli List:", deli_dept)