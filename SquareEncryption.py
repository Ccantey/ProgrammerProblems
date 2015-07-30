# A fairly simple way to encrypt a mesage is to strip all spaces and special characters from the message,
# and split the message into a 2-dimensional array, then transpose the array. example:

message = "How is everyone doing today"
square message = [H, o, w, i, s]
                 [e, v, e, r, y]
                 [o, n, e, d, o]
                 [i, n, g, t, o]
                 [d, a, y, 0, 0]
                 
encrypted message = [H, e, o, i, d]
                    [o, v, n, n, a]
                    [w, e, e, g, y]
                    [i, r, d, t, 0]
                    [s, y, o, o, 0]

#get valid user input
import re
import math
import pprint

while True:
    try:
        userInput = raw_input("Please enter a sentence void of special characters: ")
    except:
        print("sorry didn't understand that.")
        continue
    if re.search('[^a-z0-9 ]', userInput, re.IGNORECASE):
        print "Sorry that sentence contains some bullshit."
        continue       
    else:
        leanInput = userInput.replace(" ","")
        break

print "Your sentence, stripped of special characters", leanInput
print

#need to round up the square root so that we don't cut off sentences (ex: length = 10)
dimensions = int(math.ceil(math.sqrt(len(leanInput))))

print "Dimensions of the square code: ", dimensions, " x ", dimensions
print

#initialize matrix
Matrix = [[0 for x in range(dimensions)] for x in range(dimensions)]

#Magis happens here:
for y in xrange(dimensions):    
    for x in xrange(dimensions):
        for z in xrange(dimensions):
            try:
                Matrix[z][x] = leanInput[x + z*dimensions]
            except:
                #goes out of range so break out
                break

for row in Matrix:
    print row

print
print "And now the encrypted code:"
print

transpose = [[row[i] for row in Matrix] for i in range(dimensions)]
for row in transpose:
    print row


