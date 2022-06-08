# Check Array Rotation

# You have been given an integer array/list(ARR) of size N. 
# It has been sorted(in increasing order) and then rotated by some number 'K' in the right hand direction.
# Your task is to write a function that returns the value of 'K', that means, the index from which the array/list has been rotated.

# Sample Input 1:
# 1
# 6
# 5 6 1 2 3 4
# Sample Output 1:
# 2


from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
    min_index=0
    if n==0:
        return 0
    min = arr[0]
    for i in range(0, n):
    
        if (min > arr[i]):
        
            min = arr[i]
            min_index = i
        
    return min_index


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1