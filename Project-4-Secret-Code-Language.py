import random
print(("GIVE ONE BY WORD TO CODE/DECODE").title().center(150))

def code(a):
    list1 = ["a", "b", "c", "d", "hjsc", "f", "g", "h", "i", "j", "k", "l", "m", 'n', 'o', 'p', 'q', 'r.py', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
    b = list(a)
    b.append(b[0])
    del b[0]
    gh=random.choices(list1,k=3)
    hg=random.choices(list1,k=3)
    c = ''.join(b)
    c1=''.join(hg)
    c2=''.join(gh)
    print(c1+c+c2)

def code2(a):
    b=list(a)
    b.reverse()
    c=''.join(b)
    print(c)

def decode2(a):
    b = list(a)
    b.reverse()
    c = ''.join(b)
    print(c)

def decode(a):
    b =list(a)
    del b[0]
    del b[0]
    del b[0]
    del b[-1]
    del b[-1]
    del b[-1]
    for i in b:
        if (i==b[-1]):
            t=[i,]
            t1=t+b
            del(t1[-1])
            c=''.join(t1)
            print(c)
            break

def f():
    a=input("What do you want code/decode:")
    a1=a.title()
    if a1=="Code":
        b=input("Give your word to code:")
        if (len(b)<=3):
            code2(b)
        else:
            code(b)
    elif a1=="Decode":
        true = input("Give your word to decode:")
        if len(true)<=3:
            decode2(true)
        elif (len(true)>3) and (len(true)<6):
            raise IndexError("Your number should be >= 6 digit")
        else:
            decode(true)
    else:
        print("\"\"GIVE YOUR INPUT ONLY IN CODE/DECODE\"\"")
io=0
while io==0:
    f()
