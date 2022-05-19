# Nth Fibonacci Number

# Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
# F(n) = F(n-1) + F(n-2), 
# Where, F(1) = F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number

# Sample Input 1:
# 6
# Sample Output 1:
# 8

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
a=0
b=1
c=-1
for i in range(n):        # using for loop.for i in range(initial condition,finalcondition,increment/decrement).by default initial condition will be zero and increment will be one.
    c=a+b                 # method of storing fibbonacci sequences.
    a=b
    b=c
print(a)

# Give little effort to understand the concept..
