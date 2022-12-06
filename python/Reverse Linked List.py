# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         prev = None
        
#         while head: # does head still have a value?
#             temp = head
#             head = head.next # temp moves with head
#             temp.next = prev # but then we set temp to point in reverse direction at prev
#             prev = temp # prev initially starts at null
#         return prev
    
          
          #Recursive
        if not head:
            return None
        
        temp = head
        if head.next:
            temp = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return temp