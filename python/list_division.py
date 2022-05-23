numbers=input("enter your numbers with acomma : ").split(',')

new_list=[int(i) for i in numbers]

divisible_list=[]

for number in new_list:
    if number%5==0:
        divisible_list.append(number)
    

print(divisible_list)