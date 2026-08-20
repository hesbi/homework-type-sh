import random  
number = random.randint(0 , 101)
print('ay twin welcome to my "number guessing game" a random number has been selected dont ask how just try to guess it u got as many tries as u want goodluck')
while True :
    guess = input("guess ur number: ")
    if guess.isdigit() :
        guess = int(guess)
        if guess > number :
            print('ur  number has a higher value then the choosen number')
        elif guess < number :
            print('ur number has alower value then the choosen number')
        elif guess == number :
            print('congrats! u won chief')
            break
    else :
        print("u didnt enter a number brochacho")
#---------------------------------------------------------------------
import random
RPS = ["rock" , 'paper' , 'scissors']
system = random.choice(RPS) 
print('welcome to my rock paper scissors game')
while True :
    user = input('alr, [rock - paper - scissors] : ').lower().strip()
    print('system has picked =' , system)
    if system == user :
        print('tied')
    elif system == 'rock' and user == 'paper' :
        print('u win!')
        break
    elif system == 'paper' and user == 'scissors':
        print('u win!')
        break
    elif system == 'scissors' and user == 'rock':
        print('u win!')
        break
    else :
        print('u lost! *imagine losing to a robot lmao*')
        break
#--------------------------------------------------------------
while True :
    print('password must contain atleast 8 letters from the alphabet and the last piece of must contain a number')
    password = input('enter ur password :')
    if len(password) == 8 and not password[0:4].isdigit() and password[7].isdigit() :
        print('valid password!')
        break
    else :
        print('invalid passsword. . .')
#--------------------------------------------------------------
counter = 0
while True :
    num = (int(input('enter a number (keep in mind if u enter the number zero u dont ahve too enter a number anymore): ')))
    counter += num
    if num == 0 :
        print('sum of all the numbers u put in :' , counter)
        break
#--------------------------------------------------------------
for i in range(0 , 6) :
    print()
    for a in range(0,i+1) :
        print('*' , end="")







