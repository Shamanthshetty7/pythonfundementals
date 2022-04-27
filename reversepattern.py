# Code : Reverse Number Pattern

# Pattern for N = 4
# 1
# 21
# 321
# 4321

## Read input as specified in the question
## Print the required output in given forma
n=int(input())
i=1
while i<=n:                     
    j=i
    while j>=1:                 # all patterns are depending on the looping and printing.
        print(j,end="")
        j=j-1
    print()
    i=i+1

    # Before jumping to do code for any problem,first analyze the problem make a proper algorithm then code.