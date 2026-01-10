import customtkinter as ctk
from src.widgets.buttons import AppButton, LongerButton

# Action Frame buttons
class ActionFrame(ctk.CTkFrame):
    # Constructor
    def __init__(self, parent, app):
        # Frame instantiation
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.pady = 10
        self.create_widgets()

    # Buttons for actions
    def create_widgets(self):
        self.balance = AppButton(self, "B", lambda: self.app.handle_actions("B"))
        self.withdraw = AppButton(self, "W", lambda: self.app.handle_actions("W"))
        self.deposit = AppButton(self, "D", lambda: self.app.handle_actions("D"))
        self.quit = AppButton(self, "Q", lambda: self.app.handle_actions("Q"))
    # Placement of buttons
        self.balance.grid(row=0, column=0, pady=self.pady)
        self.withdraw.grid(row=1, column=0, pady=self.pady)
        self.deposit.grid(row=2, column=0, pady=self.pady)
        self.quit.grid(row=3, column=0, pady=self.pady)



# Confirmation buttons
class ConfirmationButtons(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.pady=10
        self.create_widgets()

    def create_widgets(self):
        self.yes_btn = AppButton(self, "Y", lambda: self.app.confirmation("y"))
        self.no_btn = AppButton(self, "N", lambda: self.app.confirmation("n"))
        self.yes_btn.grid(row=1, column=1, pady=self.pady)
        self.no_btn.grid(row=2, column=1, pady=self.pady)



# Keypad buttons
class Keypad(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.pady=10
        self.create_widgets()
        self.other_widget()

    # Keypad 1-9 and 0
    def create_widgets(self):  
        self.num1 = AppButton(self, "1", lambda: self.app.keypad("1"))
        self.num2 = AppButton(self, "2", lambda: self.app.keypad("2"))
        self.num3 = AppButton(self, "3", lambda: self.app.keypad("3"))
        self.num4 = AppButton(self, "4", lambda: self.app.keypad("4"))
        self.num5 = AppButton(self, "5", lambda: self.app.keypad("5"))
        self.num6 = AppButton(self, "6", lambda: self.app.keypad("6"))
        self.num7 = AppButton(self, "7", lambda: self.app.keypad("7"))
        self.num8 = AppButton(self, "8", lambda: self.app.keypad("8"))
        self.num9 = AppButton(self, "9", lambda: self.app.keypad("9"))
        self.num0 = AppButton(self, "0", lambda: self.app.keypad("0"))
        
        
        self.num1.grid(row=0, column=0, pady=self.pady, padx=5)
        self.num2.grid(row=0, column=1, pady=self.pady, padx=5)
        self.num3.grid(row=0, column=2, pady=self.pady, padx=5)
        self.num4.grid(row=1, column=0, pady=self.pady, padx=5)
        self.num5.grid(row=1, column=1, pady=self.pady, padx=5)
        self.num6.grid(row=1, column=2, pady=self.pady, padx=5)
        self.num7.grid(row=2, column=0, pady=self.pady, padx=5)
        self.num8.grid(row=2, column=1, pady=self.pady, padx=5)
        self.num9.grid(row=2, column=2, pady=self.pady, padx=5)
        self.num0.grid(row=3, column=1, pady=self.pady, padx=5)

    # Keypad cancel and backspace
    def other_widget(self):
        self.erase = LongerButton(self, "<", lambda: self.app.erase())
        self.enter = LongerButton(self, "Enter", lambda: self.app.enter())
        self.cancel = LongerButton(self, "Cancel", lambda: self.app.cancel())
        
        self.erase.grid(row=0, column=3,pady=self.pady, padx=5)
        self.enter.grid(row=1, column=3, pady=self.pady, padx=5)
        self.cancel.grid(row=2, column=3, pady=self.pady, padx=5)

# Screenframes 
class ScreenFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        
