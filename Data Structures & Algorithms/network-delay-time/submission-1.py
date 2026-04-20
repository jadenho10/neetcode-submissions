from collections import defaultdict
from heapq import heappop, heapify, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for s, t, w in times:
            edges[s].append([t, w])

        minHeap = [[0, k]]
        res = 0
        visit = set()

        while minHeap:
            wei, node = heappop(minHeap)
            if node in visit:
                continue
            visit.add(node) 
            res = wei

            for nei, wei2 in edges[node]:    
                if nei not in visit:
                    heappush(minHeap, [wei + wei2, nei]) 

        return res if len(visit) == n else -1