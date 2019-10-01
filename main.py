import tkinter as tk
import comments

class CommentWriter(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        self.value = tk.StringVar()
        self.pack()
        self.create_widgets()
        self.create_dropboxes()

    def create_widgets(self):
        self.commentbox = tk.Text(self)
        self.commentbox.pack(side="top")


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.test = tk.Button(self, text="Insert", fg="black", command=self.write_textbox)
        self.test.pack(side="bottom")

    def create_dropboxes(self):
        self.value.set(comments.BEHAVIOR[0])
        self.behavior = tk.OptionMenu(self, self.value, *comments.BEHAVIOR)
        self.behavior.pack(side="left")


    def write_textbox(self):
        self.commentbox.insert("end", self.value.get())


root = tk.Tk()
app = CommentWriter(master=root)
app.mainloop()