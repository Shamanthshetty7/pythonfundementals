# Palindrome number

# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

# Sample Input 1 :
# 121
# Sample Output 1 :
# true

# here is the code
n=int(input())
temp=n                     # assigning temporary varible to hold the value of n(if required)    
rev=0      
while n>0:
    rem=n%10              # finding the reverse as we already gone through previous program
    rev=(rev*10)+rem
    n=n//10
if(rev==temp):            # comparing reversed value with the original value
    print("true")         # if true
else:
    print('false')        # else

# and that's it.
