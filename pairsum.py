# Pair Sum

# You have been given an integer array/list(ARR) and a number X. 
# Find and return the total number of pairs in the array/list which sum to X.

# Sample Input 1:
# 1
# 9
# 1 3 6 2 5 4 3 2 4
# 7

# Sample Output 1:
# 7

from sys import stdin


def pairSum(arr, n, x) :
    # Your code goes here
    count=0
    for i in range(n):
        k=i+1
        for j in range (k,n):
            if (arr[i]+arr[j]==x):
                count+=1
    return count

# Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(pairSum(arr, n, x))

    t -= 1