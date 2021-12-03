#!/usr/bin/env python3

print("Howdy there son! What's your name?")

my_name = input()

print("Hello there " + str(my_name) + "!...My name is Python, well Python3 to be precise. Wanna calculate some powers? \n\n 1. Yes\n 2. No")

my_decision = input()

if my_decision == "1":
    print("Wohoo! Good choice " + str(my_name) + "! Good choice...");

    print("Let's calculate some powers, shall we? Please input your base and hit ENTER...")
    my_base = int(input())
    
    print("Alright! Now input your exponent value, and hit ENTER so that I can give you your power result...")
    my_exponent = int(input())

    print("Moment of truth. You gave me a base and an exponent. Well, I present to you: ")
    print(pow(my_base, my_exponent))
                                                                
else:
    print("It's okay...I understand...");

