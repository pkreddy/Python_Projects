class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		self.prev = None
	
class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def add(self,data):
		self.size = self.size + 1
		if self.head == None:
			self.head = Node(data)
		else:
			node = Node(data)
			node.next = self.head
			self.head = node
			self.head.next.prev  = self.head
			
	def printLL(self):
		if self.head == None:
			print("linkedlist is empty")
		else:
			node = self.head
			while(node != None):
				print(node.data)
				node = node.next
	
	def addToLast(self,data):
		self.size = self.size + 1
		if self.head == None:
			self.head = Node(data)
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			node.next = Node(data)
			node.next.prev = node
	
	def deleteFirst(self):
		if self.head == None:
			print("LinkedList empty cannot delete any node")
		else:
			self.head = self.head.next
			self.size = self.size - 1
			
	def deleteLast(self):
		if self.head == None:
			print("LinkedList empty cannot delete any node")
		else:
			node = self.head
			while(node.next != None):
				node = node.next
			node.prev.next = None
			self.size = self.size - 1
	
	def insertAt():
		pass
		
		
l = LinkedList()
l.add(1)
l.add(2)
l.addToLast(3)
l.addToLast(4)
l.printLL()
print("\n")
l.deleteFirst()
l.printLL()
print("\n")
l.deleteLast()
l.printLL()
print("\n")
print(l.size)