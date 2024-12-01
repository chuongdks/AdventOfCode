from os.path import dirname

file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

left_list = []
right_list = []

# Split the input by new lines
for line in input_data.splitlines():
    left, right = map(int, line.split())  # Split each line and convert to integers
    left_list.append(left)
    right_list.append(right)
    
left_list.sort()
right_list.sort()

# Output the results
# print("Left List:", left_list)
# print("Right List:", right_list)

# Part 1:
answer = 0
for i in range(len(left_list)):
    distance = abs(left_list[i] - right_list[i])
    answer += distance

print(answer)

#Part 2:
answer = 0
count = 0
similarity_score = 0
for i in range(len(left_list)):
    element = left_list[i]
    for j in range(len(right_list)):
        if (element == right_list[j]):
            count += 1
    similarity_score = count * element
    answer += similarity_score
    count = 0
    
print(answer)
        
