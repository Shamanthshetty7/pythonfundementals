# Sum of even & odd

# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
# Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
# Sample Input 1:
# 1234
# Sample Output 1:
# 6 4

# here is the code
## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
n=int(input())
sum_e=0                # to add even numbers
sum_o=0                # to add odd numbers
while n!=0:        
    if n>0:
        i=n%10         # taking reminder to seprate digit to get every single number.
        n=n//10        # removing used numbers
    if i%2==0:         # if the number is even then it must be devided by 2 so reminder will be zero.
      sum_e+=i         # if even
    else:
      sum_o+=i         # else odd
print(sum_e, sum_o)    # printing 

# and thats it.

    



    
