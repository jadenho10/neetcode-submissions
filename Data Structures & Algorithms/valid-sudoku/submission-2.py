class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet, colSet, sqSet = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue          
                val = board[r][c]
                if val in rowSet[r] or val in colSet[c] or val in sqSet[(r // 3, c // 3)]:
                    return False
                rowSet[r].add(val)
                colSet[c].add(val)
                sqSet[(r // 3, c // 3)].add(val)
        return True
