def find_next_greater(arr):
    n = len(arr)
    # Array to store the next greater element for each element
    result = [-1] * n
    
    # Stack to store indices of the elements
    stack = []

    # Iterate over the array
    for i in range(n):
        # While the stack is not empty and the current element is greater than the element 
        # corresponding to the index at the top of the stack, update the result
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]  # arr[i] is the next greater element for arr[index]
        
        # Push the current element's index onto the stack
        stack.append(i)
    
    # Print the results
    for i in range(n):
        print(f"{arr[i]} -> {result[i]}")

# Test the function with an example array
if __name__ == "__main__":
    arr = [4, 5, 2, 22]
    find_next_greater(arr)
