#include <iostream>

void printArray(int A[], int size)
{
    for (int ii=0; ii < size; ii++)
        printf("%d ", A[ii]);
    printf("\n");
}

void merge(int arr[], int left, int right)
{
    int mid = (right - left) / 2 + left;
    int leftSize = mid - left + 1;
    int rightSize = right - mid;
    int leftArr[leftSize];
    int rightArr[rightSize];
    
    std::copy(arr + left, arr + left + leftSize, leftArr);
    std::copy(arr + left + leftSize, arr + left + leftSize + rightSize, rightArr);
    int ll = 0, rr = 0, arrIdx = left;
    while(ll < leftSize && rr < rightSize){
        if(leftArr[ll] <= rightArr[rr]){
            arr[arrIdx] = leftArr[ll];
            ll++;
        }
        else{
            arr[arrIdx] = rightArr[rr];
            rr++;
        }
        arrIdx++;
    }
    
    while(ll < leftSize){
        arr[arrIdx] = leftArr[ll];
        ll++;
        arrIdx++;
    }
    while(rr < rightSize){
        arr[arrIdx] = rightArr[rr];
        rr++;
        arrIdx++;
    }
}

void mergeSort(int arr[], int leftIdx, int rightIdx)
{
    if(leftIdx >= rightIdx){
        return;
    }
    int midIdx = (rightIdx - leftIdx) / 2 + leftIdx;
    mergeSort(arr, leftIdx, midIdx);
    mergeSort(arr, midIdx + 1, rightIdx);
    merge(arr, leftIdx, rightIdx);
}
 
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);
 
    printf("Original array:\n");
    printArray(arr, arr_size);
 
    mergeSort(arr, 0, arr_size - 1);
 
    printf("\nSorted array:\n");
    printArray(arr, arr_size);
    return 0;
}

