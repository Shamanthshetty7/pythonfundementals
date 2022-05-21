# Fibonacci Member

# Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
# F(n) = F(n-1) + F(n-2)
# where F(0) = 0 and F(1) = 1
# Sample Input 1 :
# 5
# Sample Output 1 :
# true


def checkMember(m):
    a=0
    b=1
    c=-1
    if m==0 or m==1:
        return 1
    else:
        while a<m:
            c=a+b
            b=a
            a=c
        if c==m:
            return 1
        else:
            return 0
    
n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

# Done.