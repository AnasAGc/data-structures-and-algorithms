from stack_and_queue.stack_and_queue import *
import pytest

def test_pseudoqueue_dequeue(data):
    assert data.dequeue() == 10
    assert data.dequeue() == 15
    assert data.dequeue() == 20
    assert data.dequeue() == 5

def test_pseudoqueue_enqueue(data):
  assert data.pushStack.top.value==5
  assert data.pushStack.top.next.value==20
  assert data.pushStack.top.next.next.value==15
  assert data.pushStack.top.next.next.next.value==10

def test_pseudoqueue_empty():
    my_queue = PseudoQueue()
    my_queue.enqueue(5)
    assert my_queue.dequeue() == 5
    

@pytest.fixture
def data():
    my_queue = PseudoQueue()
    my_queue.enqueue(10)
    my_queue.enqueue(15)
    my_queue.enqueue(20)
    my_queue.enqueue(5)
    return my_queue