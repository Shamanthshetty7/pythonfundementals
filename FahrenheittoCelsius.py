# USING FUNCTIONS

# Fahrenheit to Celsius Function

# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.

# Input Format :
# 3 integers - S, E and W respectively
# Output Format :
# Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. 
# Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")

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

def printTable(start,end,step):
    for f in range(start,end,step):
        c=(f-32)*5/9
        print(f,int(c))
        
s= int(input())
e= int(input())
st= int(input())
printTable(s,e,st)

# Thats it..