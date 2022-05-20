
def case_calc(word):
    upper=0
    lower=0
    for i in word:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
        else:
            print("wrong input")
    print(upper)
    print(lower)
case_calc("Boby")
