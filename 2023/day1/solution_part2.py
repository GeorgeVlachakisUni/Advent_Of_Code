import re


def words2digits(inputline):
    # Dictionary mapping word representations to digits
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

    # Remove trailing whitespace from the input line
    inputline = inputline.rstrip()

    # Reverse the input line for processing from the end
    reverse_inputline = inputline[::-1]
    first = ""
    second = ""
    index = 0

    # Using regular expression to find all non-digit sequences ('\D+') or digit sequences ('\d')
    # in the inputline. This separates the alphanumeric characters and digits, returning a list in the original order.
    result = re.findall(r'\D+|\d', inputline)
    reverse_result = re.findall(r'\D+|\d', reverse_inputline)

    # Iterate through each split item from the list "result"
    for item in result:
        if item.isalpha():
            while len(item) > 0:
                for char in item:
                    first += char
                    # Check if the accumulated string is in the word2digit dictionary
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
                    # Check if the accumulated string is in the word2digit dictionary
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

    # Combine the results from forward and reverse processing
    both = first + second
    return both  # Return None if no word number is found


# Open the file 'input.txt' for reading
file1 = open('input.txt', 'r')

line_cal = 0
result = []

# Iterate through each line in the file
for line in file1:
    # Convert word representations to digits using the words2digits function
    words2digit = words2digits(line)

    # Extract numbers from the result and append to the list
    numbers = re.findall('[0-9]', words2digit)
    if len(numbers) == 1:
        result.append(''.join(numbers + numbers))
    else:
        f_l = numbers[::len(numbers) - 1]
        result.append(''.join(f_l))

# Close the file after reading
file1.close()

# Convert the list of results to integers and calculate the sum
int_list = [int(char) for char in result]
int_result = sum(int_list)

# Print the final result
print(int_result)