
def  mergesort(arr):
    n=len(arr)

    if n > 1:
       mid =int(n/2)
       left =arr[0:mid]
       right =arr[mid:n]
    #    sort the left side
       mergesort(left)
    #    sort the right side
       mergesort(right)
    #    merge the sorted left and right sides together
       merge(left, right, arr)



def merge(left, right, arr):
     i =0
     j =0
     k =0

     while i < len(left) and j < len(right):
         if left[i] <= right[j]:
            arr[k] =left[i]
            i =i + 1
         else:
            arr[k] =right[j]
            j =j + 1

         k =k + 1

     if i == len(left):
            arr[k]=right[j]
     else:
            arr[k]=left[i]


arr=[8,4,23,42,16,15]
mergesort(arr)
print(arr)