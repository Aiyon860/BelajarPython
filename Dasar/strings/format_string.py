### FORMAT STRING ###

## It's illegal to put string and number type together in a variable
# price = 15_000
# customer_name = "Daniel"
# result = "Customer" + customer_name + "buy the product with price: " + price
# print(result)

## but now we can combine string and number type together with format() method
''' 
{} is to store arguments from format() method
so that, we can combine string dan number type together 
'''
# Example 1
price = 15_000
customer_name = "Daniel"
result = "Customer: " + customer_name + "\nbuy the product with price: {}"
print(result.format(price))

print('')

# Example 2
name = "Tirza"
product_name = "Parfume"
product_price = 25_000
quantity = 1
receipt = "Name: " + name + "\nProduct: " + product_name + "\nPrice: {}" + "\nQuantity: {}"
print(receipt.format(product_price, quantity))

print('')

# Example 3
# use index number such as {0} so the arguments can be placed correctly in the placeholders
name2 = "Daniel"
food_name = "Hamburger"
food_price = 15_000
quantity = 1
receipt = "Name: " + name2 + "\nProduct: " + food_name + "\nPrice: {1}" + "\nQuantity: {0}"
print(receipt.format(quantity, food_price))





