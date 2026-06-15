# The item's discount and stock status have been defined
discounted = False
lowStock = True

#boolean variable
movingProduct = discounted or lowStock
print(movingProduct)

promotion = not discounted and not lowStock
print(promotion)

print("Is the item eligible for promotion?", promotion)