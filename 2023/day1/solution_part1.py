import re
from typing import List

# Opens the txt file containing the given calibration values
file1 = open('callibration.txt', 'r')
line_cal = 0
result = []

# Iterate through each line in the file
for line in file1:
    # Extract numbers from the line using regular expression
    numbers = re.findall('[0-9]', line)

    # If only one number is found, duplicate it and append to the result
    if len(numbers) == 1:
        result.append(''.join(numbers + numbers))
    else:
        # If more than one number is found, take every other number and append to the result
        f_l = numbers[::len(numbers) - 1]
        result.append(''.join(f_l))

# Close the file after reading
file1.close()

# Convert the list of results to integers and calculate the sum
int_list: List[int] = [int(char) for char in result]
int_result = sum(int_list)

# Print the final result
print(int_result)