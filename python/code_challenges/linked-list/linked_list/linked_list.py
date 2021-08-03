
from typing import Counter


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
    # print(node)
    if self.head:
      node.next = self.head

    self.head = node

  def includes(self,vlaue):
     current=self.head
     while current :
        #  print(current.value)
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
      # print(current.next)
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


# def zipLists(list1, list2):
#   head_L1=list1.head
#   next_l1=head_L1.next
#   head_L2=list2.head
#   next_l2=head_L2.next
#   conter=3
#   for i in range(10):
#      head_L1.next=head_L2
#      head_L2.next=next_l1
#      next_l1.next=next_l2
#     #  next_l2.next=

#   print(list1)
   

def zipLists(list1, list2):
    current1 = list1.head
    current2 = list2.head
    if current1 == None or current2 == None:
        if current1:
            return list1.__str__()
        elif current2:
            return list2.__str__()
        else:
         return "Linked lists are both Empty "
    zip_list = []
    while current1 or current2:
        if(current1):
            zip_list+=[current1.value]
            current1 = current1.next
        if(current2):
            zip_list+=[current2.value]
            current2 = current2.next
    insertion_values=''
    for item in zip_list:
      insertion_values+=f'{item}-> '
    insertion_values+='None'
    return insertion_values




if __name__ == "__main__":
  ll = LinkedList()
  test_node=Node(5)
  ss=LinkedList()
  ll.insert(167)
  ll.insert(168)
  ll.insert(54)
  ll.insert(55)
  ll.insert(3)
  ss.insert(555)
  ss.insert(1)
  ss.insert(2)
  ss.insert(3)
  # print(ll)
  # print(ll)
  # print(ss)
  print(  zipLists(ss,ll))
  # ll.insert_before(3,555555555555555)

  # print(f'{ll.head} if the Length')
#   ll.insert(71)
