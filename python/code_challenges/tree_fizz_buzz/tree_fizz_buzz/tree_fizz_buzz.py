import copy

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []

class k_arytree:
    def __init__(self):
        self.root = None

def fizz_buzz_tree(k_array):
    '''this function check the value of the trees and return fizz , buzz or fizz buzz based on the value  '''
   
    if not k_array.root:
        return None

    new_tree = copy.deepcopy(k_array)
    allnodes = []
    allnodes.append(new_tree.root)
    val = allnodes[0]
    
    while True:
        
        if val.children:
            allnodes += val.children
            
        if val.value % 3 == 0 and val.value % 5 == 0:
            val.value = 'FizzBuzz'

        elif val.value % 3 == 0:
            val.value = 'Fizz'

        elif val.value % 5 == 0:
            val.value = 'Buzz'

        else:
            val.value = str(val.value)

        allnodes.pop(0)

        if not allnodes:
            break

        val = allnodes[0]

    return new_tree


