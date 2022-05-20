import random


word=input("enter your word:" )
wordlist=list(word)
num=len(wordlist)
anagram=[]
start=True
new_word=''
while start:
    random_num=random.randint(0,(num-1))
    new_word+=str(word[random_num])

    if len(new_word)>=num:
        anagram.append(new_word)
        new_word=''
        
        if len(anagram)>=20:
            start=False
    
print(anagram)   




