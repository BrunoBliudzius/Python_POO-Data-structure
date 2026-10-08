def factorial(x):
    if x == 1:
        return 1
    
    return x * factorial(x - 1)

def countdown(x):
    if x < 1:
        return

    print(x)
    return countdown(x - 1)

def sum(x):
    if x == 1:
        return 1

    return x + sum(x - 1)

def sum_array(array:list):
    if len(array) == 1:
        return array[0]

    last_element = array.pop()
    return last_element + sum_array(array)

def len_array(array: list):
    if len(array) == 0:
        return 0

    array.pop()
    return 1 + len_array(array)

def max_value(array:list, value=0):
    if len(array) == 0:
        return value
    
    max = array.pop()
    if value > max:
        max = value
    
    return max_value(array,max)


print(f"factorial(5) = {factorial(5)}")
print()

print("Countdown 5:")
{countdown(5)}
print()

print(f"sum(5) = {sum(5)}")
print()

print(f"Sum of array: {sum_array([2,4,6])}")
print()

print(f"length of array: {len_array([2,4,6])}")
print()

print(f"max element of array: {max_value([2,100,1001])}")
print()

