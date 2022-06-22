# Wave Print

# For a given two-dimensional integer array/list of size (N x M),
#  print the array/list in a sine wave order, i.e, print the first column top to bottom, next column bottom to top and so on.

# Sample Input 1:
# 1
# 3 4 
# 1  2  3  4 
# 5  6  7  8 
# 9 10 11 12
# Sample Output 1:
# 1 5 9 10 6 2 3 7 11 12 8 4

from sys import stdin

def wavePrint(arr, n, m):

    j = 0

    wave = 1

     

    # m     - Ending row index

    # n     - Ending column index

    # i, j     - Iterator

    # wave     - for Direction

    # wave = 1 - Wave direction down

    # wave = 0 - Wave direction up 

    while j<m:

         

        # Check whether to go in

        # upward or downward

        if wave == 1:

     

            # Print the element of the 

            # matrix downward since the

                        # value of wave = 1

            for i in range(n):

                print(arr[i][j], end =' ')

            wave = 0

            j+=1

             

             

        else:

            # Print the elements of the 

            # matrix upward since the 

            # value of wave = 0

            for i in range(n-1,-1,-1):

                print(arr[i][j], end = ' ')

                 

            wave = 1

            j +=1

#Taking Iput Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()

    t -= 1