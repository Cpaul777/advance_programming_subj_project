# Simple ATM Banking System (No Database Version)

A simplified ATM Banking System that uses **Python lists and dictionaries** instead of a database. Perfect for learning and understanding CRUD operations without database complexity!

## 🎯 Key Difference from Full Version

| Feature | Full Version | Simple Version |
|---------|-------------|----------------|
| Data Storage | SQLite Database | Lists & Dictionaries |
| Persistence | Data saved to disk | Data lost when app closes |
| Complexity | More complex | Very simple |
| Best For | Production-like app | Learning CRUD concepts |

## 📁 Project Files

### Simple Version Files:
- `simple_launcher.py` - Launch menu for the system
- `simple_atm.py` - ATM interface
- `simple_admin.py` - Admin panel
- `simple_datastore.py` - **Data storage using lists** (replaces database.py)

### Shared Files (Same as full version):
- `frames.py` - UI components
- `buttons.py` - Button styles
- `requirements.txt` - Dependencies

## 🚀 Quick Start

```bash
# Install requirement
pip install customtkinter

# Run the simple launcher
python simple_launcher.py
```

## 💡 How Data Storage Works

### Full Version (SQLite):
```python
# Uses database with SQL queries
conn = sqlite3.connect("bank_system.db")
cursor.execute("SELECT * FROM accounts WHERE account_number = ?", (acc_num,))
```

### Simple Version (Lists):
```python
# Uses Python lists and dictionaries
accounts = [
    {"account_number": "123", "name": "John", "balance": 5000},
    {"account_number": "456", "name": "Jane", "balance": 10000}
]

# Find account
account = next((acc for acc in accounts if acc["account_number"] == "123"), None)
```

## 📊 Data Structure

### Accounts List
```python
self.accounts = [
    {
        "account_number": "1234567890",
        "pin": "1234",
        "name": "John Doe",
        "balance": 5000.0,
        "status": "active",
        "created_at": "2026-01-17 10:30:00"
    },
    # ... more accounts
]
```

### Transactions List
```python
self.transactions = [
    {
        "id": 1,
        "account_number": "1234567890",
        "transaction_type": "DEPOSIT",
        "amount": 1000.0,
        "balance_after": 6000.0,
        "timestamp": "2026-01-17 10:35:00"
    },
    # ... more transactions
]
```

## 🔧 CRUD Operations Explained

### CREATE (Add New Account)
```python
def create_account(self, account_number, pin, name, initial_balance=0.0):
    # Create dictionary for new account
    new_account = {
        "account_number": account_number,
        "pin": pin,
        "name": name,
        "balance": initial_balance,
        "status": "active",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Add to list
    self.accounts.append(new_account)
    return True
```

**How it works:**
1. Create a dictionary with account details
2. Add (append) to the accounts list
3. That's it! No SQL needed

### READ (Get Account Info)
```python
def get_account(self, account_number):
    # Loop through accounts list
    for account in self.accounts:
        if account["account_number"] == account_number:
            return account  # Found it!
    return None  # Not found
```

**How it works:**
1. Loop through each account in the list
2. Check if account number matches
3. Return the account dictionary if found

### UPDATE (Modify Balance)
```python
def update_balance(self, account_number, new_balance):
    # Find the account
    account = self.get_account(account_number)
    
    if account:
        # Update the balance directly
        account["balance"] = new_balance
        return True
    return False
```

**How it works:**
1. Find the account dictionary
2. Change the balance value
3. Since it's the same dictionary in the list, the list is automatically updated!

### DELETE (Remove Account)
```python
def hard_delete_account(self, account_number):
    # Find the account
    account = self.get_account(account_number)
    
    if account:
        # Remove from list
        self.accounts.remove(account)
        
        # Also remove all transactions for this account
        self.transactions = [
            trans for trans in self.transactions
            if trans["account_number"] != account_number
        ]
        return True
    return False
```

**How it works:**
1. Find the account dictionary
2. Remove it from the accounts list
3. Filter out transactions for this account using list comprehension

## 🎓 Learning Benefits

### Why This Version is Great for Learning:

1. **See CRUD Operations Clearly**
   - No SQL syntax to learn
   - Direct Python list/dict manipulation
   - Easy to understand and debug

2. **Understand Data Relationships**
   - Accounts list contains account data
   - Transactions list links to accounts via account_number
   - Easy to visualize how data connects

3. **Focus on Logic, Not Syntax**
   - No database setup required
   - No connection management
   - Pure Python operations

4. **Easy to Modify and Experiment**
   - Change data structure easily
   - Add new fields quickly
   - Test without database complications

## ⚠️ Important Limitations

### This Simple Version:

❌ **Data is NOT saved** - When you close the app, all data is lost  
❌ **Not suitable for real use** - No persistent storage  
❌ **No concurrent access** - Can't handle multiple users well  
❌ **Data lost on crash** - No recovery mechanism  

