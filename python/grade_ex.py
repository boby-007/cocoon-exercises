marks= (input("enter your marks with a coma: "))
markslist=marks.split(',')
total=0
for mark in markslist:
    total+=int(mark)

average=total/len(markslist)
if average >= 90:
    print(f"your total {total}, your average {average}, your grade is A+ ")
elif average >= 80:
    print(f"your total {total}, your average {average}, your grade is A ")
elif average >= 70:
    print(f"your total {total}, your average {average}, your grade is B+ ")
elif average >= 60:
    print(f"your total {total}, your average {average}, your grade is B ")
elif average >= 50:
    print(f"your total {total}, your average {average}, your grade is C+ ")
elif average >= 40:
    print(f"your total {total}, your average {average}, you failed")

