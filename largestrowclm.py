# Two Dimensional array
# Largest Row or Column

# For a given two-dimensional integer array/list of size (N x M), 
# you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

# Sample Input 1 :
# 1
# 2 2 
# 1 1 
# 1 1
# Sample Output 1 :
# row 0 2

'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin

def findLargest(li, n, m):
    n = len(li) 
    m = len(li[0]) 
    max_sum = -1  
    max_sum = -1 
    for j in range(m):
        sum = 0
        for ele in li:
            sum += ele[j]
        if sum>max_sum:
            max_sum = sum
            max_index = j

    max_rindex = -1
    max_rsum = -1
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
        if sum > max_rsum:
            max_rsum = sum
            max_rindex = i
    if max_sum> max_rsum:
        print('column', max_index, max_sum)
    else:
        print('row', max_rindex, max_rsum)
    
        
# Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        print('row',0,-2147483648)
        exit(0)
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1