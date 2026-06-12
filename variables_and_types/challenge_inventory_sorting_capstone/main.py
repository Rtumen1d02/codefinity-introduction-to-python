# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

#slice the items string to extract
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:27]
#slice categories string to extract
category1 = categories[0:11]
category2 = categories[13:24]
#Price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "5.40"
#Print names, prices and categories
print("We have", candy1, "for", bubblegum_price, "in the", category1)
print("We have", candy2, "for", chocolate_price, "in the", category1)
print("We have", dry_goods, "for", pasta_price, "in the", category2)
