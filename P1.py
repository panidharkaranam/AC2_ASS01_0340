def trap(arr):
    n = len(arr)
    left = 0
    right = n - 1
    left_max = arr[left]
    right_max = arr[right]
    water = 0
    
    while left <= right:
        if arr[left] <= arr[right]:
            left_max = max(left_max, arr[left])
            water += left_max - arr[left]
            left += 1
        else:
            right_max = max(right_max, arr[right])
            water += right_max - arr[right]
            right -= 1
    
    return water

# Test the function
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("Trapped water:", trap(arr))
