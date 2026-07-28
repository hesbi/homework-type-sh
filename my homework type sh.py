name_cm = input("plz enter ur name and 'code meli' : ")
name = name_cm[ : -10]
CM = int(name_cm[-10 : ])
print('name = ' , name)
print('code meli = ' , CM)
#--------------------------------------------------------
phone_number = input("plz enter ur phone number: ")
PH = phone_number[ 1 : 4]
print("operator thingy = " , PH)
#--------------------------------------------------------
username = input('plz enter ur username : ')
first_L = username[0]
USER = username.index(" ") #could've used find() to but whatever -_-
print("username = " , first_L + "." + username[USER + 1 : ])
#--------------------------------------------------------
cc_number = input('plz enter ur credit card number : ') #cc stand for credit card btw
reverse_cc = cc_number[: :-1]
print(reverse_cc)
#--------------------------------------------------------
traveled_distance = int(input('plz enter the travel distance: '))
if traveled_distance <= 2000 :
    print("payment =" , 5000)
if traveled_distance >= 7000 : 
    pay = (traveled_distance) // 5000
    payment = 2000 + (5000*pay) 
    print("payment =" , payment)
#--------------------------------------------------------
price_tag = int(input('plz enter the price tag of the object u bought: '))
if price_tag < 500000 :
    payment = price_tag
    print("payment =" , payment)
if 500000 <= price_tag <= 1000000 :
    payment = price_tag // (10/100)
    print("payment =" , payment)
if price_tag > 1000000 :
    payment = price_tag // (15/100)
    print("payment =" , payment)
#--------------------------------------------------------
credit_card_number = input('plz enter ur credit card number: ')
bank_sepah = 6037
if credit_card_number[ : 5] == bank_sepah :
    print( "credit card is from bank_sepah" )
else : 
    print('your credit card =' , credit_card_number)
#--------------------------------------------------------
time = float(input('give me a time [0|24]: '))
if time < 0 or 25 <= time :
    print('the time u entered is out of bound')
if 0 <= time <= 6 : 
    print('its midnight')
if 6 < time <= 12 :
    print('its day time')
if 12 < time <= 18 :
    print('its afternoon')
if 18 < time <= 24 :
    print(' its night time')





