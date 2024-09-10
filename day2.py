def find_missing_number(arr):
    n = len(arr) + 1  # Since the array has n-1 elements, the full length is n
    
    # Calculate the sum of first n natural numbers
    total_sum = n * (n + 1) // 2
    
    # Calculate the sum of elements in the array
    array_sum = sum(arr)
    
    # The missing number is the difference between the two sums
    missing_number = total_sum - array_sum
    return missing_number

