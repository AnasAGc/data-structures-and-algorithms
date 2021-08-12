from stack_queue_animal_shelter.stack_queue_animal_shelter import *
from stack_queue_animal_shelter import __version__
import pytest

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def data():

    shelter1=Animal_Shelter()

    fafy=Dog("fafy")
    flafl=Dog('flafl')
    flfol=Dog('flfol')

    zozo=Cat("zozo")
    zain=Cat("zain")
    zzzozo=Cat("zzzozo")

    shelter1.enqueue(fafy)
    shelter1.enqueue(flafl)
    shelter1.enqueue(flfol)
    shelter1.enqueue(zozo)
    shelter1.enqueue(zain)
    shelter1.enqueue(zzzozo)

    return shelter1



def test_create_shelter():
    assert Animal_Shelter()


def test_enqueue_values(data):
    """ check the head values  """

    actual=data.dogs.front.value.name
    actual2=data.cats.front.value.name
    expected="fafy"
    expected2="zozo"

    assert actual==expected
    assert actual2==expected2

def test_dequeue_values(data):
    """ check the Returnd value  """

    actual=data.dequeue("dog")
    actual2=data.dequeue("cat")
    expected="fafy"
    expected2="zozo"

    assert actual.name==expected
    assert actual2.name==expected2


def test_null_case(data):
    """ check if we enter dummt data """
    actual=data.dequeue("horse")
    expected=None
    assert actual==expected










# def test_stack_pushing_one_element(data):
#     data['stack'].push(1)
#     actuall=data['stack'].top.value
#     expected=1
#     assert actuall==expected

# def test_stack_pop_one_element(data):
#     data['stack'].push(1)
#     data['stack'].push(2)
#     actual = data['stack'].pop()
#     expected = 2
#     assert expected == actual

# def test_stack_is_empty():
#   # create a stack 
#   stack = Stack()
#   assert stack.is_empty()

# def test_stack_is_not_empty():
#   # create an empty stack
#   stack = Stack()
#   # push an item onto the stack
#   stack.top = Node(1)
#   # assert that the stack is not empty
#   assert not stack.is_empty()

# def test_peek_empty_stack_raises_exception():
#   check_stack = Stack()
#   with pytest.raises(Exception, match ="The stack is Empty" ):
#     check_stack.peek()


# @pytest.fixture
# def data2():
#     new_queue=Queue()
#     new_queue.enqueue(1)
#     new_queue.enqueue(2)
#     new_queue.enqueue(3)
#     new_queue.enqueue(5)
#     return new_queue
    
# def test_enqueue_one_element(data2):
   
#     actual=data2.front.value
#     expected=1
#     assert expected==actual

# def test_enqueue_multi_elements(data2):
    
#     actual=data2.front.value
#     expected=1
#     actual2=data2.rear.value
#     expected2=5
#     assert actual==expected
#     assert actual2==expected2

# def test_dequeue_one_element(data2):
#     actual=data2.dequeue()
#     expected=1
#     assert actual==expected

# def test_peek_one_element(data2):
#     actual=data2.peek()
#     expected=1
#     assert expected==actual

# def test_queue_is_empty_after_dequeue(data2):
#     data2.dequeue()
#     data2.dequeue()
#     data2.dequeue()
#     data2.dequeue()
#     assert data2.is_empty()

# def test_empty_queue():
#     assert Queue()

# def test_empty_queue_rasie_exception():
#     new_queue=Queue()
#     with pytest.raises(Exception,match="The Queue is empty"):
#         new_queue.peek()
   

# def test_empty_queue_rasie_exception_dequeue():
#     new_queue=Queue()
#     with pytest.raises(Exception,match="The Queue is empty"):
#         new_queue.dequeue()