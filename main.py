from window import *
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600) #middle 400, 300
    numRows = 12
    numCols = 16
    margin = 50
    screenX = 800
    screenY = 600
    cellSizeX = (screenX - 2 * margin) / numCols
    cellSizeY = (screenY - 2 * margin) / numRows

    maze = Maze(margin, margin, numRows, numCols, cellSizeX, cellSizeY, win)
    

    win.wait_for_close()

main()
