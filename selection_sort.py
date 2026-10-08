def selection_sort(array:list):
    sorted_array = list()
    copy_array = list(array)
    

    for i in range(0,len(copy_array)):
        lower = copy_array[0]
        lower_index = 0

        for j in range(len(copy_array)):
            if copy_array[j] < lower:
                lower = copy_array[j]
                lower_index = j

        sorted_array.append(copy_array.pop(lower_index))

    return sorted_array


def main():
    numbers = [
        42, 17, 89, 3, 65,
        28, 94, 11, 56, 73,
        6, 81, 35, 99, 24,
        50, 14, 67, 31, 78
    ]

    print(selection_sort(numbers))


if __name__ == "__main__":
    main()