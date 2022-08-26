class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # If the intervals overlap, take minimum and maximum of the two intervals
        
        output = []
        
        # If empty list
        if not intervals:
            output.append(newInterval)
            return output
        
        # If either before or after
        if newInterval[1] < intervals[0][0]:
            output.append(newInterval)
            for interval in intervals:
                output.append(interval)
            return output
                
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        # If in the middle, overlapping
        merge = False
        for interval in intervals:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                output.append(interval)
            elif interval[0] > newInterval[1] and interval[1] > newInterval[1]:
                if not merge:
                    output.append(newInterval)
                    merge = True
                output.append(interval)
            else:
                if not merge:
                    output.append([interval[0], interval[1]])
                    merge = True
                
                output[-1] = [min(output[-1][0], interval[0], newInterval[0]), max(output[-1][1], interval[1], newInterval[1])]
                print("merge", interval[0], interval[1])
                
        return output

        #### PROPER METHOD
        

