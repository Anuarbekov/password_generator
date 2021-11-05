import random
numbers = "0123456789"  #10
spec_charac = "!@#$%^&*()"  #10
cap_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  #26
litt_letter = "abcdefghijklmnopqrstuvwxyz"  #26
print("Please choose, how many digits will be your password from 1 to 72")
length = int(input())
if length <= 72:
    all = numbers + spec_charac + cap_letter + litt_letter
    shuffled = sorted(list(all), key=lambda A: random.random())
    k = random.sample(shuffled, length)
    print("Your new passwword:", ''.join(k))
else:
    print("Your password length is more than all symbols")
