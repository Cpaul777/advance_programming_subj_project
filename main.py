
import customtkinter as ctk

app = ctk.CTk()
app.title("App Banking System")
app.geometry("400x300")

button = ctk.CTkButton(app, text="click me")
button.pack()

if __name__ == "__main__":
    app.mainloop()