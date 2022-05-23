list1=input("enter the list items with a coma: ").split(',')
list2=[]
for item in list1:
    if list1.index(item)%2==1:
        list2.append(item)

print(f"odd list are: {list2}")