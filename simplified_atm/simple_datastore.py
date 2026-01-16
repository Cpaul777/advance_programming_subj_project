"""
Simplified Data Storage using Lists and Dictionaries
No database required - all data stored in memory
"""
from datetime import datetime

class BankDataStore:
    def __init__(self):
        """Initialize data storage with lists"""
        # List to store all accounts (each account is a dictionary)
        self.accounts = []
        
        # List to store all transactions (each transaction is a dictionary)
        self.transactions = []
        
        # Create demo accounts
        self.create_demo_accounts()
    
    def create_demo_accounts(self):
        """Create demo accounts for testing"""
        demo_accounts = [
            {
                "account_number": "1234567890",
                "pin": "1234",
                "name": "John Doe",
                "balance": 5000.0,
                "status": "active",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "account_number": "0987654321",
                "pin": "4321",
                "name": "Jane Smith",
                "balance": 10000.0,
                "status": "active",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            {
                "account_number": "1111222233",
                "pin": "1111",
                "name": "Bob Johnson",
                "balance": 2500.0,
                "status": "active",
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        ]
        
        # Add demo accounts to the list
        for account in demo_accounts:
            if not self.account_exists(account["account_number"]):
                self.accounts.append(account)
    
    # ==================== CREATE OPERATIONS ====================
    
    def create_account(self, account_number, pin, name, initial_balance=0.0):
        """
        Create a new account
        
        Parameters:
            account_number (str): Unique account identifier
            pin (str): 4-digit PIN
            name (str): Account holder name
            initial_balance (float): Starting balance
        
        Returns:
            bool: True if successful, False if account exists
        """
        # Check if account already exists
        if self.account_exists(account_number):
            return False
        
        # Create new account dictionary
        new_account = {
            "account_number": account_number,
            "pin": pin,
            "name": name,
            "balance": initial_balance,
            "status": "active",
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Add to accounts list
        self.accounts.append(new_account)
        
        # Log initial deposit if balance > 0
        if initial_balance > 0:
            self.add_transaction(account_number, "DEPOSIT", initial_balance, initial_balance)
        
        return True
    
    def add_transaction(self, account_number, transaction_type, amount, balance_after):
        """
        Add a transaction record
        
        Parameters:
            account_number (str): Account involved
            transaction_type (str): DEPOSIT or WITHDRAWAL
            amount (float): Transaction amount
            balance_after (float): Balance after transaction
        """
        transaction = {
            "id": len(self.transactions) + 1,  # Auto-increment ID
            "account_number": account_number,
            "transaction_type": transaction_type,
            "amount": amount,
            "balance_after": balance_after,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.transactions.append(transaction)
    
    # ==================== READ OPERATIONS ====================
    
    def account_exists(self, account_number):
        """
        Check if account exists
        
        Parameters:
            account_number (str): Account to check
        
        Returns:
            bool: True if exists, False otherwise
        """
        for account in self.accounts:
            if account["account_number"] == account_number:
                return True
        return False
    
    def get_account(self, account_number):
        """
        Get account by account number
        
        Parameters:
            account_number (str): Account to retrieve
        
        Returns:
            dict: Account dictionary or None if not found
        """
        for account in self.accounts:
            if account["account_number"] == account_number:
                return account
        return None
    
    def verify_pin(self, account_number, pin):
        """
        Verify account PIN
        
        Parameters:
            account_number (str): Account to verify
            pin (str): PIN to check
        
        Returns:
            bool: True if PIN is correct, False otherwise
        """
        account = self.get_account(account_number)
        if account and account["status"] == "active":
            return account["pin"] == pin
        return False
    
    def get_balance(self, account_number):
        """
        Get account balance
        
        Parameters:
            account_number (str): Account to check
        
        Returns:
            float: Account balance or None if not found
        """
        account = self.get_account(account_number)
        if account:
            return account["balance"]
        return None
    
    def get_account_info(self, account_number):
        """
        Get full account information
        
        Parameters:
            account_number (str): Account to retrieve
        
        Returns:
            dict: Account info or None if not found
        """
        account = self.get_account(account_number)
        if account:
            return {
                "account_number": account["account_number"],
                "name": account["name"],
                "balance": account["balance"],
                "status": account["status"],
                "created_at": account["created_at"]
            }
        return None
    
    def get_all_accounts(self):
        """
        Get all accounts
        
        Returns:
            list: List of all account dictionaries
        """
        return [
            {
                "account_number": acc["account_number"],
                "name": acc["name"],
                "balance": acc["balance"],
                "status": acc["status"]
            }
            for acc in self.accounts
        ]
    
    def get_transaction_history(self, account_number, limit=10):
        """
        Get transaction history for an account
        
        Parameters:
            account_number (str): Account to get history for
            limit (int): Maximum number of transactions to return
        
        Returns:
            list: List of transaction dictionaries
        """
        # Filter transactions for this account
        account_transactions = [
            trans for trans in self.transactions
            if trans["account_number"] == account_number
        ]
        
        # Sort by timestamp (most recent first)
        account_transactions.sort(
            key=lambda x: x["timestamp"], 
            reverse=True
        )
        
        # Return limited results
        return [
            {
                "type": trans["transaction_type"],
                "amount": trans["amount"],
                "balance_after": trans["balance_after"],
                "timestamp": trans["timestamp"]
            }
            for trans in account_transactions[:limit]
        ]
    
    # ==================== UPDATE OPERATIONS ====================
    
    def update_balance(self, account_number, new_balance):
        """
        Update account balance
        
        Parameters:
            account_number (str): Account to update
            new_balance (float): New balance value
        
        Returns:
            bool: True if successful, False if account not found
        """
        account = self.get_account(account_number)
        if account:
            account["balance"] = new_balance
            return True
        return False
    
    def deposit(self, account_number, amount):
        """
        Deposit money into account
        
        Parameters:
            account_number (str): Target account
            amount (float): Amount to deposit
        
        Returns:
            tuple: (success, new_balance or error_message)
        """
        # Validation
        account = self.get_account(account_number)
        if not account:
            return False, "Account not found"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        # Update balance
        new_balance = account["balance"] + amount
        account["balance"] = new_balance
        
        # Log transaction
        self.add_transaction(account_number, "DEPOSIT", amount, new_balance)
        
        return True, new_balance
    
    def withdraw(self, account_number, amount):
        """
        Withdraw money from account
        
        Parameters:
            account_number (str): Target account
            amount (float): Amount to withdraw
        
        Returns:
            tuple: (success, new_balance or error_message)
        """
        # Validation
        account = self.get_account(account_number)
        if not account:
            return False, "Account not found"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        if amount > account["balance"]:
            return False, "Insufficient funds"
        
        # Update balance
        new_balance = account["balance"] - amount
        account["balance"] = new_balance
        
        # Log transaction
        self.add_transaction(account_number, "WITHDRAWAL", amount, new_balance)
        
        return True, new_balance
    
    def change_pin(self, account_number, old_pin, new_pin):
        """
        Change account PIN
        
        Parameters:
            account_number (str): Account to update
            old_pin (str): Current PIN
            new_pin (str): New PIN
        
        Returns:
            tuple: (success, message)
        """
        if not self.verify_pin(account_number, old_pin):
            return False, "Invalid current PIN"
        
        account = self.get_account(account_number)
        if account:
            account["pin"] = new_pin
            return True, "PIN changed successfully"
        
        return False, "Account not found"
    
    # ==================== DELETE OPERATIONS ====================
    
    def delete_account(self, account_number):
        """
        Soft delete - mark account as closed
        
        Parameters:
            account_number (str): Account to close
        
        Returns:
            bool: True if successful, False if not found
        """
        account = self.get_account(account_number)
        if account:
            account["status"] = "closed"
            return True
        return False
    
    def hard_delete_account(self, account_number):
        """
        Permanently delete account and its transactions
        
        Parameters:
            account_number (str): Account to delete
        
        Returns:
            bool: True if successful, False if not found
        """
        # Find and remove account
        account = self.get_account(account_number)
        if not account:
            return False
        
        # Remove account from list
        self.accounts.remove(account)
        
        # Remove all transactions for this account
        self.transactions = [
            trans for trans in self.transactions
            if trans["account_number"] != account_number
        ]
        
        return True
    
    # ==================== UTILITY METHODS ====================
    
    def get_account_count(self):
        """Get total number of accounts"""
        return len(self.accounts)
    
    def get_active_account_count(self):
        """Get number of active accounts"""
        return len([acc for acc in self.accounts if acc["status"] == "active"])
    
    def get_total_balance(self):
        """Get total balance across all accounts"""
        return sum(acc["balance"] for acc in self.accounts)
    
    def clear_all_data(self):
        """Clear all accounts and transactions (use with caution!)"""
        self.accounts = []
        self.transactions = []
        self.create_demo_accounts()
