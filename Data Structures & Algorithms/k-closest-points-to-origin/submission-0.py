from heapq import heapify,heappop 
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append((sqrt((p[0]**2)+(p[1]**2)),p))
        heapify(heap)
        return [heappop(heap)[1] for i in range(k)] 