# Calculator

# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".

# Note: Each answer in next line.

# Sample Input:
# 3
# 1
# 2
# 4
# 4
# 2
# 1
# 3
# 2
# 7
# 6
# Sample Output:
# 2
# 2
# 5
# Invalid Operation


# Here is the program...
while (1):
    choice=int(input())
    if choice>=1 and choice<=5:
        a=int(input())
        b=int(input())
    if choice==1:
        print(a+b)
    if choice==2:                       # even you can use elif instead of using if again and again. 
        print(a-b)
    if choice==3:
        print(a*b)
    if choice==4:
        print(a//b)
    if choice==5:
        print(a%b)
    if choice==6:
        break                           # break function will break the loop and come out from the loop.
    if choice<1 or choice >6:
        print("invalid choice")
        
# and Thats it..
