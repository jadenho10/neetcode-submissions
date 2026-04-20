class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:  
        # Edge case  
        if len(s1) > len(s2):
            return False
        s1ct, s2ct = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1ct[ord(s1[i]) - ord('a')] += 1
            s2ct[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1ct[i] == s2ct[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            i = ord(s2[r]) - ord('a')
            if s2ct[i] == s1ct[i]:
                matches -= 1
            s2ct[i] += 1
            if s1ct[i] == s2ct[i]:
                matches += 1

            i = ord(s2[l]) - ord('a')
            if s2ct[i] == s1ct[i]:
                matches -= 1
            s2ct[i] -= 1
            if s1ct[i] == s2ct[i]:
                matches += 1
            l += 1
        return matches == 26
            
