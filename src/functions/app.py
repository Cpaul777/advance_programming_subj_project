import customtkinter as ctk
from src.widgets import buttons

app = ctk.CTk()
app.title("App Banking System")
app.geometry("500x300")

# Just for testing purposes
app.ada = ctk.CTkButton(app, text="DID THIS WORK?")
app.ada.pack(pady=50)

# Confirmation Buttons
buttons.confirm_yes(app)
buttons.confirm_no(app)

# Action Buttons
# buttons.back_button(app)



