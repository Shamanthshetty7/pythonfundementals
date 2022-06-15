# Check Permutation

# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not

# Sample Input 1:
# abcde
# baedc

# Sample Output 1:
# true


from sys import stdin

NO_OF_CHARS = 256
def isPermutation(str1, str2) :
	# Your
	count1 = [0] * NO_OF_CHARS
	count2 = [0] * NO_OF_CHARS
	for i in str1:
		count1[ord(i)]+=1

	for j in str2:
		count2[ord(j)]+=1
	if len(str1) != len(str2):
		return 0
	for i in range(NO_OF_CHARS):
		if count1[i] != count2[i]:
			return 0
	return 1

# main
string1 = stdin.readline().strip();
string2 = stdin.readline().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')

