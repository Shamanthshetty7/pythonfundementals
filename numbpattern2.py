# Number Pattern 2

# Pattern for N = 4

# 1
# 11
# 202
# 3003 

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
print(1)
i=1
while i<n:
    j=0
    while j<i+1:
        if(j==0 or j==i) :
            print(i,end="")
        else:
            print(0,end="")
        j=j+1
    i=i+1
    print()

# play with numbers using loops.