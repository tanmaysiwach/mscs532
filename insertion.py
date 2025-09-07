def insertion_sort_descending(arr):
    # Traverse from the second element to the end
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key to one position ahead
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

# Example usage
if __name__ == "__main__":
    data = [12, 4, 56, 17, 8, 99, 5]
    print("Original array:", data)
    insertion_sort_descending(data)
    print("Sorted array (descending):", data)
