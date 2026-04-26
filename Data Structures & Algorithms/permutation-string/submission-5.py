class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            c, k = s1[i], s2[i]
            s1Count[ord(c) - ord('a')] += 1
            s2Count[ord(k) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[r]) - ord('a')

            # if before adding s2[r] into s2Count, these freqs match, then decrement matches
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] += 1
            # if match exists, matches + 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            
            index = ord(s2[l]) - ord('a')
            # if before adding s2[l] into s2Count, these freqs match, then decrement matches
            if s2Count[index] == s1Count[index]:
                matches -= 1
            s2Count[index] -= 1
            # if match exists, matches + 1
            if s2Count[index] == s1Count[index]:
                matches += 1

            l += 1
        
        return matches == 26