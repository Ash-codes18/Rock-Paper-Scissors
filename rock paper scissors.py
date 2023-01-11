import random
Draw=0
Won=0
Lost=0
print()
print("                                Welcome to the Rock Paper Scissor game!")
print()
print()
print("Let's Start...")
# print()
l=["Rock","Paper","Scissor"]
x=len(l)
y=(l[random.randint(0,x-1)])
# print("Enter your choice :")
r=int(input("Enter the no. of rounds you want to have : "))
print()
print()
for i in range(0,r):
    print("Round",i+1,":")
    print()
    print("Options :")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    print("4. Quit")
    a=int(input("Enter your choice : "))
    print()
    if a==1:
        u="Rock"
    if a==2:
        u="Paper"
    if a==3:
        u="Scissor"
    while y=="Rock":
        if u=="Rock":
            print("Computer's choice: Rock")
            print("User's choice: Rock")
            print("It's a Draw!")
            print()
            print()
            Draw+=1
            break
        if u=="Paper":
            print("Computer's choice: Rock")
            print("User's choice: Paper")
            print("You have Won!")
            print()
            print()
            Won+=1
            break
        if u=="Scissor":
            print("Computer's choice: Rock")
            print("User's choice: Scissor")
            print("You have Lost!")
            print()
            print()
            Lost+=1
            break
    while y=="Paper":
        if u=="Paper":
            print("Computer's choice: Paper")
            print("User's choice: Paper")
            print("It's a Draw!")
            print()
            print()
            Draw+=1
            break
        if u=="Rock":
            print("Computer's choice: Paper")
            print("User's choice: Rock")
            print("You have Lost!")
            print()
            print()
            Lost+=1
            break
        if u=="Scissor":
            print("Computer's choice: Paper")
            print("User's choice: Scissor")
            print("You have Won!")
            print()
            print()
            Won+=1
            break
    while y=="Scissor":
        if u=="Scissor":
            print("Computer's choice: Scissor")
            print("User's choice: Scissor")
            print("It's a Draw!")
            print()
            print()
            Draw+=1
            break
        if u=="Paper":
            print("Computer's choice: Scissor")
            print("User's choice: Paper")
            print("You have Lost!")
            print()
            print()
            Lost+=1
            break
        if u=="Rock":
            print("Computer's choice: Scissor")
            print("User's choice: Rock")
            print("You have Won!")
            print()
            print()
            Won+=1
            break
    if a==4:
        break
print()
print("User's score :",Won)
print("Computer's score:",Lost)
print()
print("Final Result : ")
if Won==Lost:
    print("The match is a draw 😊")
if Won>Lost:
    print("You have won the match 😁")
if Won<Lost:
    print("You have lost the match 😭")
print()
print()
print()
cl=input("Press Enter to continue.....")
if cl==" ":
    print("The game is over.")


