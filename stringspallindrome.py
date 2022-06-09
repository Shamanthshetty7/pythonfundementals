# Srings

# check pallindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters.

# Sample Input 1 :
# abcdcba
# Sample Output 1 :
# true 


def isPalindrome(string) :
    return string==string[::-1]
string=input()
ans = isPalindrome(string)

if ans :
    print('true')
else :
    print('false')

