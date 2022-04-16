# Sum Of N Numbers.
# Given an integer n, find and print the sum of numbers from 1 to n.
# using while loop only..

# Sample Input :
# 10
# Sample Output :
# 55

# Read input as sepcified in the question
# Print output as specified in the question
n=int(input())
count=1               # count is used to make our loop as much  we want.
sum=0                 # initialization of the variable is needed at the begining otherwise variable will take garbage value or throws error.
while count<=n:       # while loop is the type of looping..is used to repeat the the task according to the users count.
    sum=sum+count     # sum will store all the sums through out the looping.
    count=count+1     # incrementation or changing count value is necessory to run the loop otherwise loop will get into infinite loop. 
print(sum)            # outside the loop the stored sum should be printed.

# indentation is very much important in python..without indentation python throws error.

# and thats it..lets move to next program.
    
    