# Reverse of a number

# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

# Sample Input 1 :
# 1234
# Sample Output 1 :
# 4321

# Here is the code.
n=int(input())
rev=0                      # here we use rev varible to represent reverse.
while n>0:
    rem=n%10               # when you devide any number by you get the reminder which is the last number of the perticular digit. 
    rev=(rev*10)+rem       # logic  to perform reverse operation .
    n=n//10                # // is used to devide the number but as the output it gives only integer by removing the  fraction part.
print(rev)         

# move to next program.