def selection_sort(arr:list)->list:
    ''' sort the list  '''
    newarr=[]
    for i in range(len(arr)-1):
        min=i
        for j in range (i+1,len(arr)):
            if arr[j] <arr[i]:
                min=j
            


        temp=arr[min]

        arr[min]=arr[i]
        arr[i]=temp
        
        


def remove_duplcates(arr):
    newarr=[]
    for i in arr:

        if i in newarr:
           continue

        else:
            newarr.append(i)
    
    return(newarr)





def reversed_insertion_sort(my_list):
    new_list=[]
    while my_list:
        min = my_list[0]  
        for x in my_list: 
            if x > min:
                min = x
        new_list.append(min)
        my_list.remove(min)    

    return(new_list)

[8,4,23,42,16,15]

def insertionSort(arr):
    
  for i in range(1,len(arr)):

    j=i-1
    temp=arr[i] # 16

    while j >=0 and temp < arr[j]: # 2>0 and 16 < 23 
      arr[j+1]=arr[j]
      j=j-1
      
    arr[j + 1] =temp # 
    
  arr=remove_duplcates(arr)
  return arr


print(insertionSort([7,8,9,0,4,2]))