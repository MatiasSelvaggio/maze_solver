from window import Window
from geometry import *
from cell import Cell

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

    c1 = Cell(window)
    c1.has_right_wall = False
    c1.draw(50, 50, 100, 100)

    c2 = Cell(window)
    c2.has_left_wall = False
    c2.has_bottom_wall = False
    c2.draw(100, 50, 150, 100)

    c1.draw_move(c2)

    c3 = Cell(window)
    c3.has_top_wall = False
    c3.has_right_wall = False
    c3.draw(100, 100, 150, 150)

    c2.draw_move(c3)

    c4 = Cell(window)
    c4.has_left_wall = False
    c4.draw(150, 100, 200, 150)

    c3.draw_move(c4, True)

    window.wait_for_close()


if __name__ == "__main__":
    main()
