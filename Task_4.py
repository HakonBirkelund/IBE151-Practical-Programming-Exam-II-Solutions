# Task 4 (direct citation):
# Write a function that, given a list and a set, returns a new list with
# the elements of the original list that are not present in the set.
# No imports are allowed.

def not_in_set(lst: list, uniques: set) -> list:
    """ Given a list and a set, returns a new list with elements not in the set

    Args:
        lst (list): List of elements (can be any, really)
        uniques (set): Set of elements (again, any type)

    Returns:
        list: A list of elements that are not present in the set.
        
    Example:
        Input: [1, 2, 5, 2, 6, 3, 5], {3, 2, 6, 7}
        Result: [1, 5, 5]
    """
    result = []     # Initialize new list to store the results
    for i in lst:   # For each element in the list
        if i not in uniques: # If element is not in the set
            result.append(i) # Append the element to the results.
    return result   # Return the result.
