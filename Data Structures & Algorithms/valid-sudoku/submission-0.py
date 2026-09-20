class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n_rows = len(board)
        n_cols = len(board[0])
        for row in board:
            seen = set()
            for num in row:
                if num==".":
                    continue
                elif int(num) <= 1 and int(num) >= 9:
                    return False
                elif int(num) in seen:
                    return False
                else:
                    seen.add(int(num))
        for col in range(n_cols):
            seen = set()
            for row in range(n_rows):
                if board[row][col]==".":
                    continue
                elif int(board[row][col]) <= 1 and int(board[row][col]) >= 9:
                    return False
                elif int(board[row][col]) in seen:
                    return False
                else:
                    seen.add(int(board[row][col]))
        for r in range(0,n_rows, 3):
            for c in range(0, n_cols, 3):
                seen = set()
                for row in range(r, r+3):
                    for col in range(c, c+3):
                        if board[row][col] == ".":
                            continue
                        elif int(board[row][col]) in seen:
                            return False
                        else:
                            seen.add(int(board[row][col]))

        return True