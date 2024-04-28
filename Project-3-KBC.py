dict_of_ques={1000:{"what is the capital of India":"New Delhi"},2000:{"what is the capital of Bihar":"Patna"},3000:{"Who is known as the Father of the Nation in India?":"Mahatma Gandhi"},
5000:{"Which planet is known as the Red Planet?":"Mars"},10000:{"What is the chemical symbol for water[give answer in capital letter]?":"H2O"},20000:{"Who wrote the play \"Romeo and Juliet\"?":"William Shakespeare"},30000:{"What is the chemical symbol for gold?":"Au"},50000:{"What is the largest ocean in the world?":"Pacific Ocean"},100000:{"Which famous scientist formulated the theory of relativity?":"Albert Einstein"},200000:{"What is the capital city of France?":"Paris"}}
amount=0
index=1
for prizes,ques in dict_of_ques.items():
    for que,ans in ques.items():
        Q1=input(f"{index}. {que}:").title()
        if Q1==ans:
            amount+=prizes
            print(f"The prize you have won is {amount}")
            index+=1
        else:
            print(f"You gave the incorrect answer. The correct answer is {ans}\nThe total amount you won is:{amount}")
            quit()
print(f"The total amount you win is :{amount}")
