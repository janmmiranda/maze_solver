from window import *

def main():
    win = Window(800, 600)
    line1 = Line(Point(0,300), Point(800, 300))
    line2 = Line(Point(400, 0), Point(400, 600))
    win.drawLine(line1, "black")
    win.drawLine(line2, "red")
    win.wait_for_close()

main()
