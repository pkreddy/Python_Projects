class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def deleteFirst(self):
		self.head = self.head.next
		self.size = self.size - 1
	
	def deleteLast(self):
		node = self.head
		while node.next.next != None:
			node = node.next
		node.next = None
		self.size = self.size - 1
	
	def deleteAt(self,position):
		node = self.head
		if position > self.size:
			print('cannot be deleted since size is',self.size,'which is less than the given position',position)
		else:
			if(position == 1):
				self.deleteFirst()
			else:
				self.size = self.size - 1
				for i in range(1,position-1,1):
					node = node.next
				node.next = node.next.next
				
	def addToFirst(self,data):
		node = Node(data)
		self.size = self.size + 1
		if self.head == None:
			self.head = node
		else:
			temp = self.head
			self.head = node
			self.head.next = temp
	
	def addToLast(self,data):
		self.size = self.size + 1
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			node_traverse = self.head
			while node_traverse.next != None:
				node_traverse = node_traverse.next
			node_traverse.next = node
	
	def insertAt(self,data,position):
		node = self.head
		if position > self.size:
			print("cannot insert in linkedlist since the size is",self.size,"but position to insert at is",position)
		else:
			if position == 1:
				self.addToFirst(data)
			else:
				self.size = self.size + 1
				for i in range(1,position-1,1):
					node = node.next
				data_node = Node(data)
				temp = node.next
				node.next = data_node
				data_node.next= temp
		
	def traverse(self):
		node = self.head #start from head node
		while node != None:
			print(node.val) #prints the node value
			node = node.next #move to the next node

'''
node1 = Node(12)
node2 = Node(14)
node3 = Node(16)
node1.next = node2
node2.next = node3

node1.traverse()
'''

l = LinkedList()
l.addToFirst(1)
l.addToFirst(2)
l.addToFirst(3)
l.addToFirst(4)
l.addToFirst(5)
l.addToLast(0)
l.insertAt(10,5)
l.deleteFirst()
l.deleteFirst()
l.deleteLast()
l.deleteAt(5)
print("size is",l.size)
l.traverse()

#print(l.head.val)