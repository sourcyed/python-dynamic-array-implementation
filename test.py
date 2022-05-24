import ctypes
import ArrayList

def print_size(arr): # Prints the length of the array as well as its size in bytes.
    a = len(arr)
    b = ctypes.sizeof(arr.A)
    print("Length: {0}; Size in bytes: {1}".format(a, b))

def test(n): # Prints the sizes of the array for n number of elements added.
    arr = ArrayList.ArrayList()
    print_size(arr)

    for i in range(n):
        arr.append(n)
        print_size(arr)

test(100)