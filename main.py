#This is a password generator program. You can add more simbols in case you need.

import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "(){}[]!;/,_"

all = lower + upper + numbers + symbols

#You can change the length of the password by changing the integer associated to the length variable
length = 16

#This part will generate a random password:
password = "".join(random.sample(all, length))
print(password)
