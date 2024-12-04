from os.path import dirname
import re

# Open file
file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

# Use regex 
pattern = r"mul\((\d+),(\d+)\)" # use grouping '()' to take the number part only
# pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))" 
matches = re.findall(pattern, input_data)
#print(matches)

# for match in matches:
#     print(match)
    
sum = 0
mul = 1
for tuple in matches:
    for x in tuple:
        mul *= int(x)
    sum += mul
    mul = 1

print(sum)
