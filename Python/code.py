# Finding a maximum among n elements in any
# language should not be worth any commenting really
def find_maximum(a):
    maximum = a[0]
    counter = 0
    for x in a:
        if x > maximum:
            maximum = x
        counter += 1
    return counter, maximum
# Same applies for finding the minimum
def find_minimum(a):
    minimum = a[0]
    counter = 0
    for x in a:
        if x < minimum:
            minimum = x
        counter += 1
    return counter, minimum


def advanced_counting_sort(a, high_key=None):
    # Phase 0: Normalizing for negative elements
    num_elements, low_key = find_minimum(a)
    for i in range(0, num_elements):
        a[i] -= low_key
    
    if not high_key:
        _, high_key = find_maximum(a)
    
    high_key -= low_key
    
    # Phase 1: Counting occurencies of each key
    counts = [0 for i in range(0, high_key + 1)]
    for i in range(0, num_elements):
        counts[a[i]] += 1
    
    # Phase 2: Adjusting result array pointers
    for i in range(1, high_key + 1):
        counts[i] += counts[i - 1]  # Counts-array becomes a pointer array
    
    # Phase 3: Backwardly filling up the result
    #          array with the input elements
    result = [None for x in a]
    for i in range(num_elements - 1, -1, -1):
        element = a[i]
        a[i] += low_key # Reverting normalization
        result_pointer = counts[element]
        result[result_pointer - 1] = element + low_key
        counts[element] -= 1
    
    return num_elements, result