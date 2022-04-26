#  Entering infinite loop will throw you time limit exceeding errors.

i=0
while i<10:        # while loop
    print(i)       # body of the while loop
i = i+1            # incrementation outside the loop.There is no connection between loop body and this line.

# program will continously print the value of i which is assigned at  the begining.there is no termination cases.
# check it through any python ide
