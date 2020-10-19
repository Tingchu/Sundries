import os

# Sort in increasing order
def maxHeapify(array, arraySize, idx):
    root = idx
    leftChild = idx * 2 + 1
    rightChild = idx * 2 + 2
    largest = root

    # Find the largest among root, left child and right child
    if leftChild < arraySize and array[largest] < array[leftChild]:
        largest = leftChild

    if rightChild < arraySize and array[largest] < array[rightChild]:
        largest = rightChild

    if largest != root:
        array[largest], array[root] = array[root], array[largest]
        maxHeapify(array, arraySize, largest)

# Sort in decreasing order
def minHeapify(array, arraySize, idx):
    root = idx
    leftChild = idx * 2 + 1
    rightChild = idx * 2 + 2
    smallest = root

    # Find the smallest among root, left child and right child
    if leftChild < arraySize and array[smallest] > array[leftChild]:
        smallest = leftChild

    if rightChild < arraySize and array[smallest] > array[rightChild]:
        smallest = rightChild

    if smallest != root:
        array[smallest], array[root] = array[root], array[smallest]
        minHeapify(array, arraySize, smallest)

def heapSort(array, increase):
    arraySize = len(array)
    for idx in range(arraySize // 2 - 1, -1, -1):
        if increase:
            maxHeapify(array, arraySize, idx)
        else:
            minHeapify(array, arraySize, idx)

    for idx in range(arraySize - 1, 0, -1):
        array[idx], array[0] = array[0], array[idx]

        # Array size decreases each loop, to avoid changing sorted part (the last N elements are sorted)
        if increase:
            maxHeapify(array, idx, 0)
        else:
            minHeapify(array, idx, 0)

if __name__ == '__main__':
    array1 = [8, 6, 7, 2, 3, 4, -1]
    array2 = [8, 6, 7, 2, 3, 4, -1]
    print("Original array:")
    print(array1)

    increase = True
    heapSort(array1, increase)

    print("Sorted array (increasing):")
    print(array1)

    decrease = not increase
    heapSort(array2, decrease)

    print("Sorted array (decreasing):")
    print(array2)
