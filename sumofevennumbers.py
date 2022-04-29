# Sum of Even Numbers

# Given a number N, print sum of all even numbers from 1 to N.
# Sample Input 1 :
# 6
# Sample Output 1 :
# 12

# here you go..

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
sum=0
i=2             # we are printing only even numbers so we are starting with even number.
while i<=n :    # while loop is used to repeat the process till the user input satisfies.
    sum=sum+i   # adding every even digit and assigning it to sum.
    i=i+2       # incrementing by 2 to get next even number.
    
print(sum)

# yah..move forward.
