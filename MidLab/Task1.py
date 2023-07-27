def slice_and_reverse(lst):
    chunk_size = len(lst) // 3
    chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

    reversed_chunks = [chunk[::-1] for chunk in chunks]
    return reversed_chunks

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = slice_and_reverse(my_list)
print(result)