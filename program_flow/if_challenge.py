print("Please enter your name: ")
name = (input())

print("Hello {}. Please enter your age".format(name))
age = int(input())

if 18 < age <= 30:
    print("Welcome to the holiday my {}".format(name))
else:
    print("Sucks to suck you sucker")
