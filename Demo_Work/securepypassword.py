import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        # Hash the password before storing it
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if website not in self.passwords:
            self.passwords[website] = {}
        self.passwords[website][username] = hashed_password
        print(f"Password added for {username} on {website}")

    def check_password(self, website, username, password):
        # Check if the provided password matches the stored password hash
        if website in self.passwords and username in self.passwords[website]:
            stored_password = self.passwords[website][username]
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if stored_password == hashed_password:
                print("Password is correct!")
            else:
                print("Incorrect password.")
        else:
            print("No matching record found.")

    def list_passwords(self):
        # Display all stored passwords
        if self.passwords:
            for website, credentials in self.passwords.items():
                print(f"Website: {website}")
                for username, _ in credentials.items():
                    print(f"  Username: {username}")
        else:
            print("No passwords stored.")

# Example usage
if __name__ == "__main__":
    manager = PasswordManager()
    manager.add_password("example.com", "Lichina01", "ACGATORS")
    manager.list_passwords()
    manager.check_password("example.com", "Lichina01", "ACGATORS")
