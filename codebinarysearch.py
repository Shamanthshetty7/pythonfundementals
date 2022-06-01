# Code Binary Search
# You have been given a sorted(in ascending order) integer array/list(ARR) of size N and an element X. 
# Write a function to search this element in the given input array/list using 'Binary Search'. 
# Return the index of the element in the input array/list. In case the element is not present in the array/list, then return -1.

# Sample Input 1:
# 7
# 1 3 7 9 11 12 45
# 1
# 3

# Sample Output 1:
# 1


from sys import stdin


def binarySearch(arr, n, x1) :
    if n==0:
        return -1
    s=0
    e=n-1
    while(s<=e):
            mid=(s+e)//2
            if arr[mid]==x1:
                return mid
            elif arr[mid]<x1:
                s=mid+1
            else:
                e=mid-1
    return -1
    
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


#main
arr, n = takeInput()
t = int(stdin.readline().strip())

while t > 0 :
    
    x = int(input().strip())    
    print(binarySearch(arr, n, x))
    t -= 1