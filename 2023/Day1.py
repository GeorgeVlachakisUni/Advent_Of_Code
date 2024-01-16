import re
from typing import List

#opens the txt containing the given the callibration values
file1 = open('callibration.txt', 'r')
line_cal = 0
result = []
for line in file1:
    numbers = re.findall('[0-9]', line)
    if len(numbers) == 1:
        result.append(''.join(numbers+numbers))
    else:
        f_l = numbers[::len(numbers)-1]
        result.append(''.join(f_l))
file1.close()
int_list: int = [int(char) for char in result]
int_result = sum(int_list)



print(int_result)