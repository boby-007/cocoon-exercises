sentence=input("enter a sentence: ").split(' ')
word= input("enter the word you want ")

def delete_word(word1,sentence1):
    if word1 in sentence1:
        sentence1.remove(word1)
        new_sent=" "
        for n in sentence1:
            new_sent+=n+" "
        print(new_sent)
    else:
        print(f"{word1} not in the sentence..please recheck")

delete_word(word,sentence)