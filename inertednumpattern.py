# Code : Inverted Number Pattern

# Pattern for N = 4
# 4444
# 333
# 22
# 1

## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=n
while i>=1:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    print()
    i=i-1

# eeasy..