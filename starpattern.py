# Code : Star Pattern

# Pattern for N = 4

# ...*
# ..***
# .*****
# *******

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(' ',end='')                  # here its used 3 while loops cause there 3 devisions.one is for spaces.
        s=s+1
    j=1
    while j<=i:                            # this is for first half.
        print('*',end='')
        j=j+1
    p=i-1    
    while p>=1:                            # this for second half.
        print('*',end='')
        p=p-1
    print()
    i=i+1

# Easy.
