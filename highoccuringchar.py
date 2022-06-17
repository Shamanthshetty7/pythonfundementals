# Highest Occuring Character

# For a given a string(str), find and return the highest occurring character.

# Sample Input 1:
# abdefgbabfba
# Sample Output 1:
# b


from sys import stdin

n=256
def highestOccuringChar(string) :
	#Your code goes here
    count=[0]*n
    for ele in string:
        count[ord(ele)]+=1
    max=count[0]
    for i in range(n):
        if max<count[i]:
            max=count[i]
            m=i
    return chr(m)
            
        
# main
string = stdin.readline().strip();
ans = highestOccuringChar(string)

print(ans)