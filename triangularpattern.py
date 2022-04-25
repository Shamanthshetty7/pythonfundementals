# Code : Triangular Star Pattern

# Pattern for N = 4
# *
# **
# ***
# ****


# Sample Input 1:
# 5
# Sample Output 1:
# *
# **
# ***
# ****
# *****

## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print('*',end="")   # end="" is used to give space instead of giving line break..
        j=j+1
    print()
    i=i+1

# its crazy...play with more patterns..it has lot of fun.