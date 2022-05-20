name=input("enter your name: ")
id = input("enter your id: ")
basic_pay=int(input("enter your basic pay: "))


def net_pay_calc(hrd,da,basic_pay):
    HRA=(basic_pay*hrd)//100
    DA= (basic_pay*da)//100
    net_pay=(basic_pay+HRA+DA)
    print(f"your HRA: {HRA}, your DA: {DA}, your Net pay: {net_pay}")


if basic_pay>=10000:
    # HRA=(basic_pay*15)//100
    # DA= (basic_pay*8)//100
    # net_pay=(basic_pay+HRA+DA)
    # print(f"your HRA: {HRA},/nyour DA: {DA},/nyour Net pay: {net_pay}")
    net_pay_calc(15,8,basic_pay)
elif basic_pay>=5000 and basic_pay<=10000:
    # HRA=(basic_pay*10)//100
    # DA= (basic_pay*5)//100
    # net_pay=(basic_pay+HRA+DA)
    # print(f"your HRA: {HRA},/nyour DA: {DA},/nyour Net pay: {net_pay}")
     net_pay_calc(10,5,basic_pay)
elif basic_pay<=5000:
    # HRA=(basic_pay*5)//100
    # DA= (basic_pay*3)//100
    # net_pay=(basic_pay+HRA+DA)
    # print(f"your HRA: {HRA},/nyour DA: {DA},/nyour Net pay: {net_pay}")
     net_pay_calc(5,3,basic_pay)
else:
    print("wrong input")
