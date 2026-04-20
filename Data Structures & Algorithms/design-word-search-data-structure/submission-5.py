class TrieNode:
    def __init__(self):
        self.children = {}
        self.endsWith = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    '''
    adding children nodes to root. set last char of string as true (endsWith)
    '''
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endsWith = True

    # dfs when we have "." regex
    def search(self, word: str) -> bool:
        # params: j: index after "period", curr is the node we are pointing at
        def dfs(j, root):
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endsWith
        
        return dfs(0, self.root)

