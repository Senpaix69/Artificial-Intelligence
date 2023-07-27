
def even(arr):
    chunk = len(arr)// 3
    return [arr[0:i: chunk] for i in range(0, len(arr), chunk)]

arr = [3,4,6,7,5,4,5,7,8,8]
print("Original: ", arr)
print("Chunks: ", even(arr))