# Code : Interesting Alphabets

# Pattern for N = 5
# E
# DE
# CDE
# BCDE
# ABCDE

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    j=i
    sc=chr(ord('A')+n-1)
    while j>=1:
        cp=chr(ord(sc)-j+1)         # we cant increment character by directly adding integers.w have to know the ascii value of perticular character then t that we can integers.
        print(cp,end='')
        j=j-1
    print()
    i=i+1

# Practice on ord() function and char() function with your own effort.It will help you to build your logic thinking ability. 

