import customtkinter
from src.style import dimensions

def confirm_yes(master):
    master.confirm_yes = customtkinter.CTkButton(
        master=master,
        text="adadad",
        width=dimensions.buttonWidth,
        height=dimensions.buttonHeight,
    )
    master.confirm_yes.pack(pady=5)

def confirm_no(master):        
    master.confirm_no = customtkinter.CTkButton(
        master=master,
        text="N",
        width=dimensions.buttonWidth,
        height=dimensions.buttonHeight,
    )

    master.confirm_no.pack(pady=10, padx=20)

# # Action buttons
# back_button = customtkinter.CTkButton(
#     text="B",
#     width=dimensions.buttonWidth,
#     height=dimensions.buttonHeight,

# )

