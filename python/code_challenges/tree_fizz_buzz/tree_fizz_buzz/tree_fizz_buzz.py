import copy

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []


class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
      
        if self.is_empty():
            self.front=value
            self.rear=value
        self.rear.next=value
        self.rear=value

    def dequeue(self):
        if self.is_empty():
            raise Exception("empty equeue")
        if self.front==self.rear:
            temp=self.front
            self.front=None
            self.rear=None
            return temp.value
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value

    def peek(self):
       if self.is_empty():
           raise Exception("empty equeue")
       return self.front.value


    def is_empty(self):
     return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter


class k_ary_tree:
    def __init__(self):
        self.root = None


def fizz_buzz_tree(k_array):
   try:
     
        copy_root=copy.deepcopy(k_array)
        temp=Queue()
        temp.enqueue(copy_root.root)
        print(temp.front.value)

        while temp.front:

            [temp.enqueue(i) for i in temp.front.children if temp.front.children]

            if (temp.front.value % 3 == 0 and temp.front.value % 5 == 0):
                temp.front.value='FizzBuzz'

            elif temp.front.value % 3 == 0:
                temp.front.value='Fizz'

            elif temp.front.value % 5 == 0:
                temp.front.value='Buzz'   
                
            temp.dequeue()
            
        return copy_root
        
   except:
        raise ValueError('Empty Root')

     



if __name__ == "__main__":
    
    tree = k_ary_tree()
    tree.root = Node(3)

    tree.root.children.append(Node(2))
    tree.root.children.append(Node(5))
    tree.root.children.append(Node(15))

    tree.root.children[0].children.append(Node(4))
    tree.root.children[0].children.append(Node(6))
    tree.root.children[0].children.append(Node(7))

    tree.root.children[1].children.append(Node(9))
    tree.root.children[1].children.append(Node(18))
    tree.root.children[2].children.append(Node(45))
    new_tree =  fizz_buzz_tree(tree)

    # print(new_tree.root.children[1].children[1].value)
    print(new_tree.root.value)

    # print(dir([]))
    # a = new_tree.__init__()
    # print(a)


#               Input (k_arr_tree)


#                      3 
#                ______|______
#               /      |      \
#              /       |       \
#             2        5        15
#           / | \     / \        \
#          4  6  7   9   18       45 
#                   Output 


#                      F
#                ______|______
#               /      |      \
#              /       |       \
#             2        B        FB
#           / | \     / \        \
#          4  F  7   F   F       FB 

#     FB =>  FizzBuzz F => Fizz , B => Buzz