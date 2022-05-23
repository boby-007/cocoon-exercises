item_num=int(input("Enter the total no of items to buy: "))

if item_num>=100:
    print (f"your total: {item_num*7}$")
elif item_num>=10 and item_num<=99:
    print(f"your total: {item_num*10}$")
elif item_num<=10:
    print(f"your total: {item_num*12}$")
else:
    print("wrong input")
