class Node():
    def __init__(self,value=None) -> None:
        """This Function Creates Nodes """
        self.value=value
        self.next=None



class Stack():
    def __init__(self,node=None) -> None:
        self.top=node

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
    
    def __str__(self):
        str=""
        while self.front:
            str+=f"{self.front.value} --> "
            self.front=self.front.next
        str+="None" 
        return(str)
        

open_list = ["[","{","("]
close_list = ["]","}",")"]
  
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return True
    else:
        return False
  
  




    

if __name__=="__main__":
    string = "{[]{()}}"
    print(string,"-", check(string))
    
    string = "[{}{})(]"
    print(string,"-", check(string))
    
    string = "((()"
    print(string,"-",check(string))


 
 
