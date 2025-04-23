from j1708.Message import Message

array = bytes([128, 91, 0, 92, 15, 190, 43, 10, 85, 96, 121, 0, 183, 53,0, 184,0,0, 245])
array2 = bytes([128,91,92,190,0,11])
array3 = bytes([128,2,126])
array4 = bytes([128,5])

def sum_array(array):
    sum_array = 0
    for i in range(0,(len(array)-1)):
        sum_array += array[i]
    sum_array &= 255
    sum_array = 256 - sum_array
    return sum_array

print(Message(array).getDeviceName())
print(Message.CRC(array))
