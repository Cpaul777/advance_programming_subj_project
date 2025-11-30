import customtkinter
from src.style import style

class ConfirmButtons: 
    def __init__(self, master):
        self.master = master
        self.frame = customtkinter.CTkFrame(
            master=master,
            width=style.confirmFrameWidth,
            height=style.confirmFrameHeight,
            fg_color=master.cget("bg")
        )

        self.frame.pack(expand=True, fill="y", side="right")
    
        self.confirm_yes = customtkinter.CTkButton(
            master=self.frame,
            text="Y",
            width=style.buttonWidth,
            height=style.buttonHeight,
        )

        self.confirm_no = customtkinter.CTkButton(
            master=self.frame,
            text="N",
            width=style.buttonWidth,
            height=style.buttonHeight,
        )

        self.confirm_yes.pack(pady=10)
        self.confirm_no.pack(pady=10)

    # def confirm_yes(self):
    #     self.confirm_yes = customtkinter.CTkButton(
    #         master=self.frame,
    #         text="Y",
    #         width=style.buttonWidth,
    #         height=style.buttonHeight,
            
    #     )
        

    # def confirm_no(self):        
    #     self.confirm_no = customtkinter.CTkButton(
    #        master=self.frame,
    #         text="Y",
    #         width=style.buttonWidth,
    #         height=style.buttonHeight,
    #     )
    #     self.confirm_yes.pack()
    #     self.confirm_no.pack()


class ActionButtons:
    def __init__(self, master):
        self.master = master
        self.frame = customtkinter.CTkFrame(
            master=master,
            width=style.actionFrameWidth,
            height=style.actionFrameHeight,
            fg_color=master.cget("bg")
        )
        self.frame.pack(expand=True, fill="y", side="left")

    def balance(self):
        self.balance_button = customtkinter.CTkButton(
            master=self.frame,
            text="B",
            width=style.buttonWidth,
            height=style.buttonHeight,
        )
        self.balance_button.grid(row=2, column=0)
    
    def deposit(self):
        self.deposit_button = customtkinter.CTkButton(
            master=self.frame,
            text="D",
            width=style.buttonWidth,
            height=style.buttonHeight,
        )
        self.deposit_button.grid(row=1, column=0)

# # Action buttons
# back_button = customtkinter.CTkButton(
#     text="B",
#     width=dimensions.buttonWidth,
#     height=dimensions.buttonHeight,

# )

