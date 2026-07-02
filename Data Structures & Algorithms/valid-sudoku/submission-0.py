class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # --- ROW CHECK ---
        for row in board:
            rowOptions = ["."] + [str(x) for x in range(1, 10)]
            for rowElement in row:
                if rowElement == ".": continue
                if rowOptions[int(rowElement)] == rowElement:
                    rowOptions[int(rowElement)] = "."
                else: return False
        
        # --- COLUMN CHECK ---
        for col in range(9):
            colOptions = ["."] + [str(x) for x in range(1, 10)]
            for row in range(9):
                colElement = board[row][col]
                if colElement == ".": continue
                if colOptions[int(colElement)] == colElement:
                    colOptions[int(colElement)] = "."
                else: return False
                
        # --- BOX CHECK ---
        for boxRow in range(0, 9, 3):
            for boxCol in range(0, 9, 3):
                boxOptions = ["."] + [str(x) for x in range(1, 10)]
                for col in range(boxCol, boxCol + 3):
                    for row in range(boxRow, boxRow + 3):
                        boxElement = board[row][col]
                        if boxElement == ".": continue
                        if boxOptions[int(boxElement)] == boxElement:
                            boxOptions[int(boxElement)] = "."
                        else: return False

        return True