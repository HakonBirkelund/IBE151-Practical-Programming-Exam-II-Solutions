# Task 1 (direct citation):
# Write a function to return the index of the first even number of
# a list of numbers. If the list has no even numbers, return -1.
# No imports are allowed.

def firsteven (lst: list) -> int:
    """Finds the index of the first even number in a list of numbers.
        If none can be found, returns -1.

    Args:
        lst (list): A list of numbers

    Returns:
        int: The index of the first even number.
        
    Examples:
        Input: [3, 5, 4, 2]
        Result: 2 
        Input: [3, 5, 1, 13]
        Result: -1
    """
    acc = 0            # initialize accumulator at 0 (index starts at 0)
    for i in lst:      # Check each element in the list
        if i % 2 == 0: # If element is divisible by 2, it is even.
            return acc # Return accumulator, as it is same as index.
        acc += 1    # Increment accumulator for each iteration after checking.
    return -1       # Return -1 if there are no elements that are even.
