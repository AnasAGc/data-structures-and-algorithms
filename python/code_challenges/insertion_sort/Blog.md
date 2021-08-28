# Insertion Sort

### Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. 


## Pseudocode

```
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

```
## Trace

Sample Array: [8,4,23,42,16,15]



### Pass 1:
when i=1

![first](./blog/1.png)

### Pass 2:
when i=2

![second](./blog/2.png)

### Pass 3:
when i=3

![3th](./blog/3.png)



### Pass 4:
when i=4

![4th](./blog/4.png)

### Pass 5:
when i=5


![5th](./blog/5.png)



## Efficency

### Time: O(n^2)

### Space: O(1)
