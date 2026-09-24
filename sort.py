# Алгоритмы сортировки


def bubble_sort(arr):
    """Сортировка пузырьком. Сложность: O(n^2)."""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """Быстрая сортировка. Сложность: O(n log n) в среднем."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3, 8, 4, 6]
    print("Исходный массив:", data)
    print("Bubble sort:    ", bubble_sort(data.copy()))
    print("Quick sort:     ", quick_sort(data.copy()))
