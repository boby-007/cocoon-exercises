test__score=input("enter your scores with a comma : ").split(',')
score_list=[]


total=0
for score in test__score:
    num=int(score)
    score_list.append(num)
    total+=num



highest=max(score_list)

if highest>=100:
    print("a value over hundred has been entered")
else:

    lowest=min(score_list)
    print(f"highest score:{highest} , lowest score:{lowest}")
        


    average=total/len(score_list)
    print(f"your total:{total}, your average:{average}")
    list_copy=score_list.copy()

    score_list.remove(highest)
    second_highest=max(score_list)

    min1=min(list_copy)
    list_copy.remove(min1)
    min2=min(list_copy)
    list_copy.remove(min2)
    total_new=sum(list_copy)
    average_new=(total_new/len(list_copy))

    print(average_new)

