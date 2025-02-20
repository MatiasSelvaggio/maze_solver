from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.__root = Tk()

        self.__root.title("Maze solver Using DFS")

        self.__root.geometry(f"{width}x{height}")

        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)

        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def run(self):
        self.__running = True
        self.__root.mainloop()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas,fill_color)
    

