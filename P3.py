# Program to sort elements in a stack using another temporary stack
def sort_stack(stack):
 
    temp_stack = []
    
    while stack:
        
        curr = stack.pop()
 
        while temp_stack and temp_stack[-1] > curr:
            stack.append(temp_stack.pop())

        temp_stack.append(curr)

    while temp_stack:
        stack.append(temp_stack.pop())

if __name__ == "__main__":
    stack = [34, 3, 31, 98, 92, 23]
    
    print("Original Stack:", stack)
    sort_stack(stack)
    print("Sorted Stack:", stack)
