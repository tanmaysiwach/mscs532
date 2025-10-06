def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)



def heapsort(arr):
    n = len(arr)
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)



def run_sorting_tests():
    import random, time
    sizes = [100, 1000, 5000]
    for size in sizes:
        print(f"\nArray size: {size}")
        for desc, gen in {
            "Random": lambda: random.sample(range(size * 2), size),
            "Sorted": lambda: list(range(size)),
            "Reverse Sorted": lambda: list(range(size, 0, -1))
        }.items():
            arr = gen()
            t0 = time.time()
            heapsort(arr.copy())
            t1 = time.time()
            print(f"{desc:<15}: {t1 - t0:.6f}s")



if __name__ == "__main__":
    run_sorting_tests()
