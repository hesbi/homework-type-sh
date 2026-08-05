# 1 - 
numbers = [15 , 50 , 70 , 1 , 90 , 20 , 4 , 108 , 6 ]
biggest = 0
for counter in numbers :
    if counter >= biggest :
        biggest = counter 
print("biggest number  = " , biggest)
# 2 - 
highest_record = 0 
for i in range (0 , 11): 
    records = int(input("place a record for the highest jump: "))
    if records > highest_record :
        highest_record = records
        print("a new record has been set = " , highest_record)
    elif records <= highest_record :
        print("this record has already been set")
# 3 - 
for a in range (1 , 11) : 
    if a % 2 == 0 :
        print(a , '+ 5 =' , (a+5))
    else : 
        print(a , "* 5 =" , (a*5))
# 4 -
username = input("enter ur user name : ")
count = 0
for q in username :
    count += 1
if count % 2 == 0 :
    half = username.find(" ")
    print(username[0 : half + 1])
else :
    half = username.find(" ")
    print(username[half : ])
# 5 - i already have a simple calculator code so i aint doin it again twin 
# 6 - 
allnum = 0 
for z in range (1 , 11) : 
    
    number = int(input("give me a number ="))
    allnum += number
avrg = (allnum/10)
print("average = ", avrg)
# 7 - 
color1 = input('enter first color: ')
color2 = input('enter second color: ')
color3 = input ('enter third color: ')
if color1 == color2 == color3 :
    print('3 colors are the same ')
elif color2 == color1 or color1 == color3 or color2 == color3 :
    print('two colors are the same ')
else : 
    print("none of the colors are the same")
# 8 -
amount_have = int(input('enter the amount u have on ur credit card: '))
amount_want = int(input("enter the amount u want: "))
if amount_want > amount_have :
    print('the amount u want is out of bound. . .')
elif amount_want <= 0 :
    print("error. . .")
else : 
    print('u have claimed' , amount_want , "from ur credit card u now have" , (amount_have - amount_want) , 'left')
# 9 -
numbs = [23 , 45 , -4 , 7 , -8 , -23 , 234 , -65]
for minus in numbs : 
    if minus < 0 :
        print ("negative numbers = " , minus)

