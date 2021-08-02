
class Node:
  ''''
  THis the class is responsiple to create the Nodes 
  '''
  def __init__(self, value=""):
    self.value = value
    self.next = None

  def __add__(self, other):
    return Node(self.value + other.value)

  # def __str__(self,value) -> str:
  #     return value


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
    print(node)
    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
         print(current.value)
         if vlaue ==current.value:
            return True
         current=current.next
     return False

  def append(self,value):
    current=Node(value)
    last=self.head
    while current:
     
     if last.next==None:
       last.next=current
       break
     last=last.next

  # def insert_before(self,old,value):
  #   current=Node(old)
  #   last=self.head
  #   temp=last.next
    # if str(current)==str(last):
    #   self.insert(value)
    #   return
      
  #   while last.next:
    
  #     if str(current)==str(temp):
  #       last.next=Node(value)
  #       last=last.next
  #       last.next=temp

  #     last=last.next
  #     temp=last.next

  def insert_before(self,flage,new_value):
    head=self.head
    nextv=self.head
    node=Node(new_value)
    if str(flage)==str(self.head):
      self.insert(new_value)
      return
    while flage!=nextv.value:
        print('aaaaaaaaaaaaaaaaaaaaa')
        head=nextv
        nextv=nextv.next
    head.next=node
    node.next=nextv

  
      




  def insert_after(self,old_value,value):
    node=Node(value)
    current=self.head
    temp=self.head
    while current.next!=None:
      if current.value==old_value:
        temp=temp.next
        current.next=node
        current=current.next
        current.next=temp
        return
      current=current.next
      temp=temp.next
    self.append(value)
      
  def __len__(self):
    counter = 0
    current = self.head
    while current:
      counter += 1
      current = current.next
    return counter      



    

 
    


  def __str__(self):
    string = ""
    current = self.head
    while current:
      string += f"{str(current.value)} -> "
      print(current.next)
      current = current.next
    string += "None"
    return string

  def __iter__(self):
    # new_list = []
    current = self.head
    while current:
      yield current.value
      current = current.next
    # return new_list

  def __repr__(self):

    return "LinkedList()"
  

  def kthFromEnd(self,num):
      num1=len(self)-1
      if num1<num:
          return ("out of range")
      num_of_loop=(len(self)-num)-1
      current=self.head
      while num_of_loop >0 :
        #   print(num_of_loop)
          current=current.next
          num_of_loop -=1
      return current.value








if __name__ == "__main__":
  ll = LinkedList()
  test_node=Node(5)
  ll.insert(167)
  ll.insert(168)
  ll.insert(54)
  ll.insert(55)
  ll.insert(3)
  ll.append(33)
  ll.append(77)

  ll.insert_before(3,555555555555555)

  print(ll)
#   ll.insert(71)
