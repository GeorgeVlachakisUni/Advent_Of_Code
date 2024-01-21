import re
result: int = 0
file1 = open('input.txt', 'r')

for line in file1:
    red: int = 0
    blue: int = 0
    green: int = 0
    input_line = re.split(r'[:;]', line)
    for item in input_line[1:]:
        x = re.split(r',', item)
        for item2 in x:
            if 'red' in item2:
                red_char: str = ''.join(char for char in item2 if char.isdigit())
                if red == 0:
                    red: int = int(red_char)
                elif red < int(red_char):
                    red: int = int(red_char)
            if 'blue' in item2:
                blue_char: str = ''.join(char for char in item2 if char.isdigit())
                if blue == 0:
                    blue: int = int(blue_char)
                elif blue < int(blue_char):
                    blue: int = int(blue_char)
            if 'green' in item2:
                green_char: str = ''.join(char for char in item2 if char.isdigit())
                if green == 0:
                    green: int = int(green_char)
                elif green < int(green_char):
                    green: int = int(green_char)
    result = (red * blue * green) + result
file1.close()
print(result)
