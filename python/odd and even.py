odd=0
even=0
for i in range(15,36):
    if i%2==0:
        even+=i
    else:
        odd+=i

print(odd)
print(even)