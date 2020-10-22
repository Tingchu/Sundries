# Time complexity: O(n + range), range = maximum - minimum

def unstableCountingSort(array):
    maximum = max(array)
    minimum = min(array)

    counts = [0] * (maximum - minimum + 1)

    for value in array:
        counts[value - minimum] += 1

    # counts is a mapping from value to number of that value in array
    # The index of counts is the value in array

    index = 0
    for ii, count in enumerate(counts):
        for jj in range(count):
            array[index] = ii + minimum
            index += 1


def stableCountingSort(array):
    maximum = max(array)
    minimum = min(array)

    # Make a shift to save space
    # counts[0] represents the number of value "minimum" in array
    counts = [0] * (maximum - minimum + 1)
    result = [0] * len(array)

    for value in array:
        counts[value - minimum] += 1

    for ii in range(len(counts) - 1):
        counts[ii+1] += counts[ii]

    # counts[index] now stores number of values in input array that is smaller than or equal to the value "index" (including index itself)
    # E.g. counts[1] will be 3 because there are two values smaller than or equal to 1, including 1 itself

    # Traverse array in reversed order to make the sort algorithm stable, i.e. the same elements will keep the original order after sorted
    # Turn on the commented print and you will understand (compare reversed and normal order)
    for value in reversed(array):
        resultIdx = counts[value - minimum] - 1
        # print("value: {} resultIdx: {}".format(value, resultIdx))
        result[resultIdx] = value
        counts[value - minimum] -= 1

    # The outer array will know nothing about the rebinding in the method, so don't write it this way
    # array = result
    for idx, value in enumerate(result):
        array[idx] = value
        

if __name__ == '__main__':
    # Counting sort only deals with integers
    array1 = [8, 6, 3, 7, 1, 60, 3, 60, 4, -1, -10, 3]
    array2 = [8, 6, 3, 7, 1, 60, 3, 60, 4, -1, -10, 3]
    
    print("Original array:")
    print(array1)

    unstableCountingSort(array1)
    print("Sorted array (increasing, unstable):")
    print(array1)

    stableCountingSort(array2)
    print("Sorted array (increasing, stable):")
    print(array2)
