# Second Largest in array

# You have been given a random integer array/list(ARR) of size N.
#  You are required to find and return the second largest element present in the array/list.
# If N <= 1 or all the elements are same in the array/list then return -2147483648 or -2 ^ 31(It is the smallest value for the range of Integer)

# Sample Input 1:
# 1
# 7
# 2 13 4 1 3 6 28
# Sample Output 1:
# 13

# Take Minimum value as MIN_VALUE = -2147483648
from sys import stdin


def secondLargestElement(arr, n):
    #Your code goes here
    arr.sort()
    if n==0:
        return -2147483648
    for i in range(n-2, -1, -1):
        if (arr[i] != arr[n - 1]) :
                return arr[i]
 
    return -2147483648


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n
    else:
        return list(),0
    




#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1