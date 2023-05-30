class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Create an instance of MyLinkedList
my_list = MyLinkedList()

userInput = int(input('How many values you want in your LinkedList:'))

for i in range(userInput):
    value = int(input('Enter the value to be inserted into the LinkedList:')) 
    my_list.insert(value)

# Print the values in the linked list
print("Values in the linked list:")
my_list.print_list()
