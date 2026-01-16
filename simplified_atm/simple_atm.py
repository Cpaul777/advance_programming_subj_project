import customtkinter as ctk
from frames import ActionFrame, ConfirmationButtons, Keypad, ScreenFrame
from simple_datastore import BankDataStore

# Color scheme
BG_COLOR = "#34495e"

class SimpleATM(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window setup
        self.geometry("1000x700")
        self.title("Simple ATM Banking System")
        self.configure(fg_color=BG_COLOR)
        
        # Data store (using lists instead of database)
        self.data_store = BankDataStore()
        
        # State management
        self.windowState = "INSERT_CARD"
        self.current_account = None
        self.current_input = ""
        self.pending_amount = 0
        self.pin_attempts = 0
        self.max_pin_attempts = 3
        
        # Grid configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        
        # Create frames
        self.action_btns = ActionFrame(self, self)
        self.screen_frame = ScreenFrame(self)
        self.confirmation = ConfirmationButtons(self, self)
        self.keypad = Keypad(self, self)
        
        # Place frames
        self.screen_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.action_btns.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ns")
        self.confirmation.grid(row=0, column=2, padx=(5, 10), pady=10, sticky="ns")
        self.keypad.grid(row=1, column=0, columnspan=3, padx=10, pady=(0, 10))
        
        # Initialize screen
        self.update_screen()
    
    def update_screen(self):
        """Update screen based on current state"""
        self.screen_frame.clear_screen()
        
        if self.windowState == "INSERT_CARD":
            self.screen_frame.update_title("Welcome to PAYAMANÈ")
            self.screen_frame.update_message("Please enter your account number\nPress Enter to continue")
            self.screen_frame.show_input()
            self.screen_frame.update_input(self.current_input)
            
        elif self.windowState == "ENTER_PIN":
            self.screen_frame.update_title("Enter PIN")
            self.screen_frame.update_message(f"Please enter your 4-digit PIN\n({self.max_pin_attempts - self.pin_attempts} attempts remaining)")
            self.screen_frame.show_input()
            self.screen_frame.update_input(self.current_input, masked=True)
            
        elif self.windowState == "MENU":
            account_info = self.data_store.get_account_info(self.current_account)
            if account_info:
                self.screen_frame.update_title("Main Menu")
                self.screen_frame.update_message(f"Welcome, {account_info['name']}!\n\nPlease select a transaction:\n\nB - Balance\nD - Deposit\nW - Withdraw\nQ - Quit")
            
        elif self.windowState == "BALANCE":
            balance = self.data_store.get_balance(self.current_account)
            self.screen_frame.update_title("Balance Inquiry")
            self.screen_frame.update_message("Your current balance is:")
            self.screen_frame.show_info()
            self.screen_frame.update_info(f"₱ {balance:,.2f}")
            self.screen_frame.update_message("Your current balance is:\n\nWould you like another transaction?")
            
        elif self.windowState == "WITHDRAW":
            self.screen_frame.update_title("Withdraw")
            self.screen_frame.update_message("Enter amount to withdraw:\n(Maximum ₱20,000 per transaction)")
            self.screen_frame.show_input()
            if self.current_input:
                self.screen_frame.update_input(f"₱ {self.current_input}")
            else:
                self.screen_frame.update_input("")
                
        elif self.windowState == "DEPOSIT":
            self.screen_frame.update_title("Deposit")
            self.screen_frame.update_message("Enter amount to deposit:")
            self.screen_frame.show_input()
            if self.current_input:
                self.screen_frame.update_input(f"₱ {self.current_input}")
            else:
                self.screen_frame.update_input("")
                
        elif self.windowState == "CONFIRM_WITHDRAW":
            self.screen_frame.update_title("Confirm Withdrawal")
            self.screen_frame.update_message(f"Withdraw ₱ {self.pending_amount:,.2f}?\n\nPress Yes to confirm or No to cancel")
            
        elif self.windowState == "CONFIRM_DEPOSIT":
            self.screen_frame.update_title("Confirm Deposit")
            self.screen_frame.update_message(f"Deposit ₱ {self.pending_amount:,.2f}?\n\nPress Yes to confirm or No to cancel")
            
        elif self.windowState == "SUCCESS_WITHDRAW":
            new_balance = self.data_store.get_balance(self.current_account)
            self.screen_frame.update_title("Transaction Successful")
            self.screen_frame.update_message(f"Successfully withdrawn ₱ {self.pending_amount:,.2f}")
            self.screen_frame.show_info()
            self.screen_frame.update_info(f"New Balance: ₱ {new_balance:,.2f}")
            self.screen_frame.update_message(f"Successfully withdrawn ₱ {self.pending_amount:,.2f}\n\nWould you like another transaction?")
            
        elif self.windowState == "SUCCESS_DEPOSIT":
            new_balance = self.data_store.get_balance(self.current_account)
            self.screen_frame.update_title("Transaction Successful")
            self.screen_frame.update_message(f"Successfully deposited ₱ {self.pending_amount:,.2f}")
            self.screen_frame.show_info()
            self.screen_frame.update_info(f"New Balance: ₱ {new_balance:,.2f}")
            self.screen_frame.update_message(f"Successfully deposited ₱ {self.pending_amount:,.2f}\n\nWould you like another transaction?")
            
        elif self.windowState == "ERROR":
            self.screen_frame.update_title("Error")
            self.screen_frame.update_message(self.error_message)
            
        elif self.windowState == "GOODBYE":
            self.screen_frame.update_title("Thank You!")
            self.screen_frame.update_message("Thank you for using PAYAMANÈ\nPlease take your card")
    
    def handle_keypad(self, digit):
        """Handle keypad number input"""
        if self.windowState in ["INSERT_CARD", "ENTER_PIN", "WITHDRAW", "DEPOSIT"]:
            self.current_input += digit
            self.update_screen()
    
    def handle_clear(self):
        """Clear the current input"""
        if len(self.current_input) > 0:
            self.current_input = self.current_input[:-1]
            self.update_screen()
    
    def handle_enter(self):
        """Handle enter button press"""
        if self.windowState == "INSERT_CARD":
            if len(self.current_input) >= 4:
                if self.data_store.account_exists(self.current_input):
                    self.current_account = self.current_input
                    self.current_input = ""
                    self.windowState = "ENTER_PIN"
                    self.pin_attempts = 0
                    self.update_screen()
                else:
                    self.show_error("Account not found. Please try again.")
                    self.current_input = ""
                    self.update_screen()
            else:
                self.show_error("Please enter a valid account number")
                
        elif self.windowState == "ENTER_PIN":
            if len(self.current_input) == 4:
                if self.data_store.verify_pin(self.current_account, self.current_input):
                    self.current_input = ""
                    self.windowState = "MENU"
                    self.update_screen()
                else:
                    self.pin_attempts += 1
                    if self.pin_attempts >= self.max_pin_attempts:
                        self.show_error("Too many incorrect attempts. Card retained.")
                        self.after(3000, self.reset_session)
                    else:
                        self.current_input = ""
                        self.update_screen()
            else:
                self.show_error("PIN must be 4 digits")
                
        elif self.windowState == "WITHDRAW":
            if self.current_input:
                try:
                    amount = float(self.current_input)
                    if amount <= 0:
                        self.show_error("Amount must be greater than zero")
                    elif amount > 20000:
                        self.show_error("Maximum withdrawal is ₱20,000")
                    elif amount > self.data_store.get_balance(self.current_account):
                        self.show_error("Insufficient funds")
                    else:
                        self.pending_amount = amount
                        self.current_input = ""
                        self.windowState = "CONFIRM_WITHDRAW"
                        self.update_screen()
                except ValueError:
                    self.show_error("Invalid amount")
                    
        elif self.windowState == "DEPOSIT":
            if self.current_input:
                try:
                    amount = float(self.current_input)
                    if amount <= 0:
                        self.show_error("Amount must be greater than zero")
                    elif amount > 50000:
                        self.show_error("Maximum deposit is ₱50,000 per transaction")
                    else:
                        self.pending_amount = amount
                        self.current_input = ""
                        self.windowState = "CONFIRM_DEPOSIT"
                        self.update_screen()
                except ValueError:
                    self.show_error("Invalid amount")
    
    def handle_cancel(self):
        """Handle cancel button press"""
        if self.windowState in ["INSERT_CARD", "ENTER_PIN"]:
            self.reset_session()
        else:
            self.current_input = ""
            self.windowState = "MENU"
            self.update_screen()
    
    def handle_actions(self, action):
        """Handle action button presses (B, D, W, Q)"""
        if self.windowState == "MENU":
            if action == "B":
                self.windowState = "BALANCE"
                self.update_screen()
            elif action == "W":
                self.current_input = ""
                self.windowState = "WITHDRAW"
                self.update_screen()
            elif action == "D":
                self.current_input = ""
                self.windowState = "DEPOSIT"
                self.update_screen()
            elif action == "Q":
                self.windowState = "GOODBYE"
                self.update_screen()
                self.after(2000, self.reset_session)
    
    def handle_confirmation(self, response):
        """Handle yes/no confirmation"""
        if response == "y":  # Yes
            if self.windowState == "CONFIRM_WITHDRAW":
                success, result = self.data_store.withdraw(self.current_account, self.pending_amount)
                if success:
                    self.windowState = "SUCCESS_WITHDRAW"
                    self.update_screen()
                else:
                    self.show_error(result)
                    
            elif self.windowState == "CONFIRM_DEPOSIT":
                success, result = self.data_store.deposit(self.current_account, self.pending_amount)
                if success:
                    self.windowState = "SUCCESS_DEPOSIT"
                    self.update_screen()
                else:
                    self.show_error(result)
                    
            elif self.windowState in ["BALANCE", "SUCCESS_WITHDRAW", "SUCCESS_DEPOSIT"]:
                # Another transaction
                self.windowState = "MENU"
                self.update_screen()
                
        elif response == "n":  # No
            if self.windowState in ["CONFIRM_WITHDRAW", "CONFIRM_DEPOSIT"]:
                self.windowState = "MENU"
                self.pending_amount = 0
                self.update_screen()
            elif self.windowState in ["BALANCE", "SUCCESS_WITHDRAW", "SUCCESS_DEPOSIT"]:
                # No more transactions
                self.windowState = "GOODBYE"
                self.update_screen()
                self.after(2000, self.reset_session)
    
    def show_error(self, message):
        """Show error message"""
        self.error_message = message
        previous_state = self.windowState
        self.windowState = "ERROR"
        self.update_screen()
        self.after(2000, lambda: self.return_from_error(previous_state))
    
    def return_from_error(self, previous_state):
        """Return to previous state after error"""
        self.windowState = previous_state
        self.current_input = ""
        self.update_screen()
    
    def reset_session(self):
        """Reset the session to initial state"""
        self.current_account = None
        self.current_input = ""
        self.pending_amount = 0
        self.pin_attempts = 0
        self.windowState = "INSERT_CARD"
        self.update_screen()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    app = SimpleATM()
    app.mainloop()
