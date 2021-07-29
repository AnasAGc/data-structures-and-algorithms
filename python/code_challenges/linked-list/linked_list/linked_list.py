
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





if __name__ == "__main__":
  ll = LinkedList()
  test_node=Node(5)
  ll.insert(167)
  ll.insert(54)
  print(test_node)
#   ll.insert(71)
