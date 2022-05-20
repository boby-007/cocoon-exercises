vowels=['a','e','i','o','u']
word=input("enter your word: ")

vowel_total=0
for i in word:
    if i in vowels:
        vowel_total+=1

print(f"no of vowels in your word is :{vowel_total}")
