from  hashmap_left_join.hashTable import *

def hashmap_left_join(hash1,hash2):

    '''
    Return list of lists with word , synonym and antonyms

    Function loops inside first hashtable buckets,
    and check if the words has antonyms in the Second hashtable 


    Parameters : Hashtable
     hash1: Hashtable
     hash2: Hashtable


    Return : List of strings =>  [ [Word,synonym,antonyms], [Word,synonym,antonyms]]

    '''
    buckets=hash1.get_buckets()
    arr=[]
    for i in buckets:
        if i:
            current=i.head
            while current:
                x=hash2.find(current.value[0])
                if not x:
                    x='Null'
                current.value.append(x)
                arr.append(current.value)
                current=current.next
    return arr

