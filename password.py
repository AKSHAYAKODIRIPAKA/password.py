import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        # Labels and Entry
        tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
        self.length_entry = tk.Entry(root, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Checkbuttons for character types
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)
        
        tk.Checkbutton(root, text="Include Uppercase", variable=self.include_uppercase).grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits).grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special).grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Password Output
        self.password_var = tk.StringVar()
        tk.Entry(root, textvariable=self.password_var, width=30).grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be positive.")

            characters = string.ascii_lowercase
            if self.include_uppercase.get():
                characters += string.ascii_uppercase
            if self.include_digits.get():
                characters += string.digits
            if self.include_special.get():
                characters += string.punctuation

            if not characters:
                raise ValueError("At least one character type must be selected.")
            
            password = ''.join(random.choice(characters) for _ in range(length))
            self.password_var.set(password)
        
        except ValueError as e:
            messagebox.showwarning("Invalid Input", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
