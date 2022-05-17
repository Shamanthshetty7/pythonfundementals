# Print Number Pyramid

# For eg. N = 6

# 123456
#  23456
#    3456
#      456
#        56
#          6
#        56
#      456
#    3456
#  23456
# 123456

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
for i in range(1,n):
    print()
    for s in range(n,n-i+1,-1):
        print(' ',end='')
    for j in range(i,n+1,1):  
        print(j,end='')  
for i in range(n,0,-1):
    print()
    for s in range(n-i,n-1,1):
        print(' ',end='')
    for j in range(i,n+1,1):
        print(j,end='')

# keep going.