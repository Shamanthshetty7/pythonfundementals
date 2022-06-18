# Compress the String

# Write a program to do basic string compression.
#  For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.

# Sample Input 1:
# aaabbccdsa
# Sample Output 1:
# a3b2c2dsa

def getCompressedString(input) :
    index = 0
    compressed = ""
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed


# Main.
string = input()
ans = getCompressedString(string)
print(ans)