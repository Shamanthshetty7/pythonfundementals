# Lets move patterns
# This will improve your logic in looping

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
while i<=n:                  # This for printing the nomber of rows 
    j=1
    while j<=n:              # And this for orinting the elements of every row
        print(n,end="")
        j=j+1
    print()
    i=i+1

# Try to understand the logic behind the code.Analyze each codes.
