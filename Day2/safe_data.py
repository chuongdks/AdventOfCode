from os.path import dirname

count = 0

def isSorted(a):
    global count 
    isIncrease = True
    isDecrease = True
    #
    for i in range (len(a) - 1):
        # Check increasing order
        if (a[i] > a[i+1]) or not (1 <= a[i+1] - a[i] <= 3): # just learn python, you could do that lol!
            isIncrease = False

        # Check decreasing order 
        if (a[i] < a[i+1]) or not (1 <= a[i] - a[i+1] <= 3):
            isDecrease = False
        
        # Return false early if both condition are False 
        if not isIncrease and not isDecrease:
            return False
        
    # Else line is sorted
    count += 1
    return isIncrease or isDecrease #

# Open file
file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

# Split the input by new lines
for line in input_data.splitlines():
    newline = map(int, line.split()) 
    print(isSorted(list(newline)))

print("Number of safe word: " + str(count))


        
