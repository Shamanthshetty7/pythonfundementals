# Code Merge Two Sorted Arrays

# You have been given two sorted arrays/lists(ARR1 and ARR2) of size N and M respectively, 
# merge them into a third array/list such that the third array is also sorted.

# Sample Input 1 :
# 1
# 5
# 1 3 4 7 11
# 4
# 2 4 6 13
# Sample Output 1 :
# 1 2 3 4 4 6 7 11 13 

from sys import stdin

def merge(arr1, n, arr2, m) : 
    i=0 
    j=0
    li=[]
    while (i<n and j<m ):
        if( arr1[i]<arr2[j]):
            li.append(arr1[i])
            i=i+1
        else:
            li.append(arr2[j])
            j=j+1
    while i<n:
        li.append(arr1[i])
        i=i+1
    while j<m:	

        li.append(arr2[j])
        j=j+1
    return li
        
            

    return li
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


# to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


# main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1