# Number Pattern 1

# Pattern for N = 4

# 1
# 11
# 111
# 1111

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
i=1
while i<=n:                   # printing row
      j=1
      while j<=i:             # number of columns in every row.
            print(1,end="")    
            j=j+1
      print()                 # giving line break after every row end.
      i=i+1

# Easiest one.