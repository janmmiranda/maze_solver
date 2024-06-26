from window import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600) #middle 400, 300
    numRows = 6
    numCols = 8
    margin = 50
    screenX = 800
    screenY = 600
    cellSizeX = (screenX - 2 * margin) / numCols
    cellSizeY = (screenY - 2 * margin) / numRows

    maze = Maze(margin, margin, numRows, numCols, cellSizeX, cellSizeY, win, 0)
    maze.break_entrance_and_exit()
    maze.break_walls(0, 0)
    maze.reset_cells_visited()
    maze.solve()
    
    win.wait_for_close()

main()
