class Node():
    def __init__(self,value=None) -> None:
        """This Function Creates Nodes """
        self.value=value
        self.next=None



class Stack():
    def __init__(self,node=None) -> None:
        self.top=node
        self.counter=0

    def push(self,value=None):
        """ Adding New value by assign it to head """
        try:
            node=Node(value)
            node.next=self.top
            self.top=node
        except:
            raise Exception('Something went wrong ')

    def pop(self):
        """ Remove Node From The stack  and Return it """
        try:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp.value
        except:
            raise Exception('The Stake Is empty ')
    
    def is_empty(self):
        """Check if the Stack is Empty  or Not """
        return not self.top

    def peek(self):
        """ Return the Top value  """
        try:
         return self.top.value
        except:
         raise Exception('The stack is Empty')

    def __str__(self) -> str:
        strain=""
        while self.top:
            strain+=f'{self.top.value}-->'
            self.top=self.top.next
        strain+="None"
        return strain
        
    


class Queue():
    def __init__(self) -> None:
        """Create Queue with None Front and Rear """
        self.front=None
        self.rear=None
    
    def enqueue(self,value):
        """Add Node to The Queue """
        node=Node(value)
        if not self.front and not self.rear:
            self.front=node
            self.rear=node

        else:    
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        """ Return the Front Node From the Queue and Remove it """
        try:
            temp=self.front
            self.front=self.front.next
            temp.next=None

            if self.front==None:
                 self.rear=None

            return temp.value
        except:
            raise Exception("The Queue is empty")

    def peek(self):
        """ Return the Front Value Without Removing it  """
        try:
         return self.front.value
        except:
         raise Exception("The Queue is empty")

    def is_empty(self):
        """ Checks if the Function it Empty of Not """
        if  self.front or self.rear:
            return False
        else:
            print("ss")
            return True

    def __str__(self) -> str:
        strain=""
        while self.front:
            strain+=f'{self.front.value}-->'
            self.front=self.front.next
        strain+="None"
        return strain
    

class PseudoQueue:
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def enqueue(self, item):
        self.pushStack.push(item)

    def dequeue(self):
        if self.popStack.is_empty():
            while self.pushStack.top != None:
                print('ssss')
                self.popStack.push(self.pushStack.top.value)
                self.pushStack.top=self.pushStack.top.next
            
        return self.popStack.pop()

    
                    
            


if __name__=="__main__":
<<<<<<< HEAD:python/code_challenges/stack_and_queue/stack_and_queue/stack_and_queue.py
 test=Stack()

 test.push(2)
 test.push(1)
 test.push(2)
 test.push(3)
#  test.dequeue()
#  test.dequeue()
#  test.dequeue()
 
 print(test)
=======
 test=PseudoQueue()

 test.enqueue(7)
 test.enqueue(1)
 test.enqueue(2)
 test.enqueue(5)

#  test.dequeue()
 
 print(test.dequeue())
 print(test.dequeue())
 print(test.dequeue())
 print(test.dequeue())
>>>>>>> 4138cf2110a2a9ba109c55477dc6718b836ad747:python/code_challenges/stack-queue-pseudo/stack_and_queue/stack_and_queue.py

 
