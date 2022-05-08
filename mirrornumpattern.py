# Code : Mirror Number Pattern

# Pattern for N = 4

# ...1
# ..12
# .123
# 1234

# in the place of dot(.) print spaces.

## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(' ',end='')           # printing spaces seperately using loop and then  simultaneously number pattern
        s=s+1
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i+1
# Done.
