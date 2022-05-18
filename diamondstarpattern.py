# Diamond of Stars

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
n2=n1-1
for i in range(1,n1+1,1):
    print()
    for s in range(1,n1-i+1):
        print(' ',end='')
    for j in range(1,2*i,1):
        print('*',end='')
for i in range(1,n2+1,1):
    print()
    for s in range(i,0,-1):
        print(' ',end='')
    for j in range(2*n2-2*i+2,1,-1):
        print('*',end='')

# move forward