# Remove character

# For a given a string(str) and a character X, write a function to remove all the occurrences of X from the given string.
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

# Sample Input 1:
# aabccbaa
# a
# Sample Output 1:
# bccb


from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
    # Your code goes here
    
    li=[ele for ele in string]
    n=len(li)
    for i in range(n-1,-1,-1):
        if li[i]==ch:
            li.remove(li[i])
    return li
#main
string =input()
ch = input()
ans = removeAllOccurrencesOfChar(string, ch)
for i in range(len(ans)):
    print(ans[i],end='')