### When to Use Each Version:

**Use Simple Version when:**
- Learning CRUD concepts
- Understanding data structures
- Quick prototyping
- Educational purposes
- Don't need to save data permanently

**Use Full Version (SQLite) when:**
- Need to save data permanently
- Building a real application
- Need transaction history to persist
- Want production-like features

## 🔄 Upgrading to Full Version

To upgrade from simple to full version, just switch the launcher:

```python
# From this:
python simple_launcher.py

# To this:
python launcher.py
```

The UI and features are identical - only the storage mechanism changes!

## 📚 Code Comparison

### Example: Depositing Money

**Simple Version (simple_datastore.py):**
```python
def deposit(self, account_number, amount):
    # Find account in list
    account = self.get_account(account_number)
    
    # Update balance
    new_balance = account["balance"] + amount
    account["balance"] = new_balance
    
    # Add transaction to list
    self.transactions.append({
        "account_number": account_number,
        "transaction_type": "DEPOSIT",
        "amount": amount,
        "balance_after": new_balance,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    return True, new_balance
```

**Full Version (database.py):**
```python
def deposit(self, account_number, amount):
    # Get connection to database
    conn = self.get_connection()
    cursor = conn.cursor()
    
    try:
        # Update balance in database
        cursor.execute('''
            UPDATE accounts 
            SET balance = balance + ? 
            WHERE account_number = ?
        ''', (amount, account_number))
        
        # Add transaction to database
        cursor.execute('''
            INSERT INTO transactions (account_number, transaction_type, amount, balance_after, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (account_number, "DEPOSIT", amount, new_balance, timestamp))
        
        return True, new_balance
    finally:
        conn.close()
```

See the difference? Simple version = direct list operations, Full version = SQL queries!

## 🎯 Demo Accounts

Both versions include the same demo accounts:

| Account Number | PIN  | Name         | Balance   |
|---------------|------|--------------|-----------|
| 1234567890    | 1234 | John Doe     | ₱5,000    |
| 0987654321    | 4321 | Jane Smith   | ₱10,000   |
| 1111222233    | 1111 | Bob Johnson  | ₱2,500    |

## 🔍 Understanding the Code

### simple_datastore.py Structure

```python
class BankDataStore:
    def __init__(self):
        self.accounts = []      # List of account dictionaries
        self.transactions = []  # List of transaction dictionaries
    
    # CREATE
    def create_account(...)     # Add to accounts list
    def add_transaction(...)    # Add to transactions list
    
    # READ
    def get_account(...)        # Find in accounts list
    def get_balance(...)        # Get balance from account
    def get_transaction_history(...) # Filter transactions list
    
    # UPDATE
    def update_balance(...)     # Modify account balance
    def deposit(...)            # Increase balance
    def withdraw(...)           # Decrease balance
    
    # DELETE
    def delete_account(...)     # Mark as closed
    def hard_delete_account(...) # Remove from list
```

### How Lists Store Data

```python
# Adding an account
accounts.append(new_account)

# Finding an account
for account in accounts:
    if account["account_number"] == search_number:
        return account

# Updating an account
account["balance"] = new_balance  # Direct modification

# Removing an account
accounts.remove(account)

# Filtering (keeping items that match condition)
active_accounts = [acc for acc in accounts if acc["status"] == "active"]
```

## 💪 Practice Exercises

Try these to understand the code better:

1. **Add a new field:**
   - Add "email" field to accounts
   - Display it in admin panel

2. **Create a new transaction type:**
   - Add "TRANSFER" transaction
   - Implement transfer between accounts

3. **Add search functionality:**
   - Search accounts by name
   - Filter transactions by type

4. **Calculate statistics:**
   - Total money in all accounts
   - Average account balance
   - Most active account

## 📖 Additional Resources

- **CRUD Explained:** Create, Read, Update, Delete operations
- **List Comprehension:** Filtering lists in Python
- **Dictionary Operations:** Working with key-value pairs
- **Loop Patterns:** Iterating through lists to find data

## ❓ FAQ

**Q: Why does data disappear when I close the app?**  
A: Because it's only stored in memory (RAM). Use the full version with SQLite for persistent storage.

**Q: Can I save the data manually?**  
A: You could export to JSON or CSV, but that's what databases are for!

**Q: Which version should I use for my school project?**  
A: If learning CRUD concepts → Simple version. If need persistence → Full version.

**Q: Can both versions run at the same time?**  
A: Yes! They use different data stores and don't interfere with each other.

## 🎉 Conclusion

This simplified version is perfect for:
- **Understanding** how CRUD operations work
- **Learning** data structure manipulation
- **Experimenting** without database complexity
- **Teaching** programming concepts

When you're ready for a production-like system, switch to the full version with SQLite!

---

**Happy Learning! 🚀**
