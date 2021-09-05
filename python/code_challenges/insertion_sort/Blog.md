# Quick Sort

Quick sort is similar to merge sort, in that it's a conquer and divide style sorting algorythm. It chooses a pivot value and partitions the input array into a left and right array.


## Pseudocode

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp


```
## Trace

Sample Array: [10,80,30,90,40,50,70]



### Pass 1:


![first](./blog/10.jpg)

### Pass 2:


![second](./blog/11.jpg)

### Pass 3:


![third](./blog/12.jpg)



### Pass 4:


![fourth](./blog/13.jpg)

### Pass 5:



![fifth](./blog/14.jpg)

### pass 6

![fifth](./blog/15.jpg)

### pass 7
![fifth](./blog/16.jpg)

### pass 8

![fifth](./blog/17.jpg)




## Efficency

### Time: O(n^2)

### Space: O(1)

# Mergesort
### merge sort (also commonly spelled as mergesort) is an efficient, general-purpose, and comparison-based sorting algorithm. 
### Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.


```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left


```

## Trace


![Mearge_Sort](linked-list-insertions-append.jpg)


## big O 
### Time: O(nlog(n))

### Space: O(n)

