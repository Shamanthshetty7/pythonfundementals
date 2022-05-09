# Alpha Pattern

# Pattern for N = 3

# A
# BB
# CCC

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:
    sc=chr(ord('A')+i-1)    # getting first letter and storing. 
    j=1
    while j<=i:
        cp=chr(ord(sc))
        print(cp,end="")
        j=j+1
    print()
    i=i+1 

# Yes you are moving, each program that you are learning is making your foundation stronger. so dont stop.
