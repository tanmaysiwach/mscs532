import random
import time

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]  # Move pivot to end
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)


def time_sort(func, arr):
    arr_copy = arr.copy()
    start = time.time()
    func(arr_copy)
    return time.time() - start


def run_tests():
    sizes = [10, 50, 100, 200, 500]
    test_types = {
        "Random": lambda n: random.sample(range(n * 2), n),
        "Sorted": lambda n: list(range(n)),
        "Reverse Sorted": lambda n: list(range(n, 0, -1)),
        "Repeated Elements": lambda n: [random.choice([1, 2, 3, 4, 5]) for _ in range(n)],
    }
    for size in sizes:
        print(f"\n--- Array Size: {size} ---")
        for test_name, generator in test_types.items():
            arr = generator(size)
            time_rand = time_sort(lambda x: randomized_quicksort(x, 0, len(x) - 1), arr)
            time_det = time_sort(lambda x: deterministic_quicksort(x, 0, len(x) - 1), arr)
            print(f"{test_name:<20} | Randomized: {time_rand:.5f}s | Deterministic: {time_det:.5f}s")

if __name__ == "__main__":
    run_tests()
