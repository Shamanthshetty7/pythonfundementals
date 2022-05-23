# Pyramid Number Pattern

# Pattern for N = 4

#    1
#   212
#  32123
# 4321234

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    s=1
    while  s<=n-i:
        print(' ',end="")
        s=s+1
    j=1
    p=i
    while j<=i:
        print(p,end="")
        j=j+1
        p=p-1
    j=2
    while j<=i:
        print(j,end="")
        j=j+1
    print()
    i=i+1

    # Thats it.
