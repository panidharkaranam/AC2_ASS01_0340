
# Program to find the reverse of a string using a stack

def reverse_string(input_str):
    stack = []
    
    # Push all characters of the string to the stack
    for char in input_str:
        stack.append(char)
    
    # Pop all characters from the stack and build the reversed string
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Test the function
input_str = "Hello, World!"
reversed_str = reverse_string(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_str)
