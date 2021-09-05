from hashmap_repeated_word import __version__
import pytest 

def test_version():
    assert __version__ == '0.1.0'


from hashmap_repeated_word.hashmap_repeated_word import *


@pytest.fixture
def test_hashtable():
    test=HashTable()
    test.add("anas",4444)
    test.add("roaa",5555)
    return test


def test_add():
  test=HashTable()
  test.add('ahmad',555)
  assert test.contains('ahmad')==True

def test_hash():
  test=HashTable()
  assert  test.hash("abdullah")==683

def test_find(test_hashtable):
    test=test_hashtable
    assert test.find("anas") == 4444
    assert test.find("roaa")==5555


def test_not_find(test_hashtable):
    test=test_hashtable
    assert test.find("test") == None

def test_contains(test_hashtable):
    test=test_hashtable
    assert test.contains("anas")
    assert test.contains("roaa")

def test_collision():
    test=HashTable(3)
    test.add("abdullah",4444)
    test.add("abd",5555)
    assert test.find("abd")==5555

def test_collision2(test_hashtable):
    test=test_hashtable
    test.add("40",4444)
    test.add("31",5555)
    assert test.find("31")==5555


def test_repeted_Word():
    assert repeted_word("welcome to jordan and welcome again")[0]== "welcome"

def test_number_of_word_in_string():
    test=HashTable()
    assert repeted_word("welcome to jordan and welcome again")[1]== 6

def test_no_repeted_Word():
    test=HashTable()
    assert repeted_word("welcome to jordan and  again")== "None"
