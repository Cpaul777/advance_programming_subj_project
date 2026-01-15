"""
ATM Banking System Launcher
Choose which application to run
"""
import customtkinter as ctk
import subprocess
import sys

class Launcher(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("400x300")
        self.title("ATM Banking System - Launcher")
        self.configure(fg_color="#34495e")
        
        # Title
        title = ctk.CTkLabel(
            self,
            text="ATM Banking System",
            font=("Arial", 28, "bold"),
            text_color="#ecf0f1"
        )
        title.pack(pady=30)
        
        subtitle = ctk.CTkLabel(
            self,
            text="Choose an application to launch:",
            font=("Arial", 14),
            text_color="#ecf0f1"
        )
        subtitle.pack(pady=10)
        
        # ATM Button
        atm_btn = ctk.CTkButton(
            self,
            text="ATM Interface",
            command=self.launch_atm,
            font=("Arial", 16, "bold"),
            fg_color="#1f538d",
            hover_color="#2980b9",
            width=250,
            height=50,
            corner_radius=10
        )
        atm_btn.pack(pady=15)
        
        # Admin Panel Button
        admin_btn = ctk.CTkButton(
            self,
            text="Admin Panel",
            command=self.launch_admin,
            font=("Arial", 16, "bold"),
            fg_color="#27ae60",
            hover_color="#229954",
            width=250,
            height=50,
            corner_radius=10
        )
        admin_btn.pack(pady=15)
        
        # Exit Button
        exit_btn = ctk.CTkButton(
            self,
            text="Exit",
            command=self.quit,
            font=("Arial", 14, "bold"),
            fg_color="#e74c3c",
            hover_color="#c0392b",
            width=150,
            height=40,
            corner_radius=10
        )
        exit_btn.pack(pady=20)
    
    def launch_atm(self):
        """Launch ATM interface"""
        subprocess.Popen([sys.executable, "app.py"])
    
    def launch_admin(self):
        """Launch Admin panel"""
        subprocess.Popen([sys.executable, "admin_panel.py"])

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    launcher = Launcher()
    launcher.mainloop()
