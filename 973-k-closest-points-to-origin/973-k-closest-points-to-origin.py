class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # We want to sort the points in the list by distance
        # Then return the up to the kth point
        
        # We want a data structure that can store points in order
        # Use a minHeap
        # Pop from the minHeap k times
        
        minHeap = []
        for point in points:
            minHeap.append([point[0]**2 + point[1]**2, point[0], point[1]])
        heapq.heapify(minHeap)
        print(minHeap)
        
        output = []
        for i in range(k):
            output.append(heapq.heappop(minHeap)[1::])
            
        return output