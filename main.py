from window import Window
from geometry import *

def main():
    window = Window(800, 600)
    point_a = Point(10,10)
    point_b = Point(790,10)
    line_a = Line(point_a, point_b)
    point_c = Point(10,10)
    point_d = Point(10,590)
    line_b = Line(point_c, point_d)
    point_e = Point(10,590)
    point_f = Point(790,590)
    line_c = Line(point_e, point_f)
    point_g = Point(790,590)
    point_h = Point(790,10)
    line_d = Line(point_g, point_h)
    window.draw_line(line_a,"red")
    window.draw_line(line_b, "black")
    window.draw_line(line_c, "blue")
    window.draw_line(line_d, "green")

    window.wait_for_close()


if __name__ == "__main__":
    main()
