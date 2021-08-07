from linked_list_zip import __version__
from linked_list_zip.linked_list_zip import *

def test_version():
    assert __version__ == '0.1.0'

def test_zip_two_list():
    linklist1=LinkedList()
    linklist1.push(1)
    linklist1.push(2)
    linklist1.push(3)
    linklist2=LinkedList()
    linklist2.push(4)
    linklist2.push(5)
    linklist2.push(6)
    linklist1.zip_list(linklist1,linklist2)
    actual=linklist1.printList()
    expected='3 -> 6 -> 2 -> 5 -> 1 -> 4 -> None'
    assert actual==expected


def test_zip_two_list():
    linklist1=LinkedList()
    linklist1.push(1)
    linklist1.push(2)
    linklist1.push(3)
    linklist2=LinkedList()
    linklist2.push(4)
    linklist2.push(5)
    linklist2.push(6)
    linklist1.zip_list(linklist1,linklist2)
    actual=linklist1.printList()
    expected='3 -> 6 -> 2 -> 5 -> 1 -> 4 -> None'
    assert actual==expected

def test_zip_two_list_first_less():
    linklist1=LinkedList()
    linklist1.push(1)
    linklist1.push(3)
    linklist2=LinkedList()
    linklist2.push(4)
    linklist2.push(5)
    linklist2.push(6)
    linklist1.zip_list(linklist1,linklist2)
    actual=linklist1.printList()
    expected='3 -> 6 -> 1 -> 5 -> None'
    assert actual==expected



def test_zip_two_list_second_less():
    linklist1=LinkedList()
    linklist1.push(1)
    linklist1.push(2)
    linklist1.push(3)
    linklist2=LinkedList()
    linklist2.push(4)
    linklist2.push(5)
    linklist1.zip_list(linklist1,linklist2)
    actual=linklist1.printList()
    expected='3 -> 5 -> 2 -> 4 -> 1 -> None'
    assert actual==expected