from hashtables.linked_list import *

class HashTable:

    def __init__(self, size = 1024):
        self.size = size
        self._buckets = [None] *self.size



    def hash(self,key:str)->int:
        '''
        Return hased index 
         
         Take Key and Convert it from to index 

        parameters: 
         Key -> string 
        return:
         index -> Number 

        '''

        value=0
        for x in key:
            value += ord(x)
        index = (value * 7) % self.size
        return index


    def add(self,key,value):
        '''
    add a value to the hashtable by its key
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



    def find(self,key:str):
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




    def contains(self,key:str):
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


    def get_buckets(self):
        '''Return Hashtable Buckets 
        

        parameters: None 
        Return: List 
        
         '''
        return self._buckets

def hashmap_left_join(hash1,hash2):
    
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


h1=HashTable(10)
h2=HashTable(10)

h1.add("a1","A1")
h1.add("c1","C1")

h1.add("b1","B1")

h2.add("a1","A2")
h2.add("b1","B2")
h2.add("D1","B2")



one = HashTable()
one.add('pond', 'enamored')
one.add('rath', 'anger')
one.add('adiligent', 'employed')
one.add('poutfit', 'garb')
one.add('hangguide', 'usher')

two = HashTable()
two.add('fond', 'averse')
two.add('wrath', 'delight')
two.add('diligent', 'idle')
two.add('guide', 'follow')
two.add('flow', 'jam')

print(hashmap_left_join(one,two))
