items=input("enter your items with a comma : ").split(',')
dict={}
for item in items:
    dict[item]=items.count(item)

new_value=[]

for item in dict:
    new_value.append(dict[item])

dic_new={}
new_value.sort()
old_value=new_value[-3:]
print(old_value)
for value in old_value:
    for item in dict:
        if value==dict[item]:
            dic_new[item]=value


print(dic_new)





    

