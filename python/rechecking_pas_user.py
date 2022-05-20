name=input("enter your username: ")
password=input("enter your password: ")

name1=input("enter your username again: ")
password1=input("enter your password again: ")

def checker (var_n,var_n1,var_p,var_p1):
    if var_n==var_n1 and var_p==var_p1:
        print("acess granted")
    else:
        print("wrong username or password")

checker(name,name1,password,password1)