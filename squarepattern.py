# Lets move patterns
# this will improve your logic in looping

# Code : Square Pattern

#Sample Input 1:
# 7
# Sample Output 1:
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777
# 7777777

# here is your code
n=int(input())
i=1
while i<=n:                  # this for printing the nomber of rows 
    j=1
    while j<=n:              # and this for orinting the elements of every row
        print(n,end="")
        j=j+1
    print()
    i=i+1

# try to understand the logic behind the code.analyze each codes.