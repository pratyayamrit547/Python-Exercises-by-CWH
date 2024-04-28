def calculator():
    add=lambda h,g:(h+g)
    subtract=lambda h,g:(h-g)
    multiply=lambda h,g:(h*g)
    divide=lambda h,g:print(f"{g} is not equal to zero") if g==0 else print((h/g))
    try:
        a=int(input("1.ADD\n2.MULTIPLY\n3.SUBTRACT\n4.DIVIDE\nWhat operation do you want to perform:-"))
        b=float(input("Give First number:-"))
        c=float(input("Give Second number:-"))
        if b == str:
            raise ValueError
        if c== str:
            raise ValueError
        if a==1:
            solution=(add(b,c))
            print(f"the solution of the question is {solution}")
        elif a==2:
            solution=(multiply(b,c))
            print(f"the solution of the question is {solution}")
        elif a==3:
            solution=(subtract(b,c))
            print(f"the solution of the question is {solution}")
        elif a==4:
            solution=(divide(b,c))
            print(f"the solution of the question is {solution}")
        else:
            print("Give value properly")
    except Exception as e:
        print(f"the problem in your given input is {e}")
calculator()
while True:
    try:
        choice=input("do you want to (continue=c) or (exit=hjsc):").title()
        if choice=="C":
            calculator()
        elif choice=="E":
            break
        else:
            print("give your choice in (c) or (hjsc)")
    except Exception as e:
        print(f"the fault in your output is:\n{e}")
