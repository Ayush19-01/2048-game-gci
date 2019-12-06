#MADE FOR SOLE PUPOSE OF GOOGLE CODE-IN 2019
#2048 Game 
import random
from tkinter import Frame, Label, CENTER
import algorithms as algo
colorbg={2: "#ffffff", 4: "#D2B48C", 8: "#D2691E", 16: "#A0522D", 32: "#8B4513", 64: "#A52A2A", 128: "#edcf72", 256: "#edcc61", 512: "#edc850", 1024: "#edc53f", 2048: "#edc22e"}
fontbg={2: "#776e65", 4: "#f9f6f2", 8: "#f9f6f2", 16: "#f9f6f2",32: "#f9f6f2", 64: "#f9f6f2", 128: "#f9f6f2",256: "#f9f6f2", 512: "#f9f6f2", 1024: "#f9f6f2", 2048: "#f9f6f2" }
FONT = ("Roboto", 40, "bold")
KEY_UP = "'i'"
KEY_DOWN = "'k'"
KEY_LEFT = "'j'"
KEY_RIGHT = "'l'"
KEY_BACK = "'p'"

class GameGrid(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.key_down)
        self.commands = {KEY_UP: algo.up,KEY_DOWN: algo.down,KEY_LEFT: algo.left, KEY_RIGHT: algo.right}
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg="#92877d",width=400, height=400)
        background.grid()

        for i in range(4):
            grid_row = []
            for j in range(4):
                cell=Frame(background, bg="#220047",width=100,height=100)
                cell.grid(row=i, column=j)
                t = Label(master=cell, text="",bg="#220047",justify=CENTER, font=FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)

    def gen(self):
        return random.randint(0,4-1)

    def init_matrix(self):
        self.matrix = algo.new1(4)
        self.history_matrixs = list()
        self.matrix = algo.addition(self.matrix)
        self.matrix = algo.addition(self.matrix)

    

    def key_down(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, done = self.commands[repr(event.char)](self.matrix)
            if done:
                self.matrix = algo.addition(self.matrix)
                self.history_matrixs.append(self.matrix)
                self.update_grid_cells()
                done = False
                if algo.status(self.matrix) == 'win':
                    self.grid_cells[0][0].configure(text="Y", fg="#CE9141", bg="#220047")
                    self.grid_cells[0][1].configure(text="O", fg="#CE9141", bg="#220047")
                    self.grid_cells[0][2].configure(text="U", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][0].configure(text="W", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][1].configure(text="I", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][2].configure(text="N", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][3].configure(text="!", fg="#CE9141", bg="#220047")
                if algo.status(self.matrix) == 'lose':
                    self.grid_cells[0][0].configure(text="G", fg="#CE9141", bg="#220047")
                    self.grid_cells[0][1].configure(text="A", fg="#CE9141", bg="#220047")
                    self.grid_cells[0][2].configure(text="M", fg="#CE9141", bg="#220047")
                    self.grid_cells[0][3].configure(text="E", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][0].configure(text="O", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][1].configure(text="V", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][2].configure(text="E", fg="#CE9141", bg="#220047")
                    self.grid_cells[1][3].configure(text="R", fg="#CE9141", bg="#220047")
                    self.grid_cells[2][0].configure(text="Y", fg="#CE9141", bg="#220047")
                    self.grid_cells[2][1].configure(text="O", fg="#CE9141", bg="#220047")
                    self.grid_cells[2][2].configure(text="U", fg="#CE9141", bg="#220047")
                    self.grid_cells[2][3].configure(text=" ", fg="#CE9141", bg="#220047")
                    self.grid_cells[3][0].configure(text="L", fg="#CE9141", bg="#220047")
                    self.grid_cells[3][1].configure(text="O", fg="#CE9141", bg="#220047")
                    self.grid_cells[3][2].configure(text="S", fg="#CE9141", bg="#220047")
                    self.grid_cells[3][3].configure(text="E", fg="#CE9141", bg="#220047")
    def update_grid_cells(self):
        for i in range(4):
            for j in range(4):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg="#220047")
                else:
                    self.grid_cells[i][j].configure(text=str(new_number), bg=colorbg[new_number],fg=fontbg[new_number])
        self.update_idletasks()

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2


GameGrid()
