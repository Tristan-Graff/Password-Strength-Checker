import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    strength = {"length": False, "uppercase": False, "lowercase": False, "digits": False, "special": False}
    strength["length"] = len(password) >= 8
    strength["uppercase"] = any(char.isupper() for char in password)
    strength["lowercase"] = any(char.islower() for char in password)
    strength["digits"] = any(char.isdigit() for char in password)
    strength["special"] = any(char in "!@#$%^&*()-_+=<>?" for char in password)
    
    score = sum(strength.values())
    
    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    elif score == 4:
        return "Strong"
    elif score == 5 and len(password) >= 12:
        return "Very Strong"
    else:
        return "Strong"

def on_check_password():
    password = entry_password.get()
    strength = check_password_strength(password)
    label_result.config(text=f"Your password strength is: {strength}")

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
label_prompt = tk.Label(root, text="Enter a password:")
label_prompt.pack(pady=10)

entry_password = tk.Entry(root, show='*')
entry_password.pack(pady=10)

button_check = tk.Button(root, text="Check Strength", command=on_check_password)
button_check.pack(pady=10)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Run the application
root.mainloop()
