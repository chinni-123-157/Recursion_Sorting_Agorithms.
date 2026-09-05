def merge_sort(array, low, upper):
    if low >= upper:
        return
    else:
        mid = (low + upper) // 2

        merge_sort(array, low, mid)
        merge_sort(array, mid + 1, upper)

        merge(array, low, mid, upper)


def merge(array, low, mid, upper):

    temp = [0] * (upper - low + 1)

    i = low
    j = mid + 1
    t = 0

    def first():
        nonlocal i, j, t

        if i <= mid and j <= upper:

            if array[i] <= array[j]:
                temp[t] = array[i]
                i += 1
            else:
                temp[t] = array[j]
                j += 1

            t += 1
            first()

    def second():
        nonlocal j, t

        if j <= upper:
            temp[t] = array[j]
            j += 1
            t += 1
            second()

    def third():
        nonlocal i, t

        if i <= mid:
            temp[t] = array[i]
            i += 1
            t += 1
            third()

    def fourth(k):
        if k > upper:
            return

        array[k] = temp[k - low]
        fourth(k + 1)

    first()

    if i > mid:
        second()
    else:
        third()

    fourth(low)



'''
# Take array input from user
array = list(map(int, input("Enter numbers separated by spaces: ").split()))
'''


array = [8, 9, 4, 5, 7, 6, 1, 3, 2]

merge_sort(array, 0, len(array) - 1)

print("Array after sorted:", array)
