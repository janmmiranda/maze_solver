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
                 win
                 ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.numRows = numRows
        self.numCols = numCols
        self.cellSizeX = cellSizeX
        self.cellSizeY = cellSizeY
        self.win = win
        self.cells = []

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