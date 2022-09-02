class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [1,0] [2,1]
        # To take 1, need to finish 0
        # To take 2, need to finish 1
        # True
        
        # Conflict when you create a loop
        # [[1,0],[0,2],[2,1]]
        # 1: 0,2
        # 0: 1,2
        # 2: 0,1
        # false
        
        # [1,0] [2,1]
        # 1: 0,2
        # 0: 1
        # 2: 1
        # true
        
        # [[1,0], [1,2], [1,3]]
        # 1: 0,2
        # 1: 3
        # 0: 1
        # 2: 1
        # 3: 1
        # True
        
        # [[1,4],[2,4],[3,1],[3,2]]
        # 1: 4,3
        # 4: 1,2
        # 2: 4,3
        # 3: 1,2

        # Conflict once there is a loop      
        # Create an adjacency list, if there is a loop return false
        # Use DFS in the adjacency list 
        
        # print(prerequisites)
        
        hashMap = {i:[] for i in range(numCourses)} # Creates an empty dictionary with empty lists for each value in numCourses
        
        for course, prerequisite in prerequisites:
            hashMap[course].append(prerequisite)
        
        visitSet = set()
        
        def dfs(course):
            if course in visitSet:
                return False
            if hashMap[course] == []:
                return True
            
            visitSet.add(course)
            for prerequisite in hashMap[course]:
                if not dfs(prerequisite): return False
            
            visitSet.remove(course)
            hashMap[course] = []
            return True
                
        for course in range(numCourses):
            if not dfs(course): return False
        return True

    
                
                
            