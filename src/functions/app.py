import customtkinter as ctk
from src.functions.events import btn1
from src.widgets import frames

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("App Banking System")
        self.windowState = "MENU"

        # Grid configuratio
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frames for buttons and the screen
        self.action_btns = frames.ActionFrame(self, self)
        self.screen_frame = frames.ScreenFrame(self)
        self.confirmation = frames.ConfirmationButtons(self, self)
        self.keypad = frames.Keypad(self, self)

        # Placements of the frames
        self.action_btns.grid(row=0, rowspan=4,column=0, sticky="ns")
        self.screen_frame.grid(row=0, rowspan=5, column=1, columnspan=4,padx=5, sticky="nsew")
        self.confirmation.grid(row=0, rowspan=2, column=5, padx=5, sticky="ns")
        self.keypad.grid(row=6, rowspan=4, column=1, columnspan=4, sticky="ew")

    def handle_actions(self, action):
        if self.windowstate == "MENU":
            if action=="B":
                self.windowState = "BALANCE"
            elif action=="W":
                self.windowState = "WITHDRAW"
            elif action=="D":
                self.windowState = "DEPOSIT"
            elif action=="Q":
                self.windowState = "MENU"
            else:
                self.CTkInputDialog(text="??? How'd you even get this error, sum ting rong wid your code boi", title="Error")
                # self.CTkMessageBox()
        
    """ SO THIS IS FOR THE CONFIRMATION BTUTON WHICH IM NOT SURE HOW TO IMPLEMENT YET 
    def confirmation(str):
        if str == "y":

        elif str=="n":
    """

    def button_click(self):
        print("Button clicked")



app = App()


