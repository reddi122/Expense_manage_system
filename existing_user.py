# existing_user.py

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("user.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(":")
            if username == u and password == p:
                print("Login successful!")
                return username

    print("Invalid credentials.")
    return None

def add_expense(username):
    amount = input("Enter amount: ")
    desc = input("Enter description: ")
    with open("expenses.txt", "a") as f:
        f.write(f"{username},{amount},{desc}\n")
    print("Expense added.")

def view_expenses(username):
    with open("expenses.txt", "r") as f:
        for idx, line in enumerate(f):
            u, amt, desc = line.strip().split(",", 2)
            if u == username:
                print(f"{idx}: ₹{amt} - {desc}")

def delete_expense(username):
    with open("expenses.txt", "r") as f:
        lines = f.readlines()
    view_expenses(username)
    idx = int(input("Enter index to delete: "))
    if 0 <= idx < len(lines):              # 0 <= 2 < 4
        u = lines[idx].split(",")[0]
        if u == username:
            del lines[idx]
            with open("expenses.txt", "w") as f:
                f.writelines(lines)
            print("Deleted.")
        else:
            print("You can only delete your own expense.")
    else:
        print("Invalid index.")

def modify_expense(username):
    with open("expenses.txt", "r") as f:
        lines = f.readlines()
    view_expenses(username)
    idx = int(input("Enter index to modify: "))
    if 0 <= idx < len(lines):
        u = lines[idx].split(",")[0]
        if u == username:
            amt = input("New amount: ")
            desc = input("New description: ")
            lines[idx] = f"{username},{amt},{desc}\n"
            with open("expenses.txt", "w") as f:
                f.writelines(lines)
            print("Modified.")
        else:
            print("You can only modify your own expense.")
    else:
        print("Invalid index.")

def report_expenses(username):
    total = 0
    with open("expenses.txt", "r") as f:
        for line in f:
            u, amt, desc = line.strip().split(",", 2)
            if u == username:
                print(f"₹{amt} - {desc}")
                total += float(amt)
    print(f"Total: ₹{total}")
