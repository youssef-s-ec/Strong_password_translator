# import string module
import string
import random

# store all characters in lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# take number of characters from user
characters_number = input("How long would you like your password? : ")

# make sure the number of characters is greater than or equal 6.
while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 6:
            print("you need at least 6 characters")
            characters_number = input("please try a bigger number:")
        else:
            break
    except:
        print("Sorry, you may enter numbers only")
        characters_number = input("How long would you like your password? : ")

# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# calculate 30 % characters and 20%  numbers .
part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

# creat password with 60% characters and 40 % digits and punctuation.

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
print("your password is: " + password)
