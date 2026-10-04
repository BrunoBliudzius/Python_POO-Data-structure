def binary_search(arr, value):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == value:
            return mid
        elif arr[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return None


def main():
    array = [i for i in range(240000)]

    value = 239999

    print("Starting binary search...")
    print("Found at index:", binary_search(array, value))


if __name__ == "__main__":
    main()
