from tkinter import *
from tkinter.ttk import *


class TextBox:
    
    def __init__(self, master_input):
        self.commentbox = Text(master_input, width=100, height=20)
    

    def get_textbox(self):
        return self.commentbox

    def parse_input(self, input, gender, name):
        self.add_name(input, name)
        
        if gender is "male":
            input = input.replace("[g]", "He")
        return input

    def add_name(self, input, name)
        if not self.commentbox.get("1.0", "end-1c"):
            return input.replace("[g]", name, 1)
    def write_textbox(self, input, gender, name):
        input = self.parse_input(input, gender, name)
        self.commentbox.insert("end", input)