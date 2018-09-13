def countvowels(text):
    vowels=("a, e, i, o, u")
    new=""
    x=set(text)
    dup=len(text)-len(x)
    for x in vowels:
     if x in text:
        new+=str(x)
    return(new,dup)
y=input("Enter a word:")
print(countvowels(y))




