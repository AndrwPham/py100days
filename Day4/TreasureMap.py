#Input: n = 3
#       postion = B3
#Output:[" ", " ", " "]
#       [" ", " ", " "]
#       [" ", "X", " "]
n = int(input("How large you want the map to be in NxN: "))
map = []
for _ in range(n):  #creates n lines
    line = []
    for i in range(n):  #creates n indexes per line
        line.append(" ")
    map.append(line)
position = input("Enter where you want your treasure in: ")
char_to_index = {}
for i in range(n):
    char_to_index[chr(65 + i)] = i  # chr(65) starts with 'A'
character = position[0]
number = int(position[1:]) - 1

if character not in char_to_index:
    print("Invalid character.")
row_index = number
column_index = char_to_index[character]  
if row_index < n and column_index < n:  # Check for valid indexes within nested_list
    map[row_index][column_index] = "X"
    print(f"{map}")
else:
    print("Out of bounds. Input refers to a non-existent element in the nested list.")



    


