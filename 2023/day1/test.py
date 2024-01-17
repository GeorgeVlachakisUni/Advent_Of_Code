from collections import deque

def words2digits(inputline):
    i = []
    for char in inputline:
        i = deque(i)
        i.appendleft(i + char)
    return i

# Example usage
input_line = "example"
result = words2digits(input_line)
print(result)