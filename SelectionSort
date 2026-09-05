def selection_sort(array, i, n):
    if i >= n - 1:
        return

    min_index = i

    def innerloop(j):
        nonlocal min_index

        if j >= n:
            return

        if array[j] < array[min_index]:
            min_index = j

        innerloop(j + 1)

    innerloop(i + 1)

    if min_index != i:
        array[i] = array[i] + array[min_index]
        array[min_index] = array[i] - array[min_index]
        array[i] = array[i] - array[min_index]

    selection_sort(array, i + 1, n)


'''
# Take array input from user
array = list(map(int, input("Enter numbers separated by spaces: ").split()))
'''

array = [9, 4, 5, 7, 6, 1, 2, 8, 3]

selection_sort(array, 0, len(array))
print('Array sorted:', array)
