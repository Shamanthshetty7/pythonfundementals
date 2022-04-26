# Code : Triangle Number Pattern

# Pattern for N = 4
# 1
# 22
# 333
# 4444

# here is the code

## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:               # loop exexute the body till the condition fails.
        print(i,end="")
        j=j+1
    print()
    i=i+1

# analyize the code try to impliment other patterns along side.

