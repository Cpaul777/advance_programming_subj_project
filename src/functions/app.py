import customtkinter as ctk
from src.style import style
from src.widgets import buttons, frames

app = ctk.CTk()
app.title("App Banking System")
app.geometry(f"{style.windowWidth}x{style.windowHeight}")
app.resizable(False,False)

# Confirmation Buttons
buttons.ConfirmButtons(app)

#Action buttons
buttons.ActionButtons(app).balance()
buttons.ActionButtons(app).deposit()
# frame screen
frames.WelcomeScreen(app)

# Just for testing purposes
app.ada = ctk.CTkButton(app, text="DID THIS WORK?")
app.ada.pack(pady=50)



# Action Buttons
# buttons.back_button(app)



