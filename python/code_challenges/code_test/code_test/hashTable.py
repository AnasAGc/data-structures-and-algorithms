
class Node:
  ''''
  THis the class is responsiple to create the Nodes
  '''
  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  def __str__(self):
    return str(self.value)


class LinkedList():

  '''
  This Class Responsable For Creating LinkdeList
  '''
  def __init__(self):
    self.head = None

  def insert(self, value):
    node = Node(value)
    # print(node)
    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
        #  print(current.value)
         if vlaue ==current.value[0]:
            return True
         current=current.next
     return False

  def append(self,value):
    new_node=Node(value)

    if self.head == None:
      self.head = new_node
    else:
      current=self.head
      while current.next:
        current=current.next
      current.next=new_node



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
        """this function will search in the hashtable about the key and update the value with the new value passed
        parameters:
        key: a string
        va: the value
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


    def update(self,key:str,newvalue):
        """this function will search in the hashtable about the key and update the value
        parameters:
        key: a string
        value: the value
        """
        
        index = self.hash(key)
        if self._buckets[index]:
            cuurrent=self._buckets[index].head
            while cuurrent:
                if cuurrent.value[0]==key:
                     cuurrent.value[1]=newvalue
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
