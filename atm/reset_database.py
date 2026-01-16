"""
Database Reset Script
Run this if you're experiencing database lock issues
"""
import os
import sys

def reset_database():
    """Delete the database file to start fresh"""
    db_file = "bank_system.db"
    
    if os.path.exists(db_file):
        try:
            os.remove(db_file)
            print(f"✓ Successfully deleted {db_file}")
            print("✓ A new database will be created when you run the app")
            print("✓ Demo accounts will be automatically restored")
        except Exception as e:
            print(f"✗ Error deleting database: {e}")
            print("\nTry closing all Python windows and run this script again")
    else:
        print(f"✓ Database file '{db_file}' doesn't exist - nothing to reset")
    
    print("\nYou can now run the launcher or app again!")

if __name__ == "__main__":
    print("=" * 60)
    print("ATM Banking System - Database Reset Tool")
    print("=" * 60)
    print("\nThis will DELETE the current database and create a fresh one.")
    print("All accounts and transactions will be lost!")
    print("\nDemo accounts will be restored automatically:")
    print("  - 1234567890 (PIN: 1234, Balance: ₱5,000)")
    print("  - 0987654321 (PIN: 4321, Balance: ₱10,000)")
    print("  - 1111222233 (PIN: 1111, Balance: ₱2,500)")
    
    response = input("\nAre you sure you want to continue? (yes/no): ").lower().strip()
    
    if response in ['yes', 'y']:
        print("\nResetting database...")
        reset_database()
    else:
        print("\nDatabase reset cancelled.")
