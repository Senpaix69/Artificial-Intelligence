def merge(left, right) -> list:
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


def findSum(myList) -> int:
    sum = 0
    for num in myList:
        sum += num
    return sum

def findMedian(myList) -> int:
    sortList = merge_sort(myList)
    return sortList[(len(myList) // 2)]

def fun():
    print("**** Note: Enter -99 to stop taking inputs ****")
    myList = []
    sum = 0
    mean = 0
    median = 0
    while True:
        userInput = input("Enter a number: ")
        if(len(userInput) != 0):
            num = int(userInput)
            if(num == -99):break
            myList.append(num)
        else:
            print("Error: Undefine")
    
    sum = findSum(myList)
    mean = sum / len(myList)
    median = findMedian(myList)

    print("Sum: ", sum)
    print("Mean: ", mean)
    print("Median: ", median)

fun()
