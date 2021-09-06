
from hashmap_tree_intersection.linked_list import *
from hashmap_tree_intersection.trees import *

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



def hash_map_tree_intersection(tree1,tree2):
    arr=[]
    # arr=tree1.in_order(tree1.root)
    print(tree1.root)
    arr1=tree2.in_order(tree2.root)
    # print(arr)
    hash=HashTable()
    print(tree1.root.value)
    def convert_tree_to_hash(root):

            if root.left:
                convert_tree_to_hash(root.left)

            hash.add(str(root.value),str(root.value))
            print("x")

            if root.right:
                convert_tree_to_hash(root.right)


    convert_tree_to_hash(tree1.root)

    for i in arr1:
        if hash.contains(str(i)):
            arr.append(i)
    return arr



tree1=BinaryTree()
root1=Node(100)
root1.left=Node(200)
root1.left.left=Node(300)
root1.left.right=Node(400)
root1.right=Node(500)
root1.right.left=Node(600)
tree1.root=root1

tree2=BinaryTree()
root=Node(100)
root.left=Node(500)
root.left.left=Node(1000)
root.left.right=Node(600)
root.right=Node(687)
root.right.left=Node(7689)
root.right.left.left=Node(300)

tree2.root=root
# print(tree1.in_order(root1))
print(hash_map_tree_intersection(tree1,tree2))