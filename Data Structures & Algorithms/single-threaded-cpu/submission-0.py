'''
given n tasks labeled from 0 to n - 1 (indices of task arr)
tasks[i] = [enqueueTime, processingTime]  # available to process, how long it takes

CPU will choose the shortest processingTime -> minHeap
If CPU is idle, and there are available tasks, CPU will choose shortest processingTime, 
or choose smallest index if all processingTimes equal

CPU finishes task and starts new one 

misconception: youre not returning turnaround time in which they finish in,
youre returning the response time 
'''
from heapq import heappush, heappop, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()

        res, minHeap = [], []
        time, i = 0, 0
        n = len(tasks)
        while len(res) < n:
            # if no tasks are available and time is less than next enqueued time
            # then make time = next tasks
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]
            
            while i < n and tasks[i][0] <= time:
                # enqueue time, processing time, idx
                enq, proc, idx = tasks[i]
                # prioritize processing time over idx
                heappush(minHeap, [proc, idx]) 
                i += 1
            
            proc, idx = heappop(minHeap)
            time += proc
            res.append(idx)
        
        return res

