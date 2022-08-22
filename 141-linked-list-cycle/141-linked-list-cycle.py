# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Basic Solution: O(n) time and O(n) memory
        # Create a list with all new values in the linked list. 
        # Traverse through the entire linked list.
        # If a node already exists in the list, return true.
        # If next node is None and true not returned, then return false.
        
#         hashMap = {}
#         curr = head
        
#         while curr is not None:
#             print(hashMap)
#             if curr in hashMap.keys():
#                 return True
#             else:
#                 hashMap[curr] = 0
#             curr = curr.next
#         return False
        
        # Using the turtle and rabbit solution: O(n) time and O(1) memory
        # Create a turtle pointer and a rabbit pointer
        # The rabbit pointer will move 2x every turn and turtle 1x
        # If the two meet, then there is a loop, if fast reaches null then there is not
        
        turtle = head
        rabbit = head
        
        while rabbit is not None and rabbit.next is not None:
            print(turtle.val, rabbit.val)
            turtle = turtle.next
            rabbit = rabbit.next.next
            
            if turtle == rabbit:
                return True
        
        return False