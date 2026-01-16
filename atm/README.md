# ATM Banking System

A fully functional ATM Banking System built with Python and CustomTkinter, featuring a modern UI and complete CRUD operations for account management.

## Features

### 🏧 ATM Interface
- **Account Authentication**: Secure PIN-based login with 3-attempt limit
- **Balance Inquiry**: Check current account balance
- **Cash Withdrawal**: Withdraw money (max ₱20,000 per transaction)
- **Cash Deposit**: Deposit money (max ₱50,000 per transaction)
- **Transaction Confirmation**: Yes/No confirmation for all transactions
- **Session Management**: Automatic logout and session reset

### 👨‍💼 Admin Panel
- **Create Account (C)**: Add new accounts with account number, name, PIN, and initial balance
- **Read Account (R)**: View account details and transaction history
- **Update Account (U)**: Modify account information
- **Delete Account (D)**: Remove accounts from the system
- **Account List**: View all accounts with status indicators
- **Transaction History**: View detailed transaction logs for any account

### 🗄️ Database
- **SQLite Database**: Persistent storage for all account and transaction data
- **Two Tables**: 
  - `accounts`: Stores account information
  - `transactions`: Logs all transactions
- **Demo Accounts**: Pre-loaded accounts for testing

## Project Structure

```
ATM-Banking-System/
├── app.py              # Main ATM interface application
├── admin_panel.py      # Admin panel for account management
├── database.py         # Database operations and CRUD functions
├── frames.py           # UI frames (screen, keypad, buttons)
├── buttons.py          # Custom button classes
├── bank_system.db      # SQLite database (auto-generated)
└── README.md          # This file
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Required Libraries
```bash
pip install customtkinter
```

### Setup
1. Clone or download the project files
2. Install required libraries
3. Run the application

## Usage

### Running the ATM Interface
```bash
python app.py
```

### Running the Admin Panel
```bash
python admin_panel.py
```

## Demo Accounts

The system comes with three pre-loaded demo accounts for testing:

| Account Number | PIN  | Name        | Balance   |
|---------------|------|-------------|-----------|
| 1234567890    | 1234 | John Doe    | ₱5,000    |
| 0987654321    | 4321 | Jane Smith  | ₱10,000   |
| 1111222233    | 1111 | Bob Johnson | ₱2,500    |

## How to Use the ATM

### Step 1: Insert Card (Enter Account Number)
1. Enter your account number using the keypad
2. Press "Enter" to continue

### Step 2: Enter PIN
1. Enter your 4-digit PIN (input is masked with asterisks)
2. Press "Enter" to continue
3. You have 3 attempts before the card is retained

### Step 3: Main Menu
Select a transaction using the side buttons:
- **B** - Balance Inquiry
- **D** - Deposit Money
- **W** - Withdraw Money
- **Q** - Quit (Exit)

### Step 4: Perform Transaction

#### Balance Inquiry
1. Press "B" button
2. Your balance is displayed
3. Choose "Yes" for another transaction or "No" to exit

#### Withdrawal
1. Press "W" button
2. Enter amount using keypad (max ₱20,000)
3. Press "Enter"
4. Confirm by pressing "Yes" or cancel with "No"
5. Transaction receipt is displayed

#### Deposit
1. Press "D" button
2. Enter amount using keypad (max ₱50,000)
3. Press "Enter"
4. Confirm by pressing "Yes" or cancel with "No"
5. Transaction receipt is displayed

### Keypad Controls
- **Number Keys (0-9)**: Enter digits
- **Clear**: Remove last digit
- **Enter**: Confirm input
- **Cancel**: Return to main menu or exit

## Admin Panel Guide

### Creating a New Account
1. Fill in all fields:
   - Account Number (unique)
   - Account Holder Name
   - PIN (4 digits)
   - Initial Balance
2. Click "Create Account"

### Viewing Account Details
1. Enter account number in "Modify Account" section
2. Click "View Details"
3. Account information is displayed in a popup

### Deleting an Account
1. Enter account number in "Modify Account" section
2. Click "Delete Account"
3. Confirm deletion in the popup
4. Account and all transactions are permanently removed

### Viewing Transaction History
1. Enter account number in "Transaction History" section
2. Click "View History"
3. A new window opens showing all transactions

### Refreshing Account List
- Click "Refresh List" to update the account display

## Code Structure Explanation

### 1. database.py
**Purpose**: Handles all database operations

**Key Classes**:
- `BankDatabase`: Main database manager

**Key Methods**:
- `create_account()`: CREATE - Add new account
- `get_account_info()`: READ - Retrieve account data
- `update_balance()`: UPDATE - Modify account balance
- `delete_account()`: DELETE - Remove account
- `deposit()`: Add money to account
- `withdraw()`: Remove money from account
- `get_transaction_history()`: Retrieve transaction logs

**How it works**:
1. Initializes SQLite database on first run
2. Creates two tables: accounts and transactions
3. Provides methods for all CRUD operations
4. Automatically logs all transactions
5. Ensures data persistence across sessions

### 2. buttons.py
**Purpose**: Custom button classes with consistent styling

**Key Classes**:
- `AppButton`: Standard square buttons (B, D, W, Q)
- `LongerButton`: Rectangular buttons (Clear, Enter, Cancel)
- `KeypadButton`: Numeric keypad buttons (0-9)
- `ConfirmButton`: Green "Yes" button
- `CancelButton`: Red "No" button

**How it works**:
1. Extends CTkButton with custom dimensions
2. Applies consistent color scheme
3. Provides hover effects
4. Accepts callback functions for actions

### 3. frames.py
**Purpose**: Container frames for organizing UI components

**Key Classes**:

**ActionFrame**:
- Contains B, D, W, Q buttons on the left side
- Calls `app.handle_actions()` with button pressed

**ConfirmationButtons**:
- Contains Yes/No buttons on the right side
- Calls `app.handle_confirmation()` with response

**Keypad**:
- Contains numeric keypad (0-9)
- Contains Clear, Enter, Cancel buttons
- Calls appropriate app methods for each button

**ScreenFrame**:
- Main display area in the center
- Shows title, messages, input field, and info
- Methods to update different screen elements
- Can show/hide input and info sections

**How it works**:
1. Each frame is a container for related buttons
2. Frames handle layout using grid system
3. Buttons call back to main app for logic
4. Screen frame dynamically updates based on state

### 4. app.py
**Purpose**: Main ATM application with business logic

**Key Components**:

**State Management**:
```python
self.windowState = "INSERT_CARD"  # Current screen state
self.current_account = None        # Logged in account
self.current_input = ""            # User input buffer
self.pending_amount = 0            # Transaction amount
self.pin_attempts = 0              # Failed login attempts
```

**States**:
- `INSERT_CARD`: Initial screen, enter account number
- `ENTER_PIN`: PIN entry screen
- `MENU`: Main menu (B, D, W, Q options)
- `BALANCE`: Display balance
- `WITHDRAW`: Enter withdrawal amount
- `DEPOSIT`: Enter deposit amount
- `CONFIRM_WITHDRAW`: Confirm withdrawal
- `CONFIRM_DEPOSIT`: Confirm deposit
- `SUCCESS_WITHDRAW`: Show withdrawal success
- `SUCCESS_DEPOSIT`: Show deposit success
- `ERROR`: Display error message
- `GOODBYE`: Exit screen

**Key Methods**:

`update_screen()`:
- Updates display based on current state
- Shows appropriate title, message, and input
- Core method that renders the UI

`handle_keypad(digit)`:
- Appends digit to current input
- Updates screen to show input

`handle_enter()`:
- Processes input based on current state
- Validates account numbers, PINs, amounts
- Advances to next state or shows errors

`handle_actions(action)`:
- Processes B, D, W, Q button presses
- Changes state to appropriate screen

`handle_confirmation(response)`:
- Processes Yes/No responses
- Executes or cancels transactions
- Returns to menu or exits

`show_error(message)`:
- Displays error message
- Automatically returns to previous state after 2 seconds

`reset_session()`:
- Clears all session data
- Returns to initial state

**How it works**:
1. App starts in INSERT_CARD state
2. User interactions trigger handler methods
3. Handlers update state and call update_screen()
4. update_screen() renders appropriate UI for state
5. Database methods are called for transactions
6. Errors are caught and displayed
7. Session automatically resets after logout

### 5. admin_panel.py
**Purpose**: Administrative interface for account management

**Key Features**:

**Account List (Left Panel)**:
- Scrollable list of all accounts
- Shows account number, name, balance, status
- Color-coded status indicators (green=active, red=closed)
- Refresh button to reload data

**Operations Panel (Right Panel)**:

*Create Account Section*:
- Input fields for new account data
- Validation for all fields
- Calls `db.create_account()` on success

*Modify Account Section*:
- View account details
- Delete account with confirmation
- Calls appropriate database methods

*Transaction History Section*:
- Opens new window with transaction log
- Shows type, amount, balance, timestamp
- Color-coded by transaction type

**How it works**:
1. Loads all accounts on startup
2. Each operation validates input
3. Calls appropriate database methods
4. Shows success/error messages
5. Refreshes display after changes
6. Uses popup windows for detailed views

## Database Schema

### accounts Table
```sql
CREATE TABLE accounts (
    account_number TEXT PRIMARY KEY,
    pin TEXT NOT NULL,
    balance REAL DEFAULT 0.0,
    name TEXT NOT NULL,
    created_at TEXT NOT NULL,
    status TEXT DEFAULT 'active'
)
```

### transactions Table
```sql
CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL,
    transaction_type TEXT NOT NULL,
    amount REAL NOT NULL,
    balance_after REAL NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
)
```

## Security Features

1. **PIN Masking**: PINs are displayed as asterisks
2. **Attempt Limit**: Max 3 PIN attempts before card retention
3. **Transaction Limits**: 
   - Withdrawal: ₱20,000 max per transaction
   - Deposit: ₱50,000 max per transaction
4. **Balance Validation**: Prevents overdrafts
5. **Session Timeout**: Automatic logout after transaction completion

## Color Scheme

- **Primary**: #1f538d (Dark Blue)
- **Secondary**: #2980b9 (Light Blue)
- **Success**: #27ae60 (Green)
- **Danger**: #e74c3c (Red)
- **Light**: #ecf0f1 (Light Gray)
- **Dark**: #2c3e50 (Dark Gray)
- **Background**: #34495e (Blue Gray)

## Troubleshooting

### Issue: "No module named 'customtkinter'"
**Solution**: Install CustomTkinter
```bash
pip install customtkinter
```

### Issue: Database not found
**Solution**: The database is automatically created. Ensure write permissions in the directory.

### Issue: Account not loading
**Solution**: Check if bank_system.db exists. Delete it to recreate with demo accounts.

### Issue: UI elements not displaying
**Solution**: Update CustomTkinter to the latest version
```bash
pip install --upgrade customtkinter
```

## Future Enhancements

- [ ] Transfer money between accounts
- [ ] Print receipt functionality
- [ ] Change PIN feature in ATM
- [ ] Multiple currency support
- [ ] Account statements
- [ ] Interest calculation
- [ ] Card scanning simulation
- [ ] Sound effects
- [ ] Network/multi-machine support
- [ ] Encryption for PIN storage

## Technologies Used

- **Python 3.x**: Programming language
- **CustomTkinter**: Modern UI framework
- **SQLite3**: Database engine
- **tkinter.messagebox**: Dialog boxes

## License

This is a educational project created for learning purposes.

## Credits

Developed as a comprehensive ATM Banking System with full CRUD operations.

---

**Note**: This is a simulation for educational purposes. Do not use for actual banking operations.
