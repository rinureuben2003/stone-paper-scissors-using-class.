import random
options=["stone","paper","scissors"]
num_rounds=int(input("how many rounds do you want to play?"))
user_score=0
computer_score=0
class play:
    def checker(num_rounds):
        global computer_score,user_score
        for round_num in range(num_rounds):
            print("round",round_num+1)
            user_choice=input("choose stone,paper,or scissors:")
            computer_choice=random.choice(options)
            print("computer choose",computer_choice)
            if user_choice==computer_choice:
                print("its a tie!")
            elif user_choice=="stone"and computer_choice=="paper":
                print("computer wins this round!")
                computer_score+=1
            elif user_choice=="stone" and computer_choice=="scissors":
                print("you win this round!")
                user_score+=1
            elif user_choice=="paper" and computer_choice=="stone":
                print("you win this round!")
                user_score+=1
            elif user_choice=="paper"and computer_choice=="scissors":
                print("computer win this round!")
                computer_score+=1
            elif user_choice=="scissors"and computer_choice=="stone":
                print("computer win this round!")
                computer_score+=1
            elif user_choice=="scissors"and computer_choice=="paper":
                print("you win this round!")
                user_score+=1
play.checker(num_rounds)
print("final scores:")
print("you:",user_score)
print("computer:",computer_score)
if user_score>computer_score:
    print("you win!")
elif computer_score>user_score:
    print("computer win!")
else:
    print("its a tie!")


            
            

     


