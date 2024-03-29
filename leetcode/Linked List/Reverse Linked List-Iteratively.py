# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        newNode = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = newNode
            newNode = cur
            cur = temp
        return newNode
            
            