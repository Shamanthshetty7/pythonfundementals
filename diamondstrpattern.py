# Code : Diamond of stars

# Note: N is always odd.


# Pattern for N = 5

# ..*
# .***
# *****
# .***
# ..*

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
n1=(n+1)//2
n2=n//2
i=1
while i<=n1:
    s=1
    while s<=(n1-i):
        print(' ',end='')
        s=s+1
    j=1
    while j<=((2*i)-1):
        print('*',end='')
        j=j+1
    print()
    i=i+1
i=n2
while i>=1:
    s=1
    while s<=(n2-i+1):
        print(' ',end='')
        s=s+1
    j=1
    while j<=(2*i-1):
        print('*',end='')
        j=j+1
    print()
    i=i-1

# Move ahead.
