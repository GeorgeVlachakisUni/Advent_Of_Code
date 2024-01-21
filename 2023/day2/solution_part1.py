import re

blue = 0
red = 0
green = 0
finalist = 0
file1 = open('input.txt', 'r')
finalist_char = []
finalist_digit = []
finalists = 0
x = []
f = 0
sumofDigits = 0

for line in file1:
    f = 0
    input_line = re.split(r'[:;]', line)
    for item in input_line[1:]:
        if 'red' in item:
            x = re.split(r',', item)
            for item2 in x:
                if 'red' in item2:
                    red_char: str = ''.join(char for char in item2 if char.isdigit())
                    red: int = int(red_char) + red
        if 'blue' in item:
            x = re.split(r',', item)
            for item2 in x:
                if 'blue' in item2:
                    blue_char: str = ''.join(char for char in item2 if char.isdigit())
                    blue: int = int(blue_char) + blue
        if 'green' in item:
            x = re.split(r',', item)
            for item2 in x:
                if 'green' in item2:
                    green_char: str = ''.join(char for char in item2 if char.isdigit())
                    green: int = int(green_char) + green

        if red <= 12 and green <= 13 and blue <= 14:
            f += 1
            if f == (len(input_line)-1):
                finalist_char.append(input_line[0])

        #prints the games that disqualified and the reason why
        else:
            if red > 12:
                print(input_line[0] + " " + str(red) + " " + "red")
            if green > 13:
                print(input_line[0] + " " + str(green) + " " + "green")
            if blue > 14:
                print(input_line[0] + " " + str(blue) + " " + "blue")
        red = 0
        green = 0
        blue = 0
file1.close()

for item in finalist_char:
    finalist_digit.append(item.replace('Game ', ''))
for item2 in finalist_digit:
    if item2 != '':
        sumofDigits = int(item2) + sumofDigits



print(sumofDigits)
