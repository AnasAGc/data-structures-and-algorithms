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

def test_linkedlist():
   assert LinkedList()

def test_insert():
  # arrange
  ll = LinkedList()
  with pytest.raises(AttributeError):
    ll.head.value
  ll.insert(51)
  actual = ll.head.value
  assert actual == 51

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

def test_add_to_last_list():

    new_linked= LinkedList()
    new_linked.insert(5)
    new_linked.append(30)
    assert new_linked.includes(30)

def test_add_many_to_last_list():
    new_linked= LinkedList()
    new_linked.insert(3)
    new_linked.append(30)
    new_linked.append(35)
    new_linked.append(40)
    assert new_linked.includes(35)

def test_add_to_middle():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_before(20,30)
    assert new_linked.includes(30)
def test_add_befor_the_first():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_before(111,30)
    assert new_linked.includes(30)
def test_add_after_middle():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_after(20,30)
    assert new_linked.includes(30)
def test_add_after_last():
    new_linked= LinkedList()
    new_linked.insert(1)
    new_linked.insert(3)
    new_linked.insert(20)
    new_linked.insert(111)
    new_linked.insert_after(1,30)
    assert new_linked.includes(30)