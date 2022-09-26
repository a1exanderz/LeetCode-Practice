class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         # Merge the two lists and sort based on initial distance.
#         # 1 3 1 4 2 
#         # 0 3 5 8 10
#         #=1 6 6 12 12 because the value = target, pop both from stack. then +1 to fleet
#         #             if the stack is not monotonic, set the larger number, or any equal numbers, to the smallest number ahead.
#         #             also set their speed to be equal to the frontmost speed.
        
#         # 1 1 1
#         # 1 6 6 ... until they reach 12, then pop both and +1 to fleet
        
#         # 1
#         # 6 ... until they reach 12, then pop and +1 to fleet

        
#         ## Merge the two lists and sort based on initial distance ascending
#         mergeList = []
#         for i in range(0, len(position)):
#             mergeList.append((position[i], speed[i]))
            
#         mergeList.sort() # O(log(n)) time
        
#         ## Create a loop to update distance per speed increment
#         fleetCount = 0
#         while mergeList:
#             print(mergeList)
#             addToFleetCount = False
#             while mergeList and mergeList[-1][0] >= target:
#                 mergeList.pop()
#                 addToFleetCount = True
#             for i in range(0, len(mergeList)):
#                 mergeList[i] = (mergeList[i][0] + mergeList[i][1], mergeList[i][1])
#             if addToFleetCount:
#                 fleetCount += 1
#             print(fleetCount)
        
#         return fleetCount

        # Solution: calculate the time it would take to reach target for each car
        # For each car in the list, if it will arrive faster than the one ahead of it, you can remove those cars from the list
        # Then, return the final length of the list
        
        mergeList = []
        for i in range(0, len(position)):
            mergeList.append((position[i], speed[i]))
            
        mergeList.sort() # O(nlog(n)) time
        
        timeList = []
        for i in range(0, len(mergeList)):
            timeList.append((target - mergeList[i][0]) / mergeList[i][1])
        
        # print(timeList)
        
        stack = []
        for i in range(len(mergeList) - 1, -1, -1):
            if not stack:
                stack.append(timeList[i])
            else:
                if timeList[i] <= stack[-1]:
                    continue
                else:
                    stack.append(timeList[i])
        
        return len(stack)
        
            
            
            