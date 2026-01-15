# Quick Start Guide - ATM Banking System

## Installation (First Time Only)

### Step 1: Install Python
If you don't have Python installed, download it from https://www.python.org/downloads/
Make sure to check "Add Python to PATH" during installation.

### Step 2: Install Required Package
Open Command Prompt (Windows) or Terminal (Mac/Linux) and run:
```bash
pip install customtkinter
```

## Running the System

### Option 1: Using the Launcher (Recommended)
```bash
python launcher.py
```
Then click either:
- "ATM Interface" - for customer transactions
- "Admin Panel" - for account management

### Option 2: Direct Launch
**For ATM Interface:**
```bash
python app.py
```

**For Admin Panel:**
```bash
python admin_panel.py
```

## Demo Accounts for Testing

Try these accounts in the ATM:

1. **John Doe**
   - Account: `1234567890`
   - PIN: `1234`
   - Balance: ₱5,000

2. **Jane Smith**
   - Account: `0987654321`
   - PIN: `4321`
   - Balance: ₱10,000

3. **Bob Johnson**
   - Account: `1111222233`
   - PIN: `1111`
   - Balance: ₱2,500

## Quick Tutorial - ATM Interface

### 🏧 Basic Transaction Flow

1. **Insert Card (Enter Account)**
   - Type account number: `1234567890`
   - Press "Enter"

2. **Enter PIN**
   - Type PIN: `1234`
   - Press "Enter"

3. **Main Menu** - Choose option:
   - Press "B" = Check Balance
   - Press "D" = Deposit Money
   - Press "W" = Withdraw Money
   - Press "Q" = Quit

4. **For Withdrawal:**
   - Press "W"
   - Type amount: `1000`
   - Press "Enter"
   - Press "Yes" to confirm
   - See new balance

5. **For Deposit:**
   - Press "D"
   - Type amount: `500`
   - Press "Enter"
   - Press "Yes" to confirm
   - See new balance

6. **Another Transaction?**
   - Press "Yes" = Return to menu
   - Press "No" = Logout

## Quick Tutorial - Admin Panel

### 👨‍💼 Account Management

**Create New Account:**
1. Fill in "Create New Account" section:
   - Account Number: `9999888877`
   - Name: `Test User`
   - PIN: `9999`
   - Balance: `1000`
2. Click "Create Account"

**View Account Details:**
1. Enter account number: `1234567890`
2. Click "View Details"
3. See account info in popup

**View Transaction History:**
1. Enter account number: `1234567890`
2. Click "View History"
3. See all transactions in new window

**Delete Account:**
1. Enter account number: `9999888877`
2. Click "Delete Account"
3. Confirm deletion

## UI Layout Explanation

### ATM Interface Layout:
```
┌────────────────────────────────────────────┐
│  [B]           SCREEN AREA           [Yes] │
│  [D]                                 [No]  │
│  [W]                                       │
│  [Q]                                       │
├────────────────────────────────────────────┤
│        [1] [2] [3] [Clear]                 │
│        [4] [5] [6] [Enter]                 │
│        [7] [8] [9] [Cancel]                │
│           [0]                              │
└────────────────────────────────────────────┘
```

**Left Side (B, D, W, Q):**
- B = Balance
- D = Deposit
- W = Withdraw
- Q = Quit

**Right Side (Yes, No):**
- Use for confirmations
- "Yes" = Confirm transaction
- "No" = Cancel transaction

**Bottom (Keypad):**
- Numbers 0-9 for input
- Clear = Delete last digit
- Enter = Submit input
- Cancel = Go back to menu

### Admin Panel Layout:
```
┌─────────────────────────────────────────────┐
│        Account Management System            │
├──────────────────┬──────────────────────────┤
│   All Accounts   │  Account Operations      │
│                  │                          │
│  [Account List]  │  [Create New Account]    │
│                  │  - Account Number        │
│  • John Doe      │  - Name                  │
│    1234567890    │  - PIN                   │
│    ₱5,000.00     │  - Balance               │
│                  │  [Create Account Button] │
│  • Jane Smith    │                          │
│    0987654321    │  [Modify Account]        │
│    ₱10,000.00    │  - Account Number        │
│                  │  [View] [Delete]         │
│  [Refresh]       │                          │
│                  │  [Transaction History]   │
│                  │  - Account Number        │
│                  │  [View History]          │
└──────────────────┴──────────────────────────┘
```

## Common Operations

### Check Balance
1. Login with account and PIN
2. Press "B" button
3. See your balance
4. Choose Yes/No for another transaction

### Make a Withdrawal
1. Login
2. Press "W" button
3. Type amount (max ₱20,000)
4. Press "Enter"
5. Press "Yes" to confirm
6. Get your money!

### Make a Deposit
1. Login
2. Press "D" button
3. Type amount (max ₱50,000)
4. Press "Enter"
5. Press "Yes" to confirm
6. Money is added!

## Troubleshooting

**Problem**: Can't login
- **Solution**: Check if caps lock is on. PIN must be exactly 4 digits.

**Problem**: "Insufficient funds" error
- **Solution**: You don't have enough money. Check balance first (press B).

**Problem**: Numbers not appearing
- **Solution**: Make sure you're on the right screen. Look at the title at the top.

**Problem**: Admin panel shows empty list
- **Solution**: Click "Refresh List" button at bottom of account list.

## Tips & Tricks

1. **Clear Input**: Use "Clear" button to fix typing mistakes
2. **Cancel Anytime**: Press "Cancel" to return to main menu
3. **Check Balance First**: Press "B" before withdrawing to see available funds
4. **Practice with Demo Accounts**: Use the pre-loaded accounts to learn
5. **Refresh Admin List**: After creating/deleting accounts, click "Refresh"

## Safety Rules

⚠️ **Important**: 
- You have only 3 attempts to enter correct PIN
- Maximum withdrawal: ₱20,000 per transaction
- Maximum deposit: ₱50,000 per transaction
- Can't withdraw more than your balance
- All transactions are logged

## Need Help?

Check the full README.md file for:
- Complete code explanation
- Database structure
- Advanced features
- Technical details

## File Structure

```
Your Folder/
├── launcher.py          ← Start here!
├── app.py              ← ATM interface
├── admin_panel.py      ← Admin panel
├── database.py         ← Database operations
├── frames.py           ← UI components
├── buttons.py          ← Button styles
├── bank_system.db      ← Your database (auto-created)
├── requirements.txt    ← Dependencies
└── README.md          ← Full documentation
```

---

## Quick Command Reference

| Command | What It Does |
|---------|-------------|
| `python launcher.py` | Open launcher menu |
| `python app.py` | Run ATM directly |
| `python admin_panel.py` | Run admin panel directly |
| `pip install customtkinter` | Install required package |

---

**Enjoy your ATM Banking System! 🏦💰**
