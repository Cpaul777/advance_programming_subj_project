import customtkinter as ctk

# Button Dimensions
buttonWidth = 40
buttonHeight = 30

class AppButton(ctk.CTkButton):
    def __init__(self, parent, label, function):
        super().__init__(
            parent,
            width = buttonWidth,
            height = buttonHeight,
            command = function,
            text = label
        )