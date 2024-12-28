actual_cost = float(input("Enter the actual product price: "))

sale_cost = float(input("Enter the sale price: "))

if (sale_cost > actual_cost):
    profit = sale_cost - actual_cost
    print("You made a profit of: ", profit)

else:
    print("no profit made")