# A number x is a sum seed of y if the sum of x and x's digits equal y.
# For example 115: 98 + 9 + 8 = 115, therefore 98 is a sum seed of 115, so is 107: 107 + 1 + 0 + 7 = 115

# Create a script that determines if a user defined, positive integer has any sumseeds.
# It should also catch invalid input

#get valid user input
while True:
    try:
        userInput = input("Please enter an integer greater than zero: ")
    except:
        print("sorry didn't understand that.")
        continue
    if userInput <= 0:
        print "Sorry that is less than zero."
        continue
    if not isinstance(userInput, int):
        print "Sorry, you must enter an integer."
        continue        
    else:
        break

#store all numbers smaller than userInput in a list
numbersArray = []
for numbers in range(0,userInput):
    numbersArray.append(numbers)

goodbye ="Sorry, none found. Better luck next time!"
#for all values in numbers array, store
for values in numbersArray:
    #seeds = each digit of values
    seeds = [int(i) for i in str(values)]
    #add seeds together
    sumofseeds = sum(seeds)
    sumseeds = values + sumofseeds
    if sumseeds == userInput:
        print seeds," = ", sumofseeds, "+ ",values, " = ", sumseeds
        goodbye = "Wasn't that fun? Goodbye!"
    else:
        pass

print goodbye
        



