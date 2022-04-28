# Code : Character Pattern

# Pattern for N = 4
# A
# BC
# CDE
# DEFG

## Read input as specified in the question
## Print the required output in given format
n=int(input())
i=1
while i<=n:
    j=1
    sc=chr(ord('A')+i-1)             # ord() function converts characters to its respective ascii value.and char() fucntion converts ascii to character.
    while j<=i:
        cp=chr(ord(sc)+j-1)
        print(cp,end="")
        j=j+1
    print()
    i=i+1

# all you have to learn is looping concept thoroughly.