class Node():
	def __init__(self,x):
		self.val = x
		self.next = None
	
	def __str__(self):
		return f"Value of current node is {self.val}"
