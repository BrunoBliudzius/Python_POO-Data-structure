def quicksort(array: list):
    if len(array) < 2:
        return array
    
    first_element = array[0]

    lower = []
    for i in array:
        if i < first_element:
            lower.append(i)
    
    equal = []
    for i in array:
        if i == first_element:
            equal.append(i)

    bigger = []
    for i in array:
        if i > first_element:
            bigger.append(i)
    
    return quicksort(lower) + equal + quicksort(bigger)

numbers = [1,4,3,7,9]
print(f"sorted array: {quicksort(numbers)}")