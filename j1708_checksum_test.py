from j1708 import checksum

array = [128, 91, 0, 92, 15, 190, 43, 10, 85, 96, 121, 0, 183, 53,0, 184,0,0, 245]
array2 = [128,91,92,190,0,11]

def sum_array(array):
    sum_array = 0
    for i in range(0,(len(array)-1)):
        sum_array += array[i]
    sum_array &= 255
    sum_array = 256 - sum_array
    return sum_array

#123 is expected
print sum_array(array)
print checksum(array)
