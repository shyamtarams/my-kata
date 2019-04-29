def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


arr = [1, 0]
print(binary_array_to_number(arr))