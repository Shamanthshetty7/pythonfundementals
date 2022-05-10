# Code : Triangle of Numbers

# Pattern for N = 4

# ...1                       # dots for spaces.
# ..232
# .34543
# 4567654

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
p=0
while i<=n:
    s=1
    while s<=n-i:
        print(' ',end='')
        s=s+1
    j=1
    while j<=i:
        print(p+j,end='')
        j=j+1
    j=i-1
    while j>=1:
        print(p+j,end='')
        j=j-1
    print()
    i=i+1
    p=p+1

# analyse the code to understand.
