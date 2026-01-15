import customtkinter as ctk
from database import BankDatabase
import tkinter.messagebox as messagebox

# Color scheme
PRIMARY_COLOR = "#1f538d"
SECONDARY_COLOR = "#2980b9"
SUCCESS_COLOR = "#27ae60"
DANGER_COLOR = "#e74c3c"
LIGHT_COLOR = "#ecf0f1"
DARK_COLOR = "#2c3e50"
BG_COLOR = "#34495e"

class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.geometry("900x600")
        self.title("ATM Banking System - Admin Panel")
        self.configure(fg_color=BG_COLOR)
        
        # Database
        self.db = BankDatabase()
        
        # Grid configuration
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Title
        title = ctk.CTkLabel(
            self,
            text="Account Management System",
            font=("Arial", 28, "bold"),
            text_color=LIGHT_COLOR
        )
        title.grid(row=0, column=0, pady=20, padx=20)
        
        # Main container
        self.main_container = ctk.CTkFrame(self, fg_color="transparent")
        self.main_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(1, weight=1)
        self.main_container.grid_rowconfigure(1, weight=1)
        
        # Left side - Account list
        self.create_account_list()
        
        # Right side - Account operations
        self.create_operations_panel()
        
        # Load accounts
        self.refresh_accounts()
    
    def create_account_list(self):
        """Create the account list section"""
        list_frame = ctk.CTkFrame(self.main_container, fg_color=DARK_COLOR, corner_radius=10)
        list_frame.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(0, 10))
        list_frame.grid_rowconfigure(1, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        list_title = ctk.CTkLabel(
            list_frame,
            text="All Accounts",
            font=("Arial", 18, "bold"),
            text_color=LIGHT_COLOR
        )
        list_title.grid(row=0, column=0, pady=10, padx=10)
        
        # Scrollable frame for accounts
        self.accounts_scroll = ctk.CTkScrollableFrame(list_frame, fg_color=LIGHT_COLOR)
        self.accounts_scroll.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
        self.accounts_scroll.grid_columnconfigure(0, weight=1)
        
        # Refresh button
        refresh_btn = ctk.CTkButton(
            list_frame,
            text="Refresh List",
            command=self.refresh_accounts,
            fg_color=PRIMARY_COLOR,
            hover_color=SECONDARY_COLOR,
            font=("Arial", 12, "bold")
        )
        refresh_btn.grid(row=2, column=0, pady=10, padx=10)
    
    def create_operations_panel(self):
        """Create the operations panel"""
        ops_frame = ctk.CTkFrame(self.main_container, fg_color=DARK_COLOR, corner_radius=10)
        ops_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        ops_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        ops_title = ctk.CTkLabel(
            ops_frame,
            text="Account Operations",
            font=("Arial", 18, "bold"),
            text_color=LIGHT_COLOR
        )
        ops_title.pack(pady=15, padx=10)
        
        # Create Account Section
        create_frame = ctk.CTkFrame(ops_frame, fg_color=LIGHT_COLOR, corner_radius=8)
        create_frame.pack(pady=10, padx=15, fill="x")
        
        ctk.CTkLabel(create_frame, text="Create New Account", font=("Arial", 14, "bold"), text_color=DARK_COLOR).pack(pady=5)
        
        # Account number
        ctk.CTkLabel(create_frame, text="Account Number:", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.new_acc_num = ctk.CTkEntry(create_frame, width=250)
        self.new_acc_num.pack(pady=5)
        
        # Name
        ctk.CTkLabel(create_frame, text="Account Holder Name:", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.new_acc_name = ctk.CTkEntry(create_frame, width=250)
        self.new_acc_name.pack(pady=5)
        
        # PIN
        ctk.CTkLabel(create_frame, text="PIN (4 digits):", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.new_acc_pin = ctk.CTkEntry(create_frame, width=250, show="*")
        self.new_acc_pin.pack(pady=5)
        
        # Initial balance
        ctk.CTkLabel(create_frame, text="Initial Balance:", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.new_acc_balance = ctk.CTkEntry(create_frame, width=250)
        self.new_acc_balance.insert(0, "0.00")
        self.new_acc_balance.pack(pady=5)
        
        # Create button
        create_btn = ctk.CTkButton(
            create_frame,
            text="Create Account",
            command=self.create_account,
            fg_color=SUCCESS_COLOR,
            hover_color="#229954",
            font=("Arial", 12, "bold")
        )
        create_btn.pack(pady=10)
        
        # Update/Delete Section
        modify_frame = ctk.CTkFrame(ops_frame, fg_color=LIGHT_COLOR, corner_radius=8)
        modify_frame.pack(pady=10, padx=15, fill="x")
        
        ctk.CTkLabel(modify_frame, text="Modify Account", font=("Arial", 14, "bold"), text_color=DARK_COLOR).pack(pady=5)
        
        # Account number to modify
        ctk.CTkLabel(modify_frame, text="Account Number:", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.mod_acc_num = ctk.CTkEntry(modify_frame, width=250)
        self.mod_acc_num.pack(pady=5)
        
        # Buttons
        btn_frame = ctk.CTkFrame(modify_frame, fg_color="transparent")
        btn_frame.pack(pady=10)
        
        view_btn = ctk.CTkButton(
            btn_frame,
            text="View Details",
            command=self.view_account,
            fg_color=PRIMARY_COLOR,
            hover_color=SECONDARY_COLOR,
            width=110
        )
        view_btn.grid(row=0, column=0, padx=5)
        
        delete_btn = ctk.CTkButton(
            btn_frame,
            text="Delete Account",
            command=self.delete_account,
            fg_color=DANGER_COLOR,
            hover_color="#c0392b",
            width=110
        )
        delete_btn.grid(row=0, column=1, padx=5)
        
        # Transaction History Section
        history_frame = ctk.CTkFrame(ops_frame, fg_color=LIGHT_COLOR, corner_radius=8)
        history_frame.pack(pady=10, padx=15, fill="x")
        
        ctk.CTkLabel(history_frame, text="Transaction History", font=("Arial", 14, "bold"), text_color=DARK_COLOR).pack(pady=5)
        
        ctk.CTkLabel(history_frame, text="Account Number:", text_color=DARK_COLOR).pack(pady=(5, 0))
        self.history_acc_num = ctk.CTkEntry(history_frame, width=250)
        self.history_acc_num.pack(pady=5)
        
        history_btn = ctk.CTkButton(
            history_frame,
            text="View History",
            command=self.view_history,
            fg_color=PRIMARY_COLOR,
            hover_color=SECONDARY_COLOR
        )
        history_btn.pack(pady=10)
    
    def refresh_accounts(self):
        """Refresh the account list"""
        # Clear existing widgets
        for widget in self.accounts_scroll.winfo_children():
            widget.destroy()
        
        # Get all accounts
        accounts = self.db.get_all_accounts()
        
        if not accounts:
            no_acc_label = ctk.CTkLabel(
                self.accounts_scroll,
                text="No accounts found",
                font=("Arial", 12),
                text_color=DARK_COLOR
            )
            no_acc_label.pack(pady=20)
            return
        
        # Display accounts
        for acc in accounts:
            acc_frame = ctk.CTkFrame(self.accounts_scroll, fg_color="white", corner_radius=5)
            acc_frame.pack(pady=5, padx=5, fill="x")
            
            status_color = SUCCESS_COLOR if acc['status'] == 'active' else DANGER_COLOR
            
            info_text = f"Account: {acc['account_number']}\nName: {acc['name']}\nBalance: ₱{acc['balance']:,.2f}\nStatus: {acc['status'].upper()}"
            
            acc_label = ctk.CTkLabel(
                acc_frame,
                text=info_text,
                font=("Arial", 11),
                text_color=DARK_COLOR,
                justify="left"
            )
            acc_label.pack(pady=8, padx=10, anchor="w")
            
            # Status indicator
            status_dot = ctk.CTkLabel(
                acc_frame,
                text="●",
                font=("Arial", 20),
                text_color=status_color
            )
            status_dot.place(relx=0.95, rely=0.5, anchor="center")
    
    def create_account(self):
        """Create a new account"""
        acc_num = self.new_acc_num.get().strip()
        name = self.new_acc_name.get().strip()
        pin = self.new_acc_pin.get().strip()
        balance_str = self.new_acc_balance.get().strip()
        
        # Validation
        if not acc_num or not name or not pin:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if len(pin) != 4 or not pin.isdigit():
            messagebox.showerror("Error", "PIN must be exactly 4 digits!")
            return
        
        try:
            balance = float(balance_str)
            if balance < 0:
                messagebox.showerror("Error", "Balance cannot be negative!")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid balance amount!")
            return
        
        # Create account
        success = self.db.create_account(acc_num, pin, name, balance)
        
        if success:
            messagebox.showinfo("Success", f"Account {acc_num} created successfully!")
            self.new_acc_num.delete(0, 'end')
            self.new_acc_name.delete(0, 'end')
            self.new_acc_pin.delete(0, 'end')
            self.new_acc_balance.delete(0, 'end')
            self.new_acc_balance.insert(0, "0.00")
            self.refresh_accounts()
        else:
            messagebox.showerror("Error", "Account number already exists!")
    
    def view_account(self):
        """View account details"""
        acc_num = self.mod_acc_num.get().strip()
        
        if not acc_num:
            messagebox.showerror("Error", "Please enter an account number!")
            return
        
        account = self.db.get_account_info(acc_num)
        
        if account:
            info = f"""
Account Number: {account['account_number']}
Name: {account['name']}
Balance: ₱{account['balance']:,.2f}
Status: {account['status'].upper()}
Created: {account['created_at']}
            """
            messagebox.showinfo("Account Details", info)
        else:
            messagebox.showerror("Error", "Account not found!")
    
    def delete_account(self):
        """Delete an account"""
        acc_num = self.mod_acc_num.get().strip()
        
        if not acc_num:
            messagebox.showerror("Error", "Please enter an account number!")
            return
        
        account = self.db.get_account_info(acc_num)
        
        if not account:
            messagebox.showerror("Error", "Account not found!")
            return
        
        # Confirm deletion
        confirm = messagebox.askyesno(
            "Confirm Deletion",
            f"Are you sure you want to delete account {acc_num}?\nName: {account['name']}\nBalance: ₱{account['balance']:,.2f}\n\nThis action cannot be undone!"
        )
        
        if confirm:
            self.db.hard_delete_account(acc_num)
            messagebox.showinfo("Success", f"Account {acc_num} has been deleted!")
            self.mod_acc_num.delete(0, 'end')
            self.refresh_accounts()
    
    def view_history(self):
        """View transaction history"""
        acc_num = self.history_acc_num.get().strip()
        
        if not acc_num:
            messagebox.showerror("Error", "Please enter an account number!")
            return
        
        if not self.db.account_exists(acc_num):
            messagebox.showerror("Error", "Account not found!")
            return
        
        # Create history window
        history_window = ctk.CTkToplevel(self)
        history_window.title(f"Transaction History - {acc_num}")
        history_window.geometry("600x400")
        history_window.configure(fg_color=BG_COLOR)
        
        # Title
        title = ctk.CTkLabel(
            history_window,
            text=f"Transaction History\nAccount: {acc_num}",
            font=("Arial", 18, "bold"),
            text_color=LIGHT_COLOR
        )
        title.pack(pady=15)
        
        # Scrollable frame
        scroll_frame = ctk.CTkScrollableFrame(history_window, fg_color=LIGHT_COLOR)
        scroll_frame.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        
        # Get transactions
        transactions = self.db.get_transaction_history(acc_num, limit=50)
        
        if not transactions:
            no_trans = ctk.CTkLabel(
                scroll_frame,
                text="No transactions found",
                font=("Arial", 14),
                text_color=DARK_COLOR
            )
            no_trans.pack(pady=20)
        else:
            for trans in transactions:
                trans_frame = ctk.CTkFrame(scroll_frame, fg_color="white", corner_radius=5)
                trans_frame.pack(pady=5, padx=5, fill="x")
                
                trans_type = trans['type']
                color = SUCCESS_COLOR if trans_type == "DEPOSIT" else DANGER_COLOR
                
                trans_text = f"{trans_type} - ₱{trans['amount']:,.2f}\nBalance After: ₱{trans['balance_after']:,.2f}\n{trans['timestamp']}"
                
                trans_label = ctk.CTkLabel(
                    trans_frame,
                    text=trans_text,
                    font=("Arial", 11),
                    text_color=DARK_COLOR,
                    justify="left"
                )
                trans_label.pack(pady=8, padx=10, anchor="w")
                
                # Type indicator
                type_label = ctk.CTkLabel(
                    trans_frame,
                    text=trans_type[0],
                    font=("Arial", 16, "bold"),
                    text_color=color
                )
                type_label.place(relx=0.95, rely=0.5, anchor="center")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    admin = AdminPanel()
    admin.mainloop()
