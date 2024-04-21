
from os import system
from string import ascii_lowercase, ascii_uppercase, digits

lowwer_letter = [i for i in ascii_lowercase]
upper_letter = [i for i in ascii_uppercase]
digit = [i for i in digits]
punction = ["?", "!", "@", "#", "$", "%", "&"]

password = "*pppAcie"

flag = True

count_lower = 0
count_upper = 0
count_digit = 0
count_punc = 0
count_blocked = 0


while flag:
    password = input("password : ")
    system("cls")

    if len(password) >= 8:
        for i in range(len(password)):
            if password[i] in lowwer_letter:
                count_lower += 1

            elif password[i] in upper_letter:
                count_upper += 1

            elif password[i] in digit:
                count_digit += 1

            elif password[i] in punction:
                count_punc += 1

            else:
                count_blocked += 1
        if 0 in [count_punc, count_digit, count_lower, count_upper] or count_blocked == 1:
            if count_blocked >= 1:
                print("you have used a blocked charechter")
            if count_digit == 0:
                print("you havent used a digit in your password")

            if count_lower == 0:
                print("you havent used a lower in your password")

            if count_upper == 0:
                print("you havent used a upper in your password")

            if count_punc == 0:
                print("you havent used a punction in your password")

            continue
        else:
            print("your password is okay and has been authenticated")
    else:
        system("cls")
        print("your password doesnt have 8 charekter")
        continue
