def bubble_sort(array, i, n):
    if i >= n - 1:
        return
    def innerloop(array, j, n, i):
        if j >= n - 1 - i:
            return
        if array[j] > array[j + 1]:
            array[j] = array[j] ^ array[j + 1]
            array[j + 1] = array[j] ^ array[j + 1]
            array[j] = array[j] ^ array[j + 1]
        innerloop(array, j + 1, n, i)
    innerloop(array, 0, n, i)
    bubble_sort(array, i + 1, n)
'''
# Take array input from user
array = list(map(int, input("Enter numbers separated by spaces: ").split()))
'''
#array = [9, 4, 5, 7, 6, 1, 2, 8, 3]

bubble_sort(array, 0, len(array))
print('Array sorted:', array)
