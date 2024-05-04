import tkinter as tk
from tkinter import colorchooser, simpledialog

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Paint Program")

        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.brush_color = "black"
        self.brush_size = 2
        self.fill_color = None
        self.text = ""

        self.selected_tool = "brush"
        self.start_x = None
        self.start_y = None
        self.draw_objects = []

        self.setup_menu()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def setup_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Brush", command=lambda: self.select_tool("brush"))
        tools_menu.add_command(label="Eraser", command=lambda: self.select_tool("eraser"))
        tools_menu.add_command(label="Text", command=self.add_text)
        tools_menu.add_command(label="Fill Color", command=self.pick_fill_color)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        color_menu = tk.Menu(menubar, tearoff=0)
        color_menu.add_command(label="Brush Color", command=self.pick_brush_color)
        menubar.add_cascade(label="Colors", menu=color_menu)

    def select_tool(self, tool):
        self.selected_tool = tool

    def pick_brush_color(self):
        color = colorchooser.askcolor(title="Choose Brush Color")[1]
        if color:
            self.brush_color = color

    def pick_fill_color(self):
        color = colorchooser.askcolor(title="Choose Fill Color")[1]
        if color:
            self.fill_color = color

    def add_text(self):
        self.text = simpledialog.askstring("Text", "Enter Text:")
        if self.text:
            self.selected_tool = "text"

    def paint(self, event):
        if self.selected_tool == "brush":
            if self.start_x and self.start_y:
                x, y = event.x, event.y
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill=self.brush_color, width=self.brush_size, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.start_x, self.start_y = event.x, event.y
        elif self.selected_tool == "eraser":
            if self.start_x and self.start_y:
                x, y = event.x, event.y
                self.canvas.create_line(self.start_x, self.start_y, x, y, fill="white", width=self.brush_size, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.start_x, self.start_y = event.x, event.y
        elif self.selected_tool == "text":
            if self.start_x and self.start_y:
                x, y = event.x, event.y
                self.canvas.create_text(x, y, text=self.text, fill=self.brush_color)
                self.selected_tool = "brush"  # switch back to brush after adding text

    def reset(self, event):
        self.start_x, self.start_y = None, None

root = tk.Tk()
paint_app = PaintApp(root)
root.mainloop()
