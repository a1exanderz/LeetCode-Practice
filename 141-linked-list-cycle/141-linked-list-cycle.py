# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Solution: O(n) time and O(n) memory
        # Create a hashmap with all new values in the linked list. 
        # Traverse through the entire linked list.
        # If a node already exists in the dictionary, return true.
        # If next node is None and true not returned, then return false.
        
        hashMap = []
        curr = head
        
        while curr is not None:
            if curr in hashMap:
                return True
            else:
                hashMap.append(curr)
            curr = curr.next
        return False
            