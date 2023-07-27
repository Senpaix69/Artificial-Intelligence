# write program that takes input from user in list till user enter -99 and then displays the list
def selection_sort(arr) -> list:
    for step in range(0, len(arr)):
        location = step
        for loc in range(step, len(arr)):
            if arr[loc] < arr[location]:
                location = loc
        arr[step], arr[location] = arr[location], arr[step]

    return arr


def fun(arr):
    while True:
        userInput = input("Enter a number: ")
        if len(userInput) == 0:
            print("You need to enter a number")
            continue
        num = int(userInput)
        if num == -99:
            if len(arr) < 6:
                print("You need to enter at least 6 elements")
                continue
            break
        arr.append(int(num))


def getEvenOdd(arr):
    even = []
    odd = []
    for elem in arr:
        if elem > 0:
            if elem % 2 == 0 and len(even) != 3:
                even.append(elem)
            elif len(odd) != 3:
                odd.append(elem)
            if len(odd) == 3 and len(even) == 3:
                break

    return even, odd


arr = []
fun(arr)
print("Original: ", arr)

A, B = getEvenOdd(arr)
print("A: ", A)
print("B: ", B)

C = A + B
print("C: ", C)

D = sorted(C)
print("D:", D)

D = sorted(D, reverse=True)
print("Reverse D:", D)

C[3] = 42
print("Changed fourth Element of C: ", C)

D.append(10)
print("After appending 10 to D: ", D)

C = C + [7, 8, 9]
print("After appening 7, 8, 9 in C: ", C)

print("First Three Element of C: ", end="")
for i in range(3):
    print(C[i], end=" ")

print("Last element of D: ", D.pop())
print("Length of D: ", len(D))
