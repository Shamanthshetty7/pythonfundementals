# Push Zeros to end

# You have been given a random integer array/list(ARR) of size N. 
# You have been required to push all the zeros that are present in the array/list to the end of it.
#  Also, make sure to maintain the relative order of the non-zero elements.

# Sample Input 1:
# 1
# 7
# 2 0 0 1 3 0 0

# Sample Output 1:
# 2 1 3 0 0 0 0

from sys import stdin

def pushZerosAtEnd(arr, n) :
    c=0
    for i in range(n):
        if(arr[i]!=0):
            arr[c]=arr[i]
            c+=1
    for j in range(c,n):
        arr[j]=0
        

            #Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1