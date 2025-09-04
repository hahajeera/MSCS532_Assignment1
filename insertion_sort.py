def insertion_sort_desc(arr):
    """
    Performs insertion sort on arr in descending order.
    """
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1

        # Move elements smaller than key_item to the right
        while j >= 0 and arr[j] < key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key_item
    return arr


if __name__ == "__main__":
    numbers = [9, 3, 5, 2, 8, 1]
    insertion_sort_desc(numbers)
    print("Sorted descending:", numbers)
