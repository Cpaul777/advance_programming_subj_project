import sqlite3
import json
from datetime import datetime
from pathlib import Path
import time

class BankDatabase:
    def __init__(self, db_name="bank_system.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Get database connection with timeout and proper isolation level"""
        conn = sqlite3.connect(self.db_name, timeout=10.0, check_same_thread=False)
        conn.isolation_level = None  # Autocommit mode
        return conn
    
    def init_database(self):
        """Create tables if they don't exist"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Create accounts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS accounts (
                    account_number TEXT PRIMARY KEY,
                    pin TEXT NOT NULL,
                    balance REAL DEFAULT 0.0,
                    name TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    status TEXT DEFAULT 'active'
                )
            ''')
            
            # Create transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    account_number TEXT NOT NULL,
                    transaction_type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    balance_after REAL NOT NULL,
                    timestamp TEXT NOT NULL,
                    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
                )
            ''')
        finally:
            conn.close()
        
        # Create demo accounts if database is empty
        self.create_demo_accounts()
    
    def create_demo_accounts(self):
        """Create demo accounts for testing"""
        demo_accounts = [
            ("1234567890", "1234", 5000.0, "John Doe"),
            ("0987654321", "4321", 10000.0, "Jane Smith"),
            ("1111222233", "1111", 2500.0, "Bob Johnson")
        ]
        
        for acc_num, pin, balance, name in demo_accounts:
            if not self.account_exists(acc_num):
                self.create_account(acc_num, pin, name, balance)
    
    # CREATE operations
    def create_account(self, account_number, pin, name, initial_balance=0.0):
        """Create a new account"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO accounts (account_number, pin, balance, name, created_at)
                VALUES (?, ?, ?, ?, ?)
            ''', (account_number, pin, initial_balance, name, timestamp))
            
            # Record initial deposit if balance > 0
            if initial_balance > 0:
                self.add_transaction(account_number, "DEPOSIT", initial_balance, initial_balance)
            
            return True
        except sqlite3.IntegrityError:
            return False
        finally:
            conn.close()
    
    def add_transaction(self, account_number, transaction_type, amount, balance_after):
        """Add a transaction record"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cursor.execute('''
                INSERT INTO transactions (account_number, transaction_type, amount, balance_after, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (account_number, transaction_type, amount, balance_after, timestamp))
        finally:
            conn.close()
    
    # READ operations
    def account_exists(self, account_number):
        """Check if account exists"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT account_number FROM accounts WHERE account_number = ?', (account_number,))
        result = cursor.fetchone()
        conn.close()
        
        return result is not None
    
    def verify_pin(self, account_number, pin):
        """Verify account PIN"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT pin FROM accounts WHERE account_number = ? AND status = "active"', (account_number,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return result[0] == pin
        return False
    
    def get_balance(self, account_number):
        """Get account balance"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT balance FROM accounts WHERE account_number = ?', (account_number,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return result[0]
        return None
    
    def get_account_info(self, account_number):
        """Get full account information"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM accounts WHERE account_number = ?', (account_number,))
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {
                'account_number': result[0],
                'balance': result[2],
                'name': result[3],
                'created_at': result[4],
                'status': result[5]
            }
        return None
    
    def get_transaction_history(self, account_number, limit=10):
        """Get transaction history for an account"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT transaction_type, amount, balance_after, timestamp
            FROM transactions
            WHERE account_number = ?
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (account_number, limit))
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                'type': row[0],
                'amount': row[1],
                'balance_after': row[2],
                'timestamp': row[3]
            }
            for row in results
        ]
    
    def get_all_accounts(self):
        """Get all accounts (for admin purposes)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT account_number, name, balance, status FROM accounts')
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                'account_number': row[0],
                'name': row[1],
                'balance': row[2],
                'status': row[3]
            }
            for row in results
        ]
    
    # UPDATE operations
    def update_balance(self, account_number, new_balance):
        """Update account balance"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE accounts
                SET balance = ?
                WHERE account_number = ?
            ''', (new_balance, account_number))
        finally:
            conn.close()
    
    def deposit(self, account_number, amount):
        """Deposit money into account"""
        current_balance = self.get_balance(account_number)
        if current_balance is None:
            return False, "Account not found"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        new_balance = current_balance + amount
        self.update_balance(account_number, new_balance)
        self.add_transaction(account_number, "DEPOSIT", amount, new_balance)
        
        return True, new_balance
    
    def withdraw(self, account_number, amount):
        """Withdraw money from account"""
        current_balance = self.get_balance(account_number)
        if current_balance is None:
            return False, "Account not found"
        
        if amount <= 0:
            return False, "Invalid amount"
        
        if amount > current_balance:
            return False, "Insufficient funds"
        
        new_balance = current_balance - amount
        self.update_balance(account_number, new_balance)
        self.add_transaction(account_number, "WITHDRAWAL", amount, new_balance)
        
        return True, new_balance
    
    def change_pin(self, account_number, old_pin, new_pin):
        """Change account PIN"""
        if not self.verify_pin(account_number, old_pin):
            return False, "Invalid current PIN"
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE accounts
                SET pin = ?
                WHERE account_number = ?
            ''', (new_pin, account_number))
            
            return True, "PIN changed successfully"
        finally:
            conn.close()
    
    # DELETE operations
    def delete_account(self, account_number):
        """Delete an account (soft delete by setting status to 'closed')"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                UPDATE accounts
                SET status = 'closed'
                WHERE account_number = ?
            ''', (account_number,))
            
            return True
        finally:
            conn.close()
    
    def hard_delete_account(self, account_number):
        """Permanently delete an account and its transactions"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Delete transactions first
            cursor.execute('DELETE FROM transactions WHERE account_number = ?', (account_number,))
            
            # Delete account
            cursor.execute('DELETE FROM accounts WHERE account_number = ?', (account_number,))
            
            return True
        finally:
            conn.close()
