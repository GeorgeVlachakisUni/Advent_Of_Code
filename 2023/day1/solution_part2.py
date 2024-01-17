import re





def words2digits(inputline):
    inputline = inputline.rstrip()
    word2digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    first: str = ""
    x = 0
    a = False
    digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    reverse_input = inputline[::-1]
    i = ['']
    iconstant = ['']
    double = ['']
    for char in inputline:
        x += 1
        iconstant.append(iconstant[-1] + char)
        i.append(i[-1] + char)
        if any(char in digit for char in i[x]) or any(word in word2digit for word in i[x].split()):
            first = i[x]
            if len(first) > 1:
                for word, digit in word2digit.items():
                    first = first.replace(word, digit)
                    x = 0
                for item in reversed(iconstant):
                    if inputline.startswith(item):
                        inputline = inputline[len(item):]
                        i = ['']
                        iconstant = ['']
                break
            else:
                x = 0
                for item in reversed(iconstant):
                    if inputline.startswith(item):
                        inputline = inputline[len(item):]
                        i = ['']
                        iconstant = ['']
                break

    while not a:
        for char in reverse_input:
            x += 1
            i.append(char + i[-1])
            iconstant.append(iconstant[-1] + char)
            if any(char in digit for char in i[x]) or any(word in word2digit for word in i[x].split()):
                second = i[x]
                if len(second) > 1:
                    for word, digit in word2digit.items():
                        second = second.replace(word, digit)
                    for item in reversed(iconstant):
                        if inputline.startswith(item):
                            inputline = inputline[len(item):]
                            i = ['']
                    x = 0  # Reset x to 0 after processing the second part
                elif len(second) == 1:
                    second = char
                    for item in reversed(iconstant):
                        if inputline.startswith(item):
                            inputline = inputline[len(item):]
                            i = ['']
                    x = 0  # Reset x to 0 after processing the second part
                a = True
                break

        reverse_input = reverse_input[1:]
        i = ['']
        x = -1

    # Assuming you want to concatenate first and second
    result : int = ''.join(first + second)
    return result
    # while 1:
    #     for char in reverse_input:
    #         x += 1
    #         i.append(char + i[-1])
    #         if any(char in digit for char in i[x]) or any(word in word2digit for word in i[x].split()):
    #             second = i[x]
    #             if len(second) > 1:
    #                 for word, digit in word2digit.items():
    #                     second = second.replace(word, digit)
    #                     x = 0
    #             elif len(second) == 1:
    #                 second = char
    #                 x = 0
    #             break
    #     reverse_input = reverse_input[1:]
    #     i = ['']
    #     x = 0
    #
    # double = double(''.join(first+second))




    # i.append(''.join(i + char))
    # for word, digit in word2digit.items():
    #         inputline = inputline.replace(word, digit)





#opens the txt containing the given the callibration values
file1 = open('callibration.txt', 'r')
line_cal = 0
result = []
for line in file1:
    words2digit = words2digits(line)
    numbers = re.findall('[0-9]', words2digit)
    if len(numbers) == 1:
        result.append(''.join(numbers+numbers))
    else:
        f_l = numbers[::len(numbers)-1]
        result.append(''.join(f_l))
file1.close()
int_list: int = [int(char) for char in result]
int_result = sum(int_list)



print(int_result)


