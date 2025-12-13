import customtkinter as ctk
from src.widgets import buttons, frames

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.resizable(False, False)
        self.title("App Banking System")

        # add widgets to app
        self.button = customtkinter.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)


    def button_click(self):
        print("button click")



    def current_frame(self):
        frame = self.frames(name)


app = App()




