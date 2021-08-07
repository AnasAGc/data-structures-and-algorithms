class Node(object):
    def __init__(self, data:int):
        self.data = data
        self.next = None
 
 
class LinkedList(object):
    def __init__(self):
        self.head = None
         
    def push(self, new_data:int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
         
    def printList(self):
        temp = self.head
        strain=''
        while temp != None:
            strain+=f"{temp.data} -> "
            temp = temp.next
        strain+="None"
        return strain
             
 
    def zip_list(self, p, q):
        list1 = p.head
        list2 = q.head
 
        # swap their postions until one finishes off
        while list1 != None and list2 != None:
 
            list1_next = list1.next
            list2_next = list2.next
 
            list2.next = list1_next  
            list1.next = list2 
 
            list1 = list1_next
            list2 = list2_next
            q.head = list2

            


if __name__=="__main__":
    linklist1=LinkedList()
    linklist1.push(1)
    linklist1.push(2)
    linklist1.push(3)
    linklist2=LinkedList()
    linklist2.push(4)
    linklist2.push(5)
    linklist1.zip_list(linklist1,linklist2)
    print(linklist1.printList())
