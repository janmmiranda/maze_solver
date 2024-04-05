from window import Window, Line, Point


class Cell():
    def __init__(self, win) -> None:
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.win = win
        self.hasLeftWall = True
        self.hasRightWall = True
        self.hasTopWall = True
        self.hasBottomWall = True
        self.visited = False

    def __repr__(self) -> str:
        return f"Cell(x1: {self.x1}, y1: {self.y1}, x2: {self.x2}, y2: {self.y2}, hasLeft: {self.hasLeftWall}, hasRight: {self.hasRightWall}, hasTop: {self.hasTopWall}, hasBottom: {self.hasBottomWall})"

    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
       
        line = Line(Point(self.x1, self.y1), Point(self.x1, self.y2))
        self.win.drawLine(line, "black" if self.hasLeftWall else "#dcdcdc")
    
        line = Line(Point(self.x2, self.y1), Point(self.x2, self.y2))
        self.win.drawLine(line, "black" if self.hasRightWall else "#dcdcdc")
    
        line = Line(Point(self.x1, self.y1), Point(self.x2, self.y1))
        self.win.drawLine(line, "black" if self.hasTopWall else "#dcdcdc")
    
        line = Line(Point(self.x1, self.y2), Point(self.x2, self.y2))
        self.win.drawLine(line, "black" if self.hasBottomWall else "#dcdcdc")

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        mid1 = self.find_center(self.x1, self.y1, self.x2, self.y2)
        mid2 = self.find_center(to_cell.x1, to_cell.y1, to_cell.x2, to_cell.y2)
        print(f"drawing line from ({mid1}) to ({mid2})")
        line = Line(Point(mid1[0], mid1[1]), Point(mid2[0], mid2[1]))
        self.win.drawLine(line, color)


    def find_center(self, x1, y1, x2, y2):
        midX = (x1 + x2) / 2
        midY = (y1 + y2) / 2
        return (midX, midY)