class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = defaultdict(int), defaultdict(int)
        for c1, c2 in zip(s, t):
            s_count[c1] += 1
            t_count[c2] += 1
        
        return s_count == t_count
