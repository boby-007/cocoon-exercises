total=0


for i in range(1,21):
    if i%2==0 or i%3==0:
        continue
    else:
        print(i)
        total+=i


print(total)
        


