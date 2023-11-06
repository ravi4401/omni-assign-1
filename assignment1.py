#QUESTION-1

a=int(input("enter marks:"))
if a>=0 and a<=100:
    if a>=95<100:
        print("A+")
    elif a>=90<94:
        print("A")
    elif a>=85<90:
        print("B+")
    elif a>=80<84:
        print("B+")
    elif a>=75<79:
        print("C+")
    elif a>=65<74:
        print("C")
    elif a>=55<64:
        print("D+")
    elif a>=45<54:
        print("D")
    elif a<45:
        print("F")
    else:
        print("wrong input")


#QUESTION-2
a=str(input("enter a word:"))
b=len(a)
if b>10:
    first=a[0]
    last=a[-1]
    c=str(b-2)
    print(first+c+last)
else:
    print(a)
