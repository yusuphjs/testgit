'''This is a "shombe"'''
#!/usr/bin/python3

import sys
import os

def circle_function(radius):

    r = float(radius)
    pi = 3.14
    area = pi*(r**2)
    perim = 2*pi*r

    print("THe area of this circle is: ",area)
    print("the perimeter of this circle is: ",perim)

def say_something(something):

    print(str(something))

if __name__ == "__main__":
    circle_function(sys.argv[1])
    say_something(sys.argv[2])
