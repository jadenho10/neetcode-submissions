class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_cont, t_cont = {}, {}
        for i in range(len(s)):
            s_cont[s[i]] = 1 + s_cont.get(s[i], 0)
            t_cont[t[i]] = 1 + t_cont.get(t[i], 0)
        
        return s_cont == t_cont