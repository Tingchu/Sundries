
# counting sort that has a map with only <radix> keys
def countingSourt(array, exp, radix=10):
    maximum = max(array)
    minimum = min(array)

    counts = [0] * radix
    result = [0] * len(array)

    for value in array:
        digit = (value // exp) % radix
        counts[digit] += 1

    # Make counts[] directly store the position of each value in array
    for ii in range(len(counts) - 1):
        counts[ii+1] += counts[ii]

    # result will be the sorted list
    for value in reversed(array):
        digit = (value // exp) % radix
        index = counts[digit] - 1
        result[index] = value
        counts[digit] -= 1

    # The outer array will know nothing about the rebinding in the method, so don't write it this way
    # array = result
    for idx, value in enumerate(result):
        array[idx] = value

def radixSort(array, radix=10):
    # Use the maimum value in array to get maximum number of digits
    maximum = max(array)
    count = 0
    while maximum > 0:
        count += 1
        maximum = maximum // radix

    tempArray = array
    minimum = min(array)
    if minimum < 0:
        # Shift values to make input array all positive
        tempArray = [x + (-minimum) for x in array]
    else:
        minimum = 0

    exp = 1
    for ii in range(count):
        countingSourt(tempArray, exp, radix)
        exp *= radix

    # Shift value back
    for idx, value in enumerate(tempArray):
        array[idx] = value + minimum

if __name__ == '__main__':
    # array1 = [8, 6, 3, 7, 60, 3, 60, 3, 212, 103, 113]
    array1 = [8, 6, 3, 7, 60, 3, 60, -12, 3, 212, -1, 103, -11, 113]
    # array2 = array1
    
    print("Original array:")
    print(array1)

    radixSort(array1)
    print("Sorted array (increasing, unstable):")
    print(array1)
