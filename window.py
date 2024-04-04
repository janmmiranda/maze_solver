from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "test"
        self.canvas = Canvas(self.__root, {"width": width, "height": height})
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
        print("closing window")

    def drawLine(self, line, fillColor):
        line.draw(self.canvas, fillColor)

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fillColor):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y,
            fill=fillColor, width=2
        )
        canvas.pack()