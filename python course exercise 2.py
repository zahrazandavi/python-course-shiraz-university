# 1. Write a program that reads a positive integer, n , from the user and then 
#  displays the sum of all of the integers from 1 to n. 
# n=int(input("enter the number:"))
# sum=sum(range(1,n+1))
# print(sum)

#  2. Create a program that reads two integers, a and b, from the user. 
#  Your program should compute and display: 
# • The sum of a and b 
# • The difference when b is subtracted from a 
# • The product of a and b 
# • The quotient when a is divided by b 
# • The remainder when a is divided by b 
# • The result of log10 a 
#  • The result of ab
# import math
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# sum=a+b
# difference=b-a
# andb=a*b
# qoutient=a/b
# remainder=a%b
# log=math.log(a)
# ab=a*b
# print("sum is ",sum)
# print("difference is",difference)
# print("a and b is",andb)
# print("qoutient is",qoutient)
# print("remainder is",remainder)
# print("log10 is",log)
# print("ab is",ab)

# 3. Write a program that begins by reading a number of cents from the user as 
# an integer. Then your program should compute and display the 
# denominations of the coins that should be used to give that amount of 
# # change to the shopper. The change should be given using as few coins as 
# # possible. Assume that the machine is loaded with pennies, nickels, dimes, 
# # quarters, loonies and toonies. 
# cents = int(input("Enter the number of cents: "))
# toonies = 200
# loonies = 100
# quarters = 25
# dimes = 10
# nickels = 5
# pennies = 1
# num_toonies = cents // toonies
# cents %= toonies
# num_loonies = cents // loonies
# cents %= loonies
# num_quarters = cents // quarters
# cents %= quarters
# num_dimes = cents // dimes
# cents %= dimes
# num_nickels = cents // nickels
# cents %= nickels
# num_pennies = cents // pennies
# print("Toonies:", num_toonies)
# print("Loonies:", num_loonies)
# print("Quarters:", num_quarters)
# print("Dimes:", num_dimes)
# print("Nickels:", num_nickels)
# print("Pennies:", num_pennies)

# 4. Write a program that reads a number of feet from the user, followed by a 
# number of inches. Once these values are read, your program should 
# compute and display the equivalent number of centimeters. 
# Hint: One foot is 12 inches. 
# One inch is 2.54 centimeters.
# f=int(input("enter number of feet in inches: "))
# cm=f*2.54
# print("number of your feet is",cm,"centimeters")

# 5. Write a program to accept two numbers from the user and calculate 
# multiplication
# a=int(input("enter the first number:"))
# b=int(input("enter the second number:"))
# m=a*b
# print("multilication is ",m)