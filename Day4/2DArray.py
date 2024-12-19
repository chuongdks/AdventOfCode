from os.path import dirname

file = open(f"{dirname(__file__)}/input.txt", "r")
input_data = file.read()
file.close()

rows = input_data.splitlines()
count = 0

# #PART 1:
# '''
# XMAS, SAMX
# '''
# for row in rows:
#     count += row.count("XMAS") + row.count("SAMX")
    
# '''
# X
#  M
#   A
#    S  
# '''
# for i in range(len(rows) - 3):
#     for j in range(len(rows[i]) - 3):
#         if rows[i][j] == 'X' and rows[i+1][j+1] == 'M' and rows[i+2][j+2] == 'A' and rows[i+3][j+3] == 'S':
#             count += 1

# '''
#    X
#   M
#  A 
# S    
# '''
# for i in range(len(rows) - 3):
#     for j in range(3, len(rows[i])):
#         if rows[i][j] == 'X' and rows[i+1][j-1] == 'M' and rows[i+2][j-2] == 'A' and rows[i+3][j-3] == 'S':
#             count += 1
            
# '''
# S
#  A
#   M
#    X  
# '''
# for i in range(len(rows) - 3):
#     for j in range(len(rows[0]) - 3):
#         if rows[i][j] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'M' and rows[i+3][j+3] == 'X':
#             count += 1
            
# '''
#    S
#   A
#  M 
# X    
# '''
# for i in range(len(rows) - 3):
#     for j in range(3, len(rows[i])):
#         if rows[i][j] == 'S' and rows[i+1][j-1] == 'A' and rows[i+2][j-2] == 'M' and rows[i+3][j-3] == 'X':
#             count += 1

# '''
# X
# M
# A
# S  
# '''
# for i in range(len(rows) - 3):
#     for j in range(len(rows[i])):
#         if rows[i][j] == 'X' and rows[i+1][j] == 'M' and rows[i+2][j] == 'A' and rows[i+3][j] == 'S':
#             count += 1
            
# '''
# S
# A
# M
# X  
# '''
# for i in range(len(rows) - 3):
#     for j in range(len(rows[i])):
#         if rows[i][j] == 'S' and rows[i+1][j] == 'A' and rows[i+2][j] == 'M' and rows[i+3][j] == 'X':
#             count += 1

# PART 2:
'''
M M
 A
S S
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[i]) - 2):
        if rows[i][j] == 'M' and rows[i][j+2] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'S' and rows[i+2][j+2] == 'S':
            count += 1
            
'''
M S
 A
M S
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[i]) - 2):
        if rows[i][j] == 'M' and rows[i][j+2] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'M' and rows[i+2][j+2] == 'S':
            count += 1
            
'''
S M
 A
S M
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[i]) - 2):
        if rows[i][j] == 'S' and rows[i][j+2] == 'M' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'S' and rows[i+2][j+2] == 'M':
            count += 1
            
'''
S S
 A
M M
'''
for i in range (len(rows) - 2):
    for j in range(len(rows[i]) - 2):
        if rows[i][j] == 'S' and rows[i][j+2] == 'S' and rows[i+1][j+1] == 'A' and rows[i+2][j] == 'M' and rows[i+2][j+2] == 'M':
            count += 1


print(count)
