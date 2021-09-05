from hashmap_repeated_word.linklist import *



class HashTable:

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] *self.size



    def get_buckets(self):
        return self._buckets

    def hash(self,key:str)->int:
        """
        This function take an string and return index that represent where should the value be in the array
        Arg:string
        return: number that represent index
        """
        value=0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size
        return index


    def add(self,key,value):
        '''add a value to the hashtable by its key
            parameters:
                key: a string
                value: any type
            Arrgument: key and value
            return: nothing
        '''

        index = self.hash(key)

        if not self._buckets[index]:
         self._buckets[index] = LinkedList()


        self._buckets[index].append([key,value])



    def find(self,key):
        """this function will search in the hashtable about the key and return the value
        parameters:
        key: a string
        return: the value
        """
        index = self.hash(key)
        if self._buckets[index]:
            cuurrent=self._buckets[index].head
            while cuurrent:
                if cuurrent.value[0]==key:
                    print(cuurrent.value[1])
                    return cuurrent.value[1]
                cuurrent=cuurrent.next
        else:
            return None




    def contains(self,key):
        """this function will check if the there is a value for the key
        parameters:
        key: a string
        return: a boolean
        """
        index=self.hash(key)
        if self._buckets[index]:
         return self._buckets[index].includes(key)
        else:
            return False



    # return self._buckets[index].includes([key,value])



def repeted_word(sentance):
    arr=sentance.lower().split(" ")
    hash=HashTable()
    for  i in arr:
        if hash.contains(i):
            return (i, len(arr))
        hash.add(i,i)
    return "None"