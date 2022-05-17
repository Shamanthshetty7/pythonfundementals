# Number Pattern 4

# Pattern for N = 4
# 1234
# 123
# 12
# 1

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=n

while i>=1:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    print()
    i=i-1
    
# Thats it..
