accounts = {}

while True:
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Delete Account")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        if name in accounts:
            print("❌ Account already exists")
        else:
            accounts[name] = 0
            print("✅ Account created")

    elif choice == "2":
        name = input("Enter name: ")
        if name in accounts:
            amount = int(input("Enter amount: "))
            accounts[name] += amount
            print("💰 Deposited successfully")
        else:
            print("❌ Account not found")

    elif choice == "3":
        name = input("Enter name: ")
        if name in accounts:
            amount = int(input("Enter amount: "))
            if accounts[name] >= amount:
                accounts[name] -= amount
                print("💸 Withdrawal successful")
            else:
                print("❌ Insufficient balance")
        else:
            print("❌ Account not found")

    elif choice == "4":
        name = input("Enter name: ")
        if name in accounts:
            print("💼 Balance:", accounts[name])
        else:
            print("❌ Account not found")

    elif choice == "5":
        name = input("Enter name: ")
        if name in accounts:
            del accounts[name]
            print("🗑️ Account deleted")
        else:
            print("❌ Account not found")

    elif choice == "6":
        print("👋 Thank you")
        break

    else:
        print("❌ Invalid choice")
