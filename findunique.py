# Find Unique

# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.

# Sample Input 1:
# 1
# 7
# 2 3 1 6 3 6 2
# Sample Output 1:
# 1

import sys

def findUnique(arr, n) :
    for i in range(0,n):
        for j in range(0,n):
            if(i!=j and arr[i]==arr[j]):
                break
            if(j==n-1):
                return arr[i]

# Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1