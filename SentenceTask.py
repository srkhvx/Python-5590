#

tense=input("Please enter a Sentence: ")
letters=0
words=1
digits=0
previous = ""
for i in tense:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1
    elif i==" ":
        if previous!=i:
            words+=1
    previous = i
print("Letters: ", letters)
print("digits: ", digits)
print("words: ", words)