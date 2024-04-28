print(("game rules:- 0:snake,1:water,2:gun").title())
print("""            s w g
computer=  0 1 2
player=s(0)-w(2)
       w(1)-w(0)
       g(2)-w(1) snake will drink water, water will absorb gun, gun will kill snake""")
import random
def mazak():
    cinput=[0,1,2]
    b=random.choices(cinput,k=1)
    a=int(input("Give your attack:"))
    ac=0

    for i in b:
        if a==0:
            print("you win")if i == 1 else (print("match draw")) if a==i else print("you lose")
            print("My attack", i)
        elif a==1:
            print("you win") if i == 2 else (print("Match Draw")) if a==i else print("You Lose")
            print("My attack", i)
        elif a==2:
            print("you win") if i == 0 else (print("Match Draw")) if a == i else print("You Lose")
            print("My attack",i)
        else:
            print("Follow The Rules")

ab=0
while ab < 1:
    mazak()
