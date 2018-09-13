L2=[]
L1=[]
def fizzbuzz():
    L1=input("Enter number")
    L2=input("Enter number")     

    l=L1+L2
    num=len(l)
    if num%3==0  and num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)  
fizzbuzz()