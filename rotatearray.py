# Rotate array

# You have been given a random integer array/list(ARR) of size N.
#  Write a function that rotates the given array/list by D elements(towards the left).

# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 2
# Sample Output 1:
# 3 4 5 6 7 1 2

from sys import stdin


def rotate(arr, n, d):
    #Your code goes here
      arr[:]=arr[d:n]+arr[0:d]
      return arr

        

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1