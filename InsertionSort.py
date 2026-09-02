def insertion_sort(array, i, n):
    if i >= n:
        return
    else:
        temp = array[i]
        j = i - 1
        def shift_recursive(array, j, temp):
            if j >= 0 and array[j] > temp:
                array[j + 1] = array[j]
                shift_recursive(array, j - 1, temp)
            else:
                array[j + 1] = temp
        shift_recursive(array, j, temp)
        insertion_sort(array, i + 1, n)
'''
# Take array input from user
array = list(map(int, input("Enter numbers separated by spaces: ").split()))
'''

#array=[9, 4, 5, 7, 6, 1, 2, 8, 3]

insertion_sort(array, 1, len(array))
print('Array sorted:', array)
