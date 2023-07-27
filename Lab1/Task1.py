def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(myList):
    if len(myList) <= 1:
        return myList
    half = len(myList) // 2
    left = merge_sort(myList[:half])
    right = merge_sort(myList[half:])
    return merge(left, right)

myList = [6,54,6,7,43,5,5,6,353,53,6]
print(merge_sort(myList))
