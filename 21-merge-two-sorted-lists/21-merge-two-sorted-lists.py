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
        
        # Compare the first nodes between two lists. Add the smaller one to the merged list (or if equal, from list1), continue until end of each list
        # Iterative method, O(n+m) time. O(1) space.
        
        dummy_node = ListNode()
        tail = dummy_node
        
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        else:
            tail.next = list2
            
        return dummy_node.next


#         # Recursive method
#         if list1 == None: return list2
#         if list2 == None: return list1
        
#         if list1.val <= list2.val:
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             print("list1", list1)
#             return list1
#         if list1.val > list2.val:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             print("list2", list2)
#             return list2
        
        
    
        
        
        
        
        