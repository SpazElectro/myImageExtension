import tkinter as tk
import myimg_reader

# conv_or_start = input("Convert or start? (start)")

# if conv_or_start == "" or conv_or_start == "start":
#     print("Starting")
# else:
#     exec(open("image_converter.py").read())
#     print("Starting")


fname = "img.myimg"#input("Input filename: ")
data = myimg_reader.openFile(fname)

def rgb2hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = int(data["width"])
        self.columns = int(data["height"])
        self.tiles = {}
        self.canvas.bind("<Configure>", self.redraw)

    def redraw(self, event=None):
        self.canvas.delete("rect")
        cellwidth = int(self.canvas.winfo_width()/self.columns)
        cellheight = int(self.canvas.winfo_height()/self.columns)
        index = -1

        for column in range(self.columns):
            for row in range(self.rows):
                index += 1
                colour = rgb2hex(data["pixels"][index][0], data["pixels"][index][1], data["pixels"][index][2])
                x1 = column*cellwidth
                y1 = row * cellheight
                x2 = x1 + cellwidth
                y2 = y1 + cellheight
                tile = self.canvas.create_rectangle(x1,y1,x2,y2, fill=colour, tags="rect")
                self.tiles[row,column] = tile

if __name__ == "__main__":
    app = App()
    app.mainloop()