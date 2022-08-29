class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # We want to sort the points in the list by distance
        # Then return the up to the kth point
        
        # We want a data structure that can store points in order
        # Use a minHeap
        # Pop from the minHeap k times
        
        minHeap = []
        for point in points:
            x = point[0]
            y = point[1]
            dist = x**2 + y**2
            point = [dist, x, y]
            minHeap.append(point)
        heapq.heapify(minHeap)
        print(minHeap)
        
        output = []
        for i in range(k):
            closestPoint = heapq.heappop(minHeap)
            print(closestPoint)
            output.append(closestPoint[1::])
            
        return output