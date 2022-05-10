# Task 3 (simplified explanation):
# Write a function that, given two dictionaries, merges them while also
# combining the values of common keys between the two. 
# No imports are allowed.

def adddict (dict1:dict, dict2:dict) -> dict:
    """Merges two dictionaries, where common keys have their values combined.
    
    Args:
        dict1 (dict): First dictionary
        dict2 (dict): Second dictionary

    Returns:
        dict: A merged dict of dict1 and dict2, summing values of common keys.
        The final dictionary also retains the order of the two dictionaries.
    
    Example:
        Input: {'Lion': 1, 'Zebra': 2, 'Turtle': 3}, {'Zebra': 2, 'Turtle': 1, 'Elephant': 1}
        Result: {'Lion': 1, 'Zebra': 4, 'Turtle': 4, 'Elephant': 1}
    """
    total = {}  # initialize a new empty dictionary to store final results.
    for i in dict1:           # for each element in dict1, add the pair
        total[i] = dict1[i]   # from dict1 to the total dictionary.
    for i in dict2:           # For each pair in dict2, if the key is NOT
        if i not in total:    # in the total dictionary, add the pair
          total[i] = dict2[i] # to the total dictionary. If the key IS in the
        else:                 # total dictionary, add the dict2 key's value
            total[i] = total[i] + dict2[i] # to the present key's value.
    return total              # Return the resulting dictionary.
