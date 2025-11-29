import customtkinter
from src.style import dimensions

# Confirmation buttons
# class confirmationButtons:
#     def __init__(self, master):
#         self.master = master
#         self.create_buttons()

#     def create_buttons(self):
#         self.confirm_yes = customtkinter.CTkButton(
#             master=self.master,
#             text="Y",
#             width=dimensions.buttonWidth,
#             height=dimensions.buttonHeight,
#         )

#         self.confirm_no = customtkinter.CTkButton(
#             master=self.master,
#             text="N",
#             width=dimensions.buttonWidth,
#             height=dimensions.buttonHeight,
#         )

#         self.confirm_yes.pack(pady = 5)
#         self.confirm_no.pack(pady = 10)

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

# def button_event():
#     print('button pressed')

# deposit = customtkinter.CTkButton(app, text='CTkButton', width=140, height=28, command=button_event)
# deposit.place(x=10, y=10)
