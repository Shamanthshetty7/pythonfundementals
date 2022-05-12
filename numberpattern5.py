# Number Pattern

# N = 5

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

# Running 3 loops for printing and 1 loop for rows.
# Analyze the code logically u will get know what is the process.
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end='')
        j=j+1
    s=1
    while s<=n-i:
        print(' ',' ',end='')
        s=s+1
    j=0
    while j<i:
        print(i-j,end='')
        j=j+1
    print()
    i=i+1