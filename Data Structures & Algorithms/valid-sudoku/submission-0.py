class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check for duplicates within each row
        for row in range(len(board)):
            rows = set()
            for col in range(len(board)):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows:
                    return False
                rows.add(board[row][col])

        # check for duplicates within each column
        for row in range(len(board)):
            cols = set()
            for col in range(len(board)):
                if board[col][row] == '.':
                    continue
                if board[col][row] in cols:
                    return False
                cols.add(board[col][row])

        # check 3x3 boxes

        for startRow in range(0, 9, 3):
            for startCol in range(0, 9, 3):
                seen = set()

                for row in range(startRow, startRow + 3):
                    for col in range(startCol, startCol + 3):
                        if board[row][col] == '.':
                            continue
                        if board[row][col] in seen:
                            return False
                        seen.add(board[row][col])

        return True