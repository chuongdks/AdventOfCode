from os.path import dirname
import re

# Open file
file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

# Use regex 
pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)" 
matches = re.findall(pattern, input_data)

#print(matches)

# Do math based on dewIt or not
sum = 0
dewIt = True

for match in matches:
    if match == "do()":
        dewIt = True
    elif match == "don't()":
        dewIt = False
        
    if dewIt and match.startswith("mul"):
        number = re.findall(r"\d+", match)
        mul = int(number[0]) * int(number[1])
        sum += mul

print(sum)
