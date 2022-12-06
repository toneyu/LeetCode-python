# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


# We break out of loop when one of the lists reaches end of nodes i.e. list 1 or list 2 becomes None
# the algorithm is the compare the values of l1 and l2 and the lower value gets merged into the new list

        dummy = ListNode() # object instantiation in python, create dummy node to start the expansion of our new merged list
        tail = dummy # dummy node is for the pointer to the head, reason is we will always end up with a dummy node in the merged list
        
        while list1 and list2: # while neither list is empty
            if list1.val < list2.val: #if first value in list 1 < list 2
                tail.next = list1 #new value in the list is taken from list 1
                list1 = list1.next # update list1 pointer to continue checking next element
            else:
                tail.next = list2 #if value of list 2 > list 1 
                list2 = list2.next# then we move new value from l2 to new list
            tail = tail.next #continue moving the pointer to next element regardless of either conditions
            
        #find the nonempty list here and insert at end of result
        if list1: #taking remaining portion of list1 and inserting to end of list
            tail.next = list1
        elif list2:# taking remaining portion of list2 and insert to end of list
            tail.next = list2
        
        return dummy.next# returns the head of merged list
        
        #the result linkedlist is always expanding so since the tail is at the end, that is also expanding
        
        
        
