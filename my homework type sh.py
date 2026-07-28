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



