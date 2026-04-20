'''
So we start off at "0000" and want to reach "target"

Also, we cannot touch any combinations in "deadends"

deadends = ["1111","0120","2020","3333"], target = "5555"  output = 20

so we keep rotating this mf until we reach 5555

BFS: we are trying to find the shortest path from og node to this node
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        q = deque([['0000', 0]]) # q will consist of node : moves it takes to get there
        visit = set(['0000'])
        while q:
            node, minMoves = q.popleft()
            if node == target:
                return minMoves
            for i in range(4):
                for d in [-1, 1]:
                    newDigit = (int(node[i]) + d) % 10
                    newComb = node[:i] + str(newDigit) + node[i + 1:]
                    if newComb not in visit and newComb not in deadends:
                        visit.add(newComb)
                        q.append([newComb, minMoves + 1])
            
        return -1