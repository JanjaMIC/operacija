# -*- coding: utf-8 -*-

x = int(raw_input("Please insert number from 1 up to 100: "))

for x in range(1, x+1):


    if (x%5) == 0 and (x%3) == 0:
        print ("FizzBuzz")
    elif (x%3) == 0:
        print ("Fizz")
    elif (x%5) == 0:
        print ("Buzz")
    else:
        print x