# Moving to CONDITIONALS and LOOPS
 
# Checking the given Number

# Given an integer n, find if n is positive, negative or 0.
# If n is positive, print "Positive"
# If n is negative, print "Negative"
# And if n is equal to 0, print "Zero".

# Sample Input 1 :
# 10
# Sample Output 1 :
# Positive

# checking whether the number is positive ,negative or zero
n=int(input())                            # taking user input
if n>0:                                   # if condition:  is used define our condition ..if condition satisfies then only the body of the if is executed.
    print("Positive")
elif n<0:                                 # elif condition: is used to give alternative condition if the 'if' condition fails then elif will be checked.
    print("Negative")
else:
    print("Zero")                         # else:  is executed when any one of the conditions are not satisfied.

# work out using your own programs..it will give you better practice.
