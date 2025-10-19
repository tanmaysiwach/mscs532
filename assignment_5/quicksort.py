import random
import time
import sys

# It's good practice to increase the recursion limit for sorting large arrays
sys.setrecursionlimit(2000)

def partition_deterministic(arr, low, high):
    """
    Partitions the array using the last element as the pivot.

    Args:
        arr: The list of numbers to be partitioned.
        low: The starting index of the subarray.
        high: The ending index of the subarray.

    Returns:
        The index of the pivot element after partitioning.
    """
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_deterministic_recursive(arr, low, high):
    """
    The recursive function to perform Quicksort.

    Args:
        arr: The list of numbers to be sorted.
        low: The starting index.
        high: The ending index.
    """
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition_deterministic(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_deterministic_recursive(arr, low, pi - 1)
        quicksort_deterministic_recursive(arr, pi + 1, high)

def quicksort_deterministic(arr):
    """Wrapper function for deterministic Quicksort."""
    quicksort_deterministic_recursive(arr, 0, len(arr) - 1)


def partition_randomized(arr, low, high):
    """
    Partitions the array using a randomly chosen element as the pivot.

    Args:
        arr: The list of numbers to be partitioned.
        low: The starting index of the subarray.
        high: The ending index of the subarray.

    Returns:
        The index of the pivot element after partitioning.
    """
    # Choose a random pivot and move it to the end
    rand_pivot_index = random.randint(low, high)
    arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]

    # Use the deterministic partition logic with the new pivot at arr[high]
    return partition_deterministic(arr, low, high)

def quicksort_randomized_recursive(arr, low, high):
    """
    The recursive function to perform randomized Quicksort.

    Args:
        arr: The list of numbers to be sorted.
        low: The starting index.
        high: The ending index.
    """
    if low < high:
        # pi is the partitioning index, arr[pi] is now at the right place
        pi = partition_randomized(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort_randomized_recursive(arr, low, pi - 1)
        quicksort_randomized_recursive(arr, pi + 1, high)

def quicksort_randomized(arr):
    """Wrapper function for randomized Quicksort."""
    quicksort_randomized_recursive(arr, 0, len(arr) - 1)


def run_empirical_analysis():
    """
    Compares the performance of deterministic and randomized Quicksort
    on different types of input data.
    """
    sizes = [100, 500, 1000]
    distributions = ["Random", "Sorted", "Reverse-Sorted"]

    for size in sizes:
        print(f"\n----- Analyzing for input size: {size} -----")
        for dist_name in distributions:
            print(f"\n--- Distribution: {dist_name} ---")
            if dist_name == "Random":
                arr = [random.randint(0, size) for _ in range(size)]
            elif dist_name == "Sorted":
                arr = list(range(size))
            else: # Reverse-Sorted
                arr = list(range(size, 0, -1))

            # --- Test Deterministic Quicksort ---
            arr_copy_det = arr[:]
            start_time = time.perf_counter()
            try:
                quicksort_deterministic(arr_copy_det)
                end_time = time.perf_counter()
                print(f"Deterministic Quicksort Time: {end_time - start_time:.6f} seconds")
            except RecursionError:
                print("Deterministic Quicksort: Exceeded maximum recursion depth.")


            # --- Test Randomized Quicksort ---
            arr_copy_rand = arr[:]
            start_time = time.perf_counter()
            quicksort_randomized(arr_copy_rand)
            end_time = time.perf_counter()
            print(f"Randomized Quicksort Time:    {end_time - start_time:.6f} seconds")

# To run the analysis, uncomment the line below
# run_empirical_analysis()
