# Triplet Sum

# You have been given a random integer array/list(ARR) and a number X. 
# Find and return the number of triplets in the array/list which sum to X.


from sys import stdin

def findTriplet(arr, n, x) :
    #Your code goes here
    #return your answer
    count=0
    for i in range(n-2):
        T=i+1
        for j in range (T,n-1):
            p=j+1
            for e in range(p,n):
                if((arr[i]+arr[j]+arr[e])==x):
                    count=count+1
                
    return count
                
                    
# Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1