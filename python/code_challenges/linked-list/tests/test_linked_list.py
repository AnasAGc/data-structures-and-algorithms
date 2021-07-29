import pytest
from linked_list import __version__
from linked_list.linked_list import LinkedList, Node
def test_version():
    assert __version__ == '0.1.0'

def test_create_node():
  assert Node()

def test_node_has_value():

  node = Node("Anas")
  actual = node.value
  assert actual == "Anas"


def test_node_has_next_attribute():
  node = Node("Anas")
  actual = node.next
  assert True
# test creating a linked list

def test_linkedlist():
   assert LinkedList()

# test inserting values into linked list

def test_insert():
  # arrange
  ll = LinkedList()
  with pytest.raises(AttributeError):
    ll.head.value
  ll.insert(51)
  actual = ll.head.value
  assert actual == 51
# test finding a value in linked list; found and not found

def test_fined_value_in_linked_list():
    new_linked= LinkedList()
    new_linked.insert(52)
    assert new_linked.includes(52)


def test_fined_value_in_linked_list():
    new_linked= LinkedList()
    with pytest.raises(AttributeError):
        new_linked.head.value
    new_linked.insert(52)
    assert new_linked.includes(31)==False
# test removing value from linked list