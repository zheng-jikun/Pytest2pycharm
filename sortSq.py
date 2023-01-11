

def custom_sort(sequence: list) -> list:
    """Returns a sorted copy of a given list."""
    arr = sequence[:]
    n = len(arr)

    for i in range(1, n):
        for j in range(0, n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr