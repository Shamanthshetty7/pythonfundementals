# Fahrenheit to Celsius

# One of the importants basic program..

# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
# Sample Input 1:
# 0 
# 100 
# 20
# Sample Output 1:
# 0   -17
# 20  -6
# 40  4
# 60  15
# 80  26
# 100 37

# Read input as sepcified in the question
# Print output as specified in the question

s=int(input())               # Starting value
e=int(input())               # ending value
w=int(input())               # difference
while s<=e :                 # loop will terminate when the condition is failed.
   celcious=(s-32)*5/9       # farnheit to celcious conversion formulae
   print  (s,int(celcious))  # printing both value at a time
   s=s+w                     # incrementation


# You are done with the code.

