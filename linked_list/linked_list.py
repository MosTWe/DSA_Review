from node import Node

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            while temp.next != None:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        temp = self.head
        if self.length <= 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None
        else:
            self.head = self.head.next
            temp.next = None
            self.length -= 1
            return temp.value
        
    def get(self, index):
        if index >= self.length or index < 0:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0 :
            return False
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            temp = self.get(index - 1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            self.print_list

        return True
            
    
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

my_linked_list = LinkedList(4)
my_linked_list.append(5)
my_linked_list.print_list()
print(my_linked_list.set_value(1,8))
my_linked_list.pop_first()
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.print_list()
my_linked_list.pop_first()
my_linked_list.print_list()
