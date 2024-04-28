import os
cwd=os.getcwd()
list=os.listdir()
number=1
for i in list:
    if i.endswith(".pdf"):
        os.rename(f"{cwd}/{i}",f'{cwd}/{number} test.pdf')
        number=number+1
