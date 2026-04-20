class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        res, visit = 0, set(wordList)
        q = deque([beginWord])
        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft() 
                if node == endWord:
                    return res
                for i in range(len(node)):
                    for c in range(97,123):
                        if node[i] != c:
                            nei = node[:i] + chr(c) + node[i + 1:]
                            if nei in visit:
                                visit.remove(nei)
                                q.append(nei)
        return 0
                
