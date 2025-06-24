# new_user.py

def register_user():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("user.txt", "a") as f:
        f.write(f"{username}:{password}\n")

    print("User registered successfully!")
    return username
