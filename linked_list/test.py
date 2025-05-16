import pytest
from node import Node
from linked_list import LinkedList


def test_node():
    x = Node(1)
    assert x.value == 1
    assert x.next == None


class TestAppend:

    def test_append_normal(self, normal_list):
        normal_list.append(3)
        assert normal_list.tail.value == 3
        assert normal_list.length == 3

class TestPop:
    
    def test_pop_normal(self, normal_list):
        value = normal_list.pop().value
        assert value == 2
        assert normal_list.length == 1

    def test_pop_singleton(self, singleton_list):
        singleton_list.pop()
        assert singleton_list.head == None
        assert singleton_list.tail == None
        assert singleton_list.length == 0

    def test_pop_empty(self, empty_list):
        assert empty_list.head == empty_list.tail
        

class TestPrepend:
    
    def test_prepend_normal(self, normal_list):
        normal_list.prepend(0)
        assert normal_list.head.value == 0
        assert normal_list.length == 3
    
    def test_prepend_empty(self, empty_list):
        # empty_list.print_list()
        empty_list.prepend(1)
        # empty_list.print_list()

        assert empty_list.head == empty_list.tail
        assert empty_list.length == 1

class TestPopFirst:
    
    def test_pop_first_normal(self, normal_list):
        normal_list.pop_first()
        assert normal_list.head.value == 2
        assert normal_list.length == 1
    
    def test_pop_first_singleton(self, singleton_list):
        singleton_list.pop_first()
        assert singleton_list.head == None
        assert singleton_list.tail == None
        assert singleton_list.length == 0
    
    def test_pop_first_empty(self, empty_list):
        assert empty_list.head == empty_list.tail

class TestGet:
    
    def test_get_normal(self, normal_list):
        assert normal_list.get(0).value == 1

    def test_get_out_of_bounds(self, normal_list):
        assert normal_list.get(-1) == None
        assert normal_list.get(10) == None

class TestSetValue:
    
    def test_set_value_normal(self, normal_list):
        normal_list.set_value(0, 3)
        assert normal_list.head.value == 3
    
    def test_set_value_out_of_bounds(self, normal_list):
        assert normal_list.set_value(10, 9) == False
        assert normal_list.set_value(-1, 0) == False


class TestInsert:

    def test_insert_middle(self, normal_list):
        assert normal_list.insert(1, 5) == True
        assert normal_list.length == 3
        normal_list.print_list()
        assert normal_list.head.next.value == 5

    def test_insert_start(self, normal_list):
        assert normal_list.insert(0, 5) == True
        assert normal_list.length == 3
        assert normal_list.head.value == 5
    
    def test_insert_end(self, normal_list):
        assert normal_list.insert(2, 5) == True
        assert normal_list.length == 3
        assert normal_list.tail.value == 5
    
    def test_insert_out_of_bounds(self, normal_list):
        assert normal_list.insert(10, 9) == False
        assert normal_list.insert(-1, 0) == False

class TestRemove:

    def test_remove_middle(self, normal_list):
        normal_list.prepend(0)
        assert normal_list.remove(1).value == 1
        assert normal_list.length == 2
        assert normal_list.head.value == 0
        assert normal_list.tail.value == 2

        
    def test_remove_start(self, normal_list):
        assert normal_list.remove(0).value == 1 
        assert normal_list.length == 1
        assert normal_list.head.value == 2
    
    def test_remove_end(self, normal_list):
        assert normal_list.remove(1).value == 2
        assert normal_list.length == 1
        assert normal_list.tail.value == 1
    
    def test_remove_out_of_bounds(self, normal_list):
        assert normal_list.remove(10) == False
        assert normal_list.remove(-1) == False

    
@pytest.fixture()
def singleton_list():
    return(LinkedList(1))

@pytest.fixture()
def empty_list(singleton_list):
    singleton_list.head = None
    singleton_list.tail = None
    singleton_list.length = 0
    return singleton_list

@pytest.fixture()
def normal_list(singleton_list):
    tmp = Node(2)
    singleton_list.head.next = tmp
    singleton_list.tail = tmp
    singleton_list.length += 1
    return singleton_list


        