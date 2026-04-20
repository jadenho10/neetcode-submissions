class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1count, s2count = [0] * 26, [0] * 26  # all of size 26
        for r in range(len(s1)):
            s1count[ord(s1[r]) - ord('a')] += 1 
            s2count[ord(s2[r]) - ord('a')] += 1 
        

        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            i = ord(s2[r]) - ord('a')
            if s2count[i] == s1count[i]:
                matches -= 1
            s2count[i] += 1
            if s1count[i] == s2count[i]:
                matches += 1
            
            
            i = ord(s2[l]) - ord('a')
            if s2count[i] == s1count[i]:
                matches -= 1
            s2count[i] -= 1
            if s1count[i] == s2count[i]:
                matches += 1
            
            l += 1
        return matches == 26