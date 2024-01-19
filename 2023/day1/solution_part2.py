import re
def words2digits(inputline):
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

    inputline = inputline.rstrip()
    reverse_inputline = inputline[::-1]
    first = ""
    second =""
    index = 0

    # Using regular expression to find all non-digit sequences ('\D+') or digit sequences ('\d')
    # in the inputline. This separates the alphanumeric characters and digits, returning a list in the original order.
    result = re.findall(r'\D+|\d', inputline)
    reverse_result = re.findall(r'\D+|\d', reverse_inputline)

    #iterates between each split item from the list "result"
    for item in result:
        if item.isalpha():
            while len(item) > 0:
                for char in item:
                    first += char
                    if first in word2digit:
                        first = word2digit[first]
                        item = ""
                        break
                else:
                    item = item[1:]
                    first = ""
            result = result[1:]

        elif item.isdigit():
            first = item
            result = result[1:]
        if first != "":
            break

    for item in reverse_result:
        if item.isalpha():
            while len(item) > 0:
                for char in item:
                    second = char + second
                    if second in word2digit:
                        second = word2digit[second]
                        item = ""
                        break
                else:
                    item = item[1:]
                    second = ""
            result = result[1:]

        elif item.isdigit():
            second = item
            result = result[1:]
        if second != "":
            break

    both = first + second
    return both  # Return None if no word number is found


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