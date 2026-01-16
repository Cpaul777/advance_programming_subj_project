import customtkinter as ctk
from buttons import AppButton, LongerButton, KeypadButton, ConfirmButton, CancelButton

# Color scheme
PRIMARY_COLOR = "#1f538d"
SECONDARY_COLOR = "#2980b9"
SUCCESS_COLOR = "#27ae60"
DANGER_COLOR = "#e74c3c"
LIGHT_COLOR = "#ecf0f1"
DARK_COLOR = "#2c3e50"
BG_COLOR = "#34495e"

# Action Frame buttons (B, D, W, Q on the left)
class ActionFrame(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.pady = 15
        self.create_widgets()

    def create_widgets(self):
        # Action buttons with labels
        self.balance = AppButton(self, "B", lambda: self.app.handle_actions("B"))
        self.deposit = AppButton(self, "D", lambda: self.app.handle_actions("D"))
        self.withdraw = AppButton(self, "W", lambda: self.app.handle_actions("W"))
        self.quit = AppButton(self, "Q", lambda: self.app.handle_actions("Q"), color=DANGER_COLOR)
        
        # Placement
        self.balance.grid(row=0, column=0, pady=self.pady)
        self.deposit.grid(row=1, column=0, pady=self.pady)
        self.withdraw.grid(row=2, column=0, pady=self.pady)
        self.quit.grid(row=3, column=0, pady=self.pady)

# Confirmation buttons (Y, N on the right)
class ConfirmationButtons(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color="transparent")
        self.app = app
        self.pady = 15
        self.create_widgets()

    def create_widgets(self):
        self.yes_btn = ConfirmButton(self, "Yes", lambda: self.app.handle_confirmation("y"))
        self.no_btn = CancelButton(self, "No", lambda: self.app.handle_confirmation("n"))
        
        self.yes_btn.grid(row=0, column=0, pady=self.pady)
        self.no_btn.grid(row=1, column=0, pady=self.pady)

# Keypad buttons (1-9, 0, and control buttons)
class Keypad(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent, fg_color=BG_COLOR, corner_radius=10)
        self.app = app
        self.pady = 5
        self.padx = 5
        self.create_widgets()
        self.other_widgets()

    def create_widgets(self):  
        # Create number buttons 1-9 and 0
        buttons = [
            (1, 0, 0), (2, 0, 1), (3, 0, 2),
            (4, 1, 0), (5, 1, 1), (6, 1, 2),
            (7, 2, 0), (8, 2, 1), (9, 2, 2),
            (0, 3, 1)
        ]
        
        self.number_buttons = {}
        for num, row, col in buttons:
            btn = KeypadButton(self, str(num), lambda n=num: self.app.handle_keypad(str(n)))
            btn.grid(row=row, column=col, pady=self.pady, padx=self.padx)
            self.number_buttons[num] = btn

    def other_widgets(self):
        # Control buttons
        self.clear_btn = LongerButton(self, "Clear", lambda: self.app.handle_clear(), color=DANGER_COLOR)
        self.enter = LongerButton(self, "Enter", lambda: self.app.handle_enter(), color=SUCCESS_COLOR)
        self.cancel = LongerButton(self, "Cancel", lambda: self.app.handle_cancel(), color=DANGER_COLOR)
        
        self.clear_btn.grid(row=0, column=3, pady=self.pady, padx=self.padx, rowspan=1)
        self.enter.grid(row=1, column=3, pady=self.pady, padx=self.padx, rowspan=1)
        self.cancel.grid(row=2, column=3, pady=self.pady, padx=self.padx, rowspan=2)

# Screen frame - main display area
class ScreenFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=LIGHT_COLOR, corner_radius=10, border_width=3, border_color=DARK_COLOR)
        
        # Configure grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Main container
        self.content_frame = ctk.CTkFrame(self, fg_color=LIGHT_COLOR)
        self.content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        # Title label
        self.title_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=("Arial", 24, "bold"),
            text_color=DARK_COLOR
        )
        self.title_label.pack(pady=(0, 20))
        
        # Message label
        self.message_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=("Arial", 16),
            text_color=DARK_COLOR,
            wraplength=400,
            justify="center"
        )
        self.message_label.pack(pady=10)
        
        # Input display (for PIN and amounts)
        self.input_frame = ctk.CTkFrame(self.content_frame, fg_color="white", corner_radius=5, border_width=2, border_color=DARK_COLOR)
        self.input_label = ctk.CTkLabel(
            self.input_frame,
            text="",
            font=("Arial", 20, "bold"),
            text_color=DARK_COLOR,
            width=300,
            height=40
        )
        self.input_label.pack(padx=10, pady=10)
        
        # Additional info label (for balance, etc.)
        self.info_label = ctk.CTkLabel(
            self.content_frame,
            text="",
            font=("Arial", 18, "bold"),
            text_color=PRIMARY_COLOR
        )
        
    def show_input(self):
        """Show the input frame"""
        self.input_frame.pack(pady=20)
    
    def hide_input(self):
        """Hide the input frame"""
        self.input_frame.pack_forget()
    
    def show_info(self):
        """Show the info label"""
        self.info_label.pack(pady=10)
    
    def hide_info(self):
        """Hide the info label"""
        self.info_label.pack_forget()
    
    def update_title(self, text):
        """Update the title text"""
        self.title_label.configure(text=text)
    
    def update_message(self, text):
        """Update the message text"""
        self.message_label.configure(text=text)
    
    def update_input(self, text, masked=False):
        """Update the input display"""
        if masked:
            self.input_label.configure(text="*" * len(text))
        else:
            self.input_label.configure(text=text)
    
    def update_info(self, text):
        """Update the info label"""
        self.info_label.configure(text=text)
    
    def clear_screen(self):
        """Clear all screen content"""
        self.title_label.configure(text="")
        self.message_label.configure(text="")
        self.input_label.configure(text="")
        self.info_label.configure(text="")
        self.hide_input()
        self.hide_info()
