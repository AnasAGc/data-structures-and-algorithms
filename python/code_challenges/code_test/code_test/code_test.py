from code_test.hashTable import *


# def uniq_string (str):
    
#  hash=HashTable()

#  if not str :
#    return False

#  for i in str:
#     i=i.lower()
#     if i == " ":
#         continue
#     if hash.contains(i):
#         return False
#     hash.add(i,i)

#  return True









def string (str):
 remove=[".","!"]
 hash=HashTable()
 mostcommin=['a',1]
 if not str :
   return False

 str=str.split(' ')

 for i in str:
    i=i.lower()
    
    if i in " ":
        continue
    
    for x in i:
        if x in remove:
            i.replace(x,'')

    if hash.contains(i):

        newval= hash.find(i)+1
        hash.update(i,newval)

        if mostcommin[1]<=newval:
            mostcommin[0]=i
            mostcommin[1]=newval
    else:
        hash.add(i,1)

 return mostcommin[0]


print(string("No. not. Try Do or do not.There is try."))