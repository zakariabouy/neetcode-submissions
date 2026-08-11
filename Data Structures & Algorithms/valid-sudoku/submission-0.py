class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hash sets to track what digits we have seen
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # Key will be a tuple: (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                # If the digit is already in the row, col, or square, it's invalid
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                
                # Otherwise, register the digit as "seen" in our sets
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True