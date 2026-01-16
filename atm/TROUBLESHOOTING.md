# Troubleshooting Guide - Database Lock Issue

## Problem: "Database is locked" Error

This error occurs when multiple programs are trying to access the database at the same time, or when a previous connection wasn't closed properly.

---

## Solution 1: Close All Python Windows (RECOMMENDED)

### Step 1: Close Everything
1. Close **ALL** Python windows/applications currently running
2. Close the **launcher** if it's open
3. Close the **ATM interface** if it's open
4. Close the **admin panel** if it's open

### Step 2: Restart
1. Run `python launcher.py` again
2. Try opening just ONE application at a time

**Note**: The updated database.py now handles connections better, so this should prevent future locks!

---

## Solution 2: Reset the Database

If closing windows doesn't work, reset the database:

### Method A: Using the Reset Script (Easy)
```bash
python reset_database.py
```

This will:
- Delete the old database
- Create a fresh one when you run the app
- Restore the demo accounts automatically

### Method B: Manual Reset
1. Close all Python applications
2. Find and delete `bank_system.db` in your project folder
3. Run the launcher or app again - a new database will be created

---

## Solution 3: Check for Background Processes

### On Windows:
1. Press `Ctrl + Shift + Esc` to open Task Manager
2. Look for any Python processes
3. End all Python tasks
4. Try running the launcher again

### On Mac:
1. Press `Cmd + Space` and type "Activity Monitor"
2. Search for "Python"
3. Quit all Python processes
4. Try running the launcher again

### On Linux:
```bash
# Check for Python processes
ps aux | grep python

# Kill any Python processes (replace PID with actual process ID)
kill -9 PID
```

---

## Solution 4: Run Apps Separately (Not at Same Time)

Instead of using the launcher, run each app individually:

### For ATM Interface:
```bash
python app.py
```

### For Admin Panel (in a SEPARATE terminal/command prompt):
```bash
python admin_panel.py
```

**Important**: The updated code now allows both to run simultaneously, but if you're still having issues, run them one at a time.

---

## What I Fixed in the Database

I updated `database.py` with these improvements:

1. **Better Connection Handling**: 
   - Added 10-second timeout for locks
   - Using `check_same_thread=False` for better multi-window support
   - Auto-commit mode enabled

2. **Proper Connection Closing**:
   - All database operations now use try-finally blocks
   - Connections are always closed, even if errors occur

3. **Lock Prevention**:
   - Connections open and close quickly
   - No long-held connections

---

## Prevention Tips

To avoid database locks in the future:

1. **Don't spam-click buttons** - Wait for operations to complete
2. **Close properly** - Use the Quit button, don't force-close windows
3. **One action at a time** - Don't try to perform multiple transactions simultaneously
4. **Restart if stuck** - If something feels frozen, close and restart

---

## Still Having Issues?

If none of these solutions work:

### Option 1: Fresh Start
1. Delete the entire project folder
2. Re-download all files
3. Install customtkinter: `pip install customtkinter`
4. Run `python launcher.py`

### Option 2: Check Python Installation
```bash
# Check Python version (should be 3.8 or higher)
python --version

# Check if customtkinter is installed
pip show customtkinter
```

### Option 3: Try Direct Database Access
```python
# Test if database works
python -c "import sqlite3; conn = sqlite3.connect('bank_system.db'); print('Database OK'); conn.close()"
```

---

## Quick Reference

| Error Message | Most Likely Cause | Quick Fix |
|--------------|-------------------|-----------|
| "Database is locked" | Multiple apps open | Close all Python windows |
| "Unable to open database" | File permissions | Run reset_database.py |
| "No module named customtkinter" | Package not installed | pip install customtkinter |
| Window freezes | Database operation stuck | Close and restart |

---

## Understanding the Fix

The original code had these issues:
```python
# OLD CODE - Could cause locks
conn = sqlite3.connect(self.db_name)  # No timeout
# ... operations ...
conn.commit()  # Explicit commit (can hold lock longer)
conn.close()
```

The new code fixes this:
```python
# NEW CODE - Better lock handling
conn = sqlite3.connect(self.db_name, timeout=10.0, check_same_thread=False)
conn.isolation_level = None  # Auto-commit, faster operations
try:
    # ... operations ...
finally:
    conn.close()  # ALWAYS closes, even on error
```

---

## Test After Fixing

To verify everything works:

1. **Test 1**: Run launcher, open ATM, log in with demo account
2. **Test 2**: Open admin panel, view account list
3. **Test 3**: Try running both simultaneously (should work now!)
4. **Test 4**: Perform a withdrawal and check it logs properly

If all tests pass, you're good to go! 🎉

---

## Contact for Help

If you're still stuck, provide these details:
- Operating System (Windows/Mac/Linux)
- Python version
- Exact error message
- What you were doing when error occurred

---

**Remember**: The updated database.py should prevent most lock issues. If problems persist, use the reset script!
