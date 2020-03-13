from tkinter import *
from tkinter.ttk import *
import comments
import textbox as tb
class CommentWriter(Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.value = StringVar()
        self.create_widgets()
        self.create_dropboxes()
        self.create_namebox()


    def create_widgets(self):
        self.commentbox = tb.TextBox(self.master)
        self.commentbox.get_textbox().grid(row=2, column=0)

        #self.quit = Button(self.master, text="QUIT", fg="red",
       #                       command=self.master.destroy)
       # self.quit.grid(row=3, column=0)

        self.test = Button(self.master, command=lambda: self.commentbox.write_textbox(self.behavior.get(), "male", "Steve"))
        self.test.grid(row=2, column=1)


    def create_dropboxes(self):
        self.behavior = Combobox(self.master, values = comments.behavior, state = "readonly")
        self.behavior.grid(row=1, column=0)


    def create_namebox(self):
        self.namebox = Label(self.master, text="Name of Student")
        self.namebox.grid(row=0, column=0, sticky="W")


if __name__ == "__main__":
    root = Tk()
    app = CommentWriter(master=root)
    app.mainloop()

