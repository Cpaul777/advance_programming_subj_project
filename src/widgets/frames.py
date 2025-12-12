import customtkinter

class WelcomeScreen:
    def __init__(self, master):
        self.master = master
        self.frame = customtkinter.CTkFrame(
            master=master,
            width=style.frameWidth,
            height=style.frameHeight,
        )
        self.frame.pack(expand=True, fill="both", padx=100 ,pady=20)

        self.label = customtkinter.CTkLabel(
            master=self.frame,
            text = "Welcome to POWERBANK\nPress OK to start",
            font = (style.screenLabelFont, 10),
        )
        self.label.pack(expand=True)

class SelectionScreen:
    def __init__(self, master):
        self.frame = customtkinter.CTkFrame(
            master=master,
            width=style.frameWidth,
            height=style.frameHeight,
            bg=master.cget("bg")
        )
        self.frame.pack(expand=True, pady=20)

        self.master = master
        
        # Balance label
        self.balance = customtkinter.CTkLabel(
            master=self.frame,
            text = "Balance",
            font = (style.screenLabelFont, style.screenLabelFontSize),
            anchor = "left",
            padx = 3,   
        )
        self.balance.pack(side="left", padx=10, pady=25)
        