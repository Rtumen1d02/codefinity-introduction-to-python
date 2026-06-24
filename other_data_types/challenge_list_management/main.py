#list of deli items
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
#combine into one main list
deli_dept = [meat, cheese, condiment]
print("Initial Deli List:", deli_dept)
#restock item
if meat[0] == "Ham": 
    if meat[2] < 100:
        meat[2] = 100
        print("Restock its quantity to 100")
    else:
        meat[2] = 100
        print("Restocked to 100")
#meat.remove("50")
#meat.append("100")
#add seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
#append deli_dept to seasonal_meat
deli_dept.append(seasonal_meat)
#remove condiment from deli_dept
deli_dept.remove(condiment)
#sort deli_dept
deli_dept.sort()
print("Updated Deli List:", deli_dept)