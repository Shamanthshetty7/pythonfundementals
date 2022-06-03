# Buble sort

# Provided with a random integer array/list(ARR) of size N, you have been required to sort this array using 'Bubble Sort'.

from sys import stdin                       # To include the external functions or operations on our program.Lybraries of respective functions is imprted by import command.

def bubbleSort(arr, n) :
    #Your code goes here
    for i in range(n-1):
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
            
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
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
    bubbleSort(arr, n)
    printList(arr, n)

    t-= 1