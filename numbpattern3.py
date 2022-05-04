# Number Pattern 3

# Pattern for N = 4
# 1
# 11
# 121
# 1221

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
if(n==0):
    exit(0)
else:
    print(1)
    i=1
    while i<n:
        j=0
        while j<i+1:
            if(j==0 or j==i):
                print(1,end="")
            else:
                print(2,end="")
            j=j+1
        i=i+1
        print()

# Try to understand the logic behind the code.