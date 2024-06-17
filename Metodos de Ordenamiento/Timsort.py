MIN_MERGE = 32

def calc_min_run(n):
    """Calcula el min_run según la longitud del array."""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(arr, left, right):
    """Realiza Insertion Sort en el subarray arr[left:right+1]."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    """Combina dos subarrays ordenados arr[l:m+1] y arr[m+1:r+1]."""
    len1, len2 = m - l + 1, r - m
    left = arr[l:l + len1]
    right = arr[m + 1:m + 1 + len2]
    
    i, j, k = 0, 0, l
    
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def tim_sort(arr):
    """Implementa el algoritmo Timsort."""
    n = len(arr)
    min_run = calc_min_run(n)

    # Ordenar segmentos individuales de tamaño 'min_run' usando Insertion Sort
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Fusionar segmentos ordenados
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(arr, left, mid, right)
        
        size *= 2

# Ejemplo de uso
arr = [5, 21, 7, 23, 19, 3, 17, 8, 15, 2, 9, 12, 22, 10, 6, 1, 18, 20, 4, 14, 13, 11, 16]
print("Array original:", arr)
tim_sort(arr)
print("Array ordenado:", arr)
