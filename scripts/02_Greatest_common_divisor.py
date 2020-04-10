# By using math library
import math

a = int(input("Enter forst number: "))
b = int(input("Enter second number: "))

print("The gcd of 60 and 48 is :", math.gcd(a, b))



## Using recursion and fastest algorithm for GCD 
a = int(input("Enter forst number: "))
b = int(input("Enter second number: "))

def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)

print("The gcd of 60 and 48 is :", gcd(a, b))