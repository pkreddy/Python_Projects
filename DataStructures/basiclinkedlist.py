class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self #start from head node
        while node != None:
            print(node.val) #prints the node value
            node = node.next #move to the next node


node1 = Node(12)
node2 = Node(14)
node3 = Node(16)
node1.next = node2
node2.next = node3

node1.traverse()
