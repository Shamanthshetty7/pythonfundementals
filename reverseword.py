# Reverse Each Word

# Aadil has been provided with a sentence in the form of a string as a function parameter.
#  The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.

# Sample Input 1:
# Welcome to Coding Ninjas

# Sample Output 1:
# emocleW ot gnidoC sajniN


from sys import stdin


def reverseEachWord(string) :
	# Your code goes here
    st =list()
 
    # Traverse given string and push all characters
    # to stack until we see a space.
    for i in range(len(string)):
        if string[i] != " ":
            st.append(string[i])
 
        # When we see a space, we print
        # contents of stack.
        else:
            while len(st) > 0:
                print(st[-1], end= "")
                st.pop()
            print(end = " ")
 
    # Since there may not be space after
    # last word.
    while len(st) > 0:
        print(st[-1], end = "")
        st.pop()

#main
string = stdin.readline().strip()
reverseEachWord(string)
