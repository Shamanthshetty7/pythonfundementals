# Array's and Lists

# Array Sum

# Input Format :

# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces

# Output Format :
# Sum

## Read input as specified in the question.
## Print output as specified in the qu
n=int(input())
li=[int(x) for x in input().split()]          # split() function is used to take space seperated inputs.
sum=0
for ele in li:                                # for ele in li -- means it gives directly the element present in the list sequentially.
    sum=sum+ele
print(sum)

 
    
    


    