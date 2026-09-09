def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        partition_sort(arr, low, pi - 1)
        partition_sort(arr, pi + 1, high)


'''
# Take array input from user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
'''

arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
partition_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
