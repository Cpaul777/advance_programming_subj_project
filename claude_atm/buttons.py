import customtkinter as ctk

# Button Dimensions
buttonWidth = 50
buttonHeight = 50

# Longer button dimensions
longwbtn = 100
longhbtn = 50

# Color scheme
PRIMARY_COLOR = "#1f538d"
SECONDARY_COLOR = "#2980b9"
SUCCESS_COLOR = "#27ae60"
DANGER_COLOR = "#e74c3c"
LIGHT_COLOR = "#ecf0f1"
DARK_COLOR = "#2c3e50"

class AppButton(ctk.CTkButton):
    """Standard square button for main actions"""
    def __init__(self, parent, label, function, color=PRIMARY_COLOR):
        super().__init__(
            parent,
            width=buttonWidth,
            height=buttonHeight,
            command=function,
            text=label,
            font=("Arial", 14, "bold"),
            fg_color=color,
            hover_color=SECONDARY_COLOR,
            corner_radius=8,
            border_width=0
        )

class LongerButton(ctk.CTkButton):
    """Rectangular button for special actions"""
    def __init__(self, parent, label, function, color=PRIMARY_COLOR):
        super().__init__(
            parent, 
            width=longwbtn,
            height=longhbtn,
            command=function,
            text=label,
            font=("Arial", 12, "bold"),
            fg_color=color,
            hover_color=SECONDARY_COLOR,
            corner_radius=8,
            border_width=0
        )

class KeypadButton(ctk.CTkButton):
    """Keypad number button"""
    def __init__(self, parent, label, function):
        super().__init__(
            parent,
            width=60,
            height=50,
            command=function,
            text=label,
            font=("Arial", 16, "bold"),
            fg_color=LIGHT_COLOR,
            text_color=DARK_COLOR,
            hover_color="#bdc3c7",
            corner_radius=5,
            border_width=2,
            border_color=DARK_COLOR
        )

class ConfirmButton(ctk.CTkButton):
    """Green confirmation button"""
    def __init__(self, parent, label, function):
        super().__init__(
            parent,
            width=60,
            height=45,
            command=function,
            text=label,
            font=("Arial", 14, "bold"),
            fg_color=SUCCESS_COLOR,
            hover_color="#229954",
            corner_radius=8,
            border_width=0
        )

class CancelButton(ctk.CTkButton):
    """Red cancel button"""
    def __init__(self, parent, label, function):
        super().__init__(
            parent,
            width=60,
            height=45,
            command=function,
            text=label,
            font=("Arial", 14, "bold"),
            fg_color=DANGER_COLOR,
            hover_color="#c0392b",
            corner_radius=8,
            border_width=0
        )
