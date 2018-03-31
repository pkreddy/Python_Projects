class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def nxt(self,next_val):
        self.next = next_val

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
      
n = Node(1)
n.nxt(2)
n.nxt(3)
n.nxt(5)
n.traverse()
