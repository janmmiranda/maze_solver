from cell import Cell
import random
import time

class Maze():
    def __init__(self,
                 x1,
                 y1,
                 numRows,
                 numCols,
                 cellSizeX,
                 cellSizeY,
                 win=None,
                 seed=None
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.numRows = numRows
        self.numCols = numCols
        self.cellSizeX = cellSizeX
        self.cellSizeY = cellSizeY
        self.win = win
        self.cells = []
        if seed:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        for col in range(self.numCols):
            colList = []
            for row in range(self.numRows):
                colList.append(Cell(self.win))
            self.cells.append(colList)
        for col in range(self.numCols):
            for row in range(self.numRows):
                self._draw_cell(col, row)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cellSizeX
        y1 = self.y1 + j * self.cellSizeY
        x2 = x1 + self.cellSizeX
        y2 = y1 + self.cellSizeY
        self.cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def break_entrance_and_exit(self):
        self.cells[0][0].hasLeftWall = False
        self._draw_cell(0, 0)
        self.cells[self.numCols - 1][self.numRows - 1].hasRightWall = False
        self._draw_cell(self.numCols - 1, self.numRows - 1)

    def break_walls(self, col, row):
        curr = self.cells[col][row]
        curr.visited = True
        while True:
            choices = []
            leftNeighbor = self.cells[col - 1][row] if col - 1 >= 0 else None
            rightNeighbor = self.cells[col + 1][row] if col + 1 < self.numCols else None
            upNeighbor = self.cells[col][row - 1] if row - 1 >= 0 else None
            downNeighbor = self.cells[col][row + 1] if row + 1 < self.numRows else None
            if leftNeighbor and not leftNeighbor.visited:
                choices.append("l")
            if rightNeighbor and not rightNeighbor.visited:
                choices.append("r")
            if upNeighbor and not upNeighbor.visited:
                choices.append("u")
            if downNeighbor and not downNeighbor.visited:
                choices.append("d")    
            if len(choices) == 0:
                self._draw_cell(col, row)
                return
            choice = random.choice(choices)
            if choice == "l":
                curr.hasLeftWall = False
                self.break_walls(col - 1, row)
            elif choice == "r":
                curr.hasRightWall = False
                self.break_walls(col + 1, row)
            elif choice == "u":
                curr.hasTopWall = False
                self.break_walls(col, row - 1)
            elif choice == "d":
                curr.hasBottomWall = False
                self.break_walls(col, row + 1)
    
    def reset_cells_visited(self):
        for col in range(self.numCols):
            for row in range(self.numRows):
                self.cells[col][row].visited = False

    def solve(self):
        return self.solveR(0, 0)

    def solveR(self, col, row):
        self._animate()
        curr = self.cells[col][row]
        curr.visited = True

        if self.numCols - 1 == col and self.numRows - 1 == row:
            return True
        else:
            leftNeighbor = self.cells[col - 1][row] if col - 1 >= 0 and not self.cells[col - 1][row].visited and not curr.hasLeftWall else None
            rightNeighbor = self.cells[col + 1][row] if col + 1 < self.numCols and not self.cells[col + 1][row].visited and not curr.hasRightWall else None
            upNeighbor = self.cells[col][row - 1] if row - 1 >= 0  and not self.cells[col][row - 1].visited and not curr.hasTopWall else None
            downNeighbor = self.cells[col][row + 1] if row + 1 < self.numRows and not self.cells[col][row + 1].visited and not curr.hasBottomWall else None

            if leftNeighbor:
                curr.draw_move(leftNeighbor)
                temp = self.solveR(col - 1, row)
                if temp:
                    return True
                else:
                   curr.draw_move(leftNeighbor, True) 
            if rightNeighbor:
                curr.draw_move(rightNeighbor)
                temp = self.solveR(col + 1, row)
                if temp:
                    return True
                else:
                   curr.draw_move(rightNeighbor, True) 
            if upNeighbor:
                curr.draw_move(upNeighbor)
                temp = self.solveR(col, row - 1)
                if temp:
                    return True
                else:
                   curr.draw_move(upNeighbor, True) 
            if downNeighbor:
                curr.draw_move(downNeighbor)
                temp = self.solveR(col, row + 1)
                if temp:
                    return True
                else:
                   curr.draw_move(downNeighbor, True) 
        return False
