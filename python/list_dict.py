
list_1=input("enter your 1st list with a comma :").split(',')


list_2=input("enter your 2nd list with a comma :").split(',')

dict={}
i=0

for n in list_1:
    dict[n]=list_2[i]
    i+=1

print(dict)
