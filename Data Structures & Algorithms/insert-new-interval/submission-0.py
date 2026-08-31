class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = []
        temp = newInterval
        j = 0
        while j < len(intervals):
            cur = intervals[j]
            if cur[1] < temp[0]:
                new.append(cur)
            elif temp[1] < cur[0]:
                new.append(temp)
                return new + intervals[j:]
            else:
                temp = [min(cur[0],temp[0]),max(cur[1],temp[1])]
            j+=1
        
        new.append(temp)
        return new
