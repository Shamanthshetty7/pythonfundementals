# 2. Write a program to input marks of three tests of a student (all integers). Then calculate and print the average of all test marks.
#Input format  :  3 Test marks (in different lines)
#Sample Input 1 :
# 3 
# 4 
# 6
# Sample Output 1 :
# 4.333333333333333
# Output format :  Average 


# programing is like any other sport ,you might know the rules but you have to play to learn...
# Read input as sepcified in the question
# Print output as specified in the quest
#Here you go
Marks1=int(input())                          # input() function is used to take the iput from the user
Marks2=int(input())                          # Bydefault input() function will take string.(if you give 1 then the input taken will be "1",which is not integer is string)
Marks3=int(input())                          # before using input() function mention the datatype which you are gonna take as input 
Average=(Marks1+Marks2+Marks3)/3             # Arthmetic operations works as per BODMAS rule.
print (Average)

#Try running the program using python3 ide
#let's move to next program