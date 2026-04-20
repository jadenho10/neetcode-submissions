'''
my idea:
since hashmaps need their keys to be immutable
use a tuple of freq list
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagramList[tuple(count)].append(s)
        return list(anagramList.values())
            