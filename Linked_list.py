class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        to_print = '['
        curr=self.head
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr=curr.next
        to_print= to_print[:-2]
        to_print += ']'
        if to_print:
            return to_print
        return '[]'

    def append_val(self, x):
        """ Add x to the end of the list """
        if not isinstance(x, Node):  #Convering to a node if needed
            x= Node(x)
        if self.head == None:
            self.head = x
        else:
            self.tail.next = x
        self.tail=x

    def add_to_start(self, x):
        if not isinstance(x, Node):
            x= Node(x)
        if self.head == None:
            self.head = x
        else:
            x.next = self.head
            self.head =x

    def search_val(self, x):
        index=0
        indecies =[]
        curr = self.head
        while curr  is not None:
            if curr.data == x:
                indecies.append(index)
            curr = curr.next
            index += 1
        return indecies

    def remove_val_by_index(self, x):

        if self.head == None:
            return "It cant be removed"
        else:
            curr =self.head
            previous = curr
            index = 0
            for index in range(x):
                previous = curr
                curr= curr.next
                index += 1
            previous.next = curr.next

    def length(self):
        if self.head == None:
            print("The linked list is empty")
        else:
            length=0
            curr = self.head
            while curr is not None:
                curr = curr.next
                length += 1
            print(length )


    def reverse_list_recur(self, current, previous):
        if self.head== None:
            return
        elif current.next == None:
            self.tail=self.head
            current.next = previous
            self.head = current
        else:
            next = current.next
            current.next = previous
            reverse_list_recur(next, current)





node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
print(node1)
myLinkedList= LinkedList()

myLinkedList.append_val(node1)
myLinkedList.append_val(node2)
myLinkedList.append_val(node3)
myLinkedList.append_val(node4)
myLinkedList.append_val(5)

print(myLinkedList)
myLinkedList.add_to_start(6)
print(myLinkedList)

print(myLinkedList.search_val(4))
myLinkedList.length()
myLinkedList.remove_val_by_index(2)
print(myLinkedList)
myLinkedList.length()
