# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution: Did not work
        # Add the end of each linkedList to a new linkedList. Once added, remove from original

#         curr = head
#         nodeList = [curr]

#         while (curr.next != None):
#             curr = curr.next
#             nodeList.append(curr)

#         reverseList = nodeList[-1]
#         reverseList.next = nodeList[3]
#         print(reverseList)

#         i = len(nodeList) - 2
#         print(i, nodeList[i])


#         while i >= 0:
#             reverseList.next = nodeList[i]
#             reverseList = reverseList.next
#             i -= 1
#             print(reverseList)

############
        # Solution 1: Iterative
        # Use a two pointer approach. 
        # Pointer 1 is first set to None and Pointer 2 is first set to head
        # Save the current Pointer 2.next as a temp variable, and then set Pointer 2.next to Pointer 1
        # Pointer 1 should be set to Pointer 2, and Pointer 2 to the temp variable
        # Continue until Pointer 2 has no next
        
        p1, p2 = None, head
        
        while p2:
            temp = p2.next
            p2.next = p1
            p1 = p2
            p2 = temp
            
        return p1
            
            
            
        
        
            
            
        
        
        
        