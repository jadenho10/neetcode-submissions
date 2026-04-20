from heapq import heappush, heappop, heapify
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        res = 0
        maxheap = [-num for num in count.values()]
        q = deque() # (num of tasks remaining, time slot)

        while maxheap or q:
            res += 1
            if not maxheap:
                res = q[0][1]
            else:
                cnt = 1 + heappop(maxheap)
                if cnt:
                    q.append((cnt, res + n))
            if q and q[0][1] == res:
                heapq.heappush(maxheap, q.popleft()[0])
        return res




