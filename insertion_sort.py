def insertion_sort_asc(arr):
    """
    Performs insertion sort on arr in ascending order.
    """
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr


if __name__ == "__main__":
    numbers = [9, 3, 5, 2, 8, 1]
    insertion_sort_asc(numbers)
    print("Sorted ascending:", numbers)
