import string
import random


def user_data():
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    user_email = input("Enter your Email address: ")

    details = [first_name, last_name, user_email]
    return details

def user_password(details):
    characters = string.ascii_letters
    length = 5
    random_password = ''.join(random.choice(characters) for i in range(length))

    password = str(details[0][0:2] + details[1][-2:] + random_password)

    return password

validation = True
storage = []

while validation:
    details = user_data()
    
    password = user_password(details)
    print ("Your password is: " + str(password))

    user_choice = input(str("do you like the password generated? If yes enter Yes, if no enter No and type in your password: "))

    password_loop = True

    while password_loop:
        if user_choice == 'Yes':
            details.append(password)

            storage.append(details) 

            password_loop = False
            break
        else:
            user_password = input(str("Enter password greater than or equal to 7:"))
    
            password_length = True

            while password_length:

                if len(user_password) >= 7:
                    details.append(user_password)

                    storage.append(details)

                    password_length = False

                    password_loop = False

                else:
                    print("Your password is less than 7") 
                    user_password = input(str("Enter your password:"))

    another_user = input(str("Would you like to enter another user? Yes/No:"))        
    if (another_user == "No"):
        validation = False
        for item in storage:
            print(item)
    else:
        validation = True
 