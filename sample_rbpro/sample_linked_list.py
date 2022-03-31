# A simple Python program for traversal of a linked list
class Node:
	# Function to initialise the node object
	# its like an constructor mathod, while creating instance of the class need to pass required parameters
	def __init__(self, data=0):
		self.data = data # Assign data
		self.next = None # Initialize next as null

class LinkedList:
	# Function to initialize head
	def __init__(self):
		self.head = None
	# This function prints contents of linked list
	# starting from head
	def printList(self):
		temp = self.head
		while (temp):
			print (temp.data)
			temp = temp.next

def main():
    llist = LinkedList()
    llist.head = Node(11111111)
    second = Node(2222)
    third = Node(3)
    llist.head.next = second # Link first node with second
    second.next = third # Link second node with the third node
    llist.printList()

# Code execution starts here
if __name__=='__main__':
    main()
	
