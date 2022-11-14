## Dictionaries for python
#c
# Author :  Gaylene
# Created by :  Gaylene
# Architect(s):  Gaylene 
# Developer(s): Gaylene
# Created Date: 11/13/22 
# Description : reverse a string  
# Version: 1.0  
# Modified by:Gaylene
# Modified Date: 11/13/22
# program to find odd or even numbers no conditionals or control statement

#input  your number
# finding the even number by dividing by 2 
# saying if  n is divisible by 2 its even 
#if its not divisible by 2 its odd 

n= int(input("Enter a Number:"))
print("Even" * (n % 2 == 0), "Odd" * (n % 2 != 0))