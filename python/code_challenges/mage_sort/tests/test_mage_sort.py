from mage_sort import __version__
from mage_sort.meregsort import *

def test_version():
    assert __version__ == '0.1.0'

def test_check_sortion():

    arr=[8,4,23,42,16,15]
    mergesort(arr)
    
    actual=arr
    expected=[4, 8, 15, 16, 23, 42] 
    
    assert  actual==expected