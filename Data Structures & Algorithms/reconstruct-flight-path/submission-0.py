class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adjList = {src : [] for src, dst in tickets}

        for s, d in tickets:
            adjList[s].append(d)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adjList:
                return False
            
            temp = list(adjList[src])
            for i, dst in enumerate(temp):
                adjList[src].pop(i)
                res.append(dst)
                if dfs(dst): 
                    return True
                res.pop()
                adjList[src].insert(i, dst)
            return False
        dfs("JFK")
        return res
            





        