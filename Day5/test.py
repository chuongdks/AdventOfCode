from os.path import dirname

file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

rows = input_data.splitlines()

orderList = []
updateList = []

for x in rows:  
    if "|" in x:  
        y = x.split("|")  
        orderList.append(y)  
        
for x in rows:  
    if "," in x:  
        y = x.split(",")  
        updateList.append(y)  
        
# print(orderList)
# print(updateList)

#Part 1
def checkValid(row):
    for i in range(len(row)):
        for j in range(len(orderList)):
            try:
                if row[i] == orderList[j][0] and row.index(orderList[j][1]) < i:
                    return False
            except:
                continue
    return True

#Part 2
def fixUpdateList(row):
    for i in range(len(row)):
        for j in range(len(orderList)):
            try:
                wrongIndex = row.index(orderList[j][1])
                if row[i] == orderList[j][0] and wrongIndex < i:
                    temp = row[i]
                    row[i] = row[wrongIndex]
                    row[wrongIndex] = temp
            except:
                continue
    return row

count = 0
validsUpdate = []
invalidsUpadte = []

# # Part 1
# for update in updateList:
#     if checkValid(update):
#         validsUpdate.append(update)

# Part 2
for update in updateList:
    if not checkValid(update):
        invalidsUpadte.append(update)

for i in range(len(invalidsUpadte)):
    while not checkValid(invalidsUpadte[i]):
        invalidsUpadte[i] = fixUpdateList(invalidsUpadte[i])

for update in invalidsUpadte:
    count += int(update[(len(update)) // 2]) # // is floor division
    
print(count)