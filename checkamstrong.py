# Check Armstrong
# Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
#An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.

# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

# Input Format :
# Integer n
# Output Format :
# true or false

# Sample Input 1 :
# 1
# Sample Output 1 :
# true

## Read input as specified in the question.
## Print output as specified in the question.
def amstrong(a):
    temp=a
    rev=0
    sum=0
    digit=str(a)
    while a>0:
        rem=a%10
        sum=sum+(rem**len(digit))
        a=a//10
    if(n==sum):
        return 1
    else:
        return 0
n=int(input())
is_amstrong=amstrong(n)
if(is_amstrong):
      print("true")
else:
      print("false")

    