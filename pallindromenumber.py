# Palindrome number

# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121

# Sample Input 1 :
# 121
# Sample Output 1 :
# true

def checkPalindrome(a):
    temp=a
    rev=0
    while a>0:
        rem=a%10
        rev=(rev*10)+rem
        a=a//10
    if(temp==rev):
        return 1
    else:
        return 0
        
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')