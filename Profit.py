actual_cost= float(input("Please enter the actual amount: "))
sales_cost = float(input("Please enter the sales amount: "))

if(sales_cost > actual_cost):
    amount = sales_cost - actual_cost
    print(amount)
else:
    print("No Profit")
