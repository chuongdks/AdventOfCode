from os.path import dirname

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
    return isIncrease or isDecrease # use Or to seperate

# Open file
file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

safeCounter = 0
# Split the input by new lines
for line in input_data.splitlines():
    newline = list(map(int, line.split())) 
    if isSorted(newline):
        safeCounter += 1
    # Check if removing a level is safe
    else: 
        for i in range(len(newline)):
            removeLine = newline[:i] + newline[i+1:] # You can fucking do that!
            if isSorted(removeLine):
                safeCounter += 1
                break # get out of the loop if removing a level is safe
            
print("Number of safe word: " + str(safeCounter))