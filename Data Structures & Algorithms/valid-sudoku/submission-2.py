class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                if board[r][c] not in rows[r]:
                    rows[r].add(board[r][c])
                else:
                    return False
                
                if board[r][c] not in cols[c]:
                    cols[c].add(board[r][c])
                else:
                    return False
                
                if board[r][c] not in squares[(r //3 , c//3)]:
                    squares[(r // 3, c //3)].add(board[r][c])
                else:
                    return False
        
        return True
            