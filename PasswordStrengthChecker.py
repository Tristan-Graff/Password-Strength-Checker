import tkinter as tk
from tkinter import ttk
import re

def check_password_strength(password):
    strength = {"length": len(password) >= 8,
                "uppercase": any(char.isupper() for char in password),
                "lowercase": any(char.islower() for char in password),
                "digits": any(char.isdigit() for char in password),
                "special": any(char in "!@#$%^&*()-_+=<>?" for char in password)}
    
    score = sum(strength.values())
    
    tips = [
        ("Password should be at least 8 characters long.", strength["length"]),
        ("Password should include at least one uppercase letter.", strength["uppercase"]),
        ("Password should include at least one lowercase letter.", strength["lowercase"]),
        ("Password should include at least one digit.", strength["digits"]),
        ("Password should include at least one special character (!@#$%^&*()-_+=<>?).", strength["special"])
    ]
    
    if score <= 2:
        return score, "Weak", tips
    elif score == 3:
        return score, "Medium", tips
    elif score == 4:
        return score, "Strong", tips
    elif score == 5 and len(password) >= 12:
        return score, "Very Strong", tips
    elif score == 5:
        return score, "Strong", tips
    else:
        return score, "Strong", tips

def on_password_entry(event):
    password = entry_password.get()
    score, strength, tips = check_password_strength(password)
    progress_bar['value'] = (score / 5) * 100
    label_strength.config(text=f"Password Strength: {strength}")
    
    if strength == "Weak":
        progress_bar['style'] = 'red.Horizontal.TProgressbar'
    elif strength == "Medium":
        progress_bar['style'] = 'yellow.Horizontal.TProgressbar'
    elif strength == "Strong":
        progress_bar['style'] = 'green.Horizontal.TProgressbar'
    elif strength == "Very Strong":
        progress_bar['style'] = 'blue.Horizontal.TProgressbar'
    
    # Display tips with checkmarks for met criteria
    text_tips.config(state=tk.NORMAL)
    text_tips.delete(1.0, tk.END)
    for tip, met in tips:
        color = 'darkgreen' if met else 'darkred'
        checkmark = '✔' if met else '✘'
        text_tips.insert(tk.END, checkmark, (color,))
        text_tips.insert(tk.END, f" {tip}\n")
    text_tips.config(state=tk.DISABLED)

def toggle_password_visibility():
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        toggle_button.config(text="Hide")
    else:
        entry_password.config(show='*')
        toggle_button.config(text="Show")

def update_progressbar_length(event):
    width = root.winfo_width()
    progress_bar['length'] = width * 0.6  # 60% of the window width

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")  # Adjusted window size for better layout
root.configure(bg='#0077BE')  # Lapris blue color

# Create and place the widgets
label_prompt = tk.Label(root, text="Enter a password:", bg='#0077BE', fg='white', font=("Helvetica", 12))
label_prompt.pack(pady=10)

# Frame to contain the password entry and show button
password_frame = tk.Frame(root, bg='#0077BE')
password_frame.pack(pady=10)

entry_password = tk.Entry(password_frame, show='*', font=("Helvetica", 12))
entry_password.pack(side='left')

toggle_button = tk.Button(password_frame, text="Show", command=toggle_password_visibility, bg='#0000CD', fg='white', font=("Helvetica", 12))
toggle_button.pack(side='left', padx=5)

entry_password.bind("<KeyRelease>", on_password_entry)

# Create a progress bar for password strength
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate')
progress_bar.pack(pady=10)

# Label to display the password strength text
label_strength = tk.Label(root, text="Password Strength: ", bg='#0077BE', fg='white', font=("Helvetica", 12))
label_strength.pack(pady=10)

# Frame to contain the tips
tips_container = tk.Frame(root, bd=2, relief=tk.SUNKEN, padx=5, pady=5, width=500, bg='#0077BE')
tips_container.pack(pady=10, fill="x", expand=False)

# Header for the tips box
label_tips_header = tk.Label(tips_container, text="Password Suggestions", font=("Helvetica", 14, "bold"), bg='#0077BE', fg='white')
label_tips_header.pack(pady=5)

# Text widget to display the password tips
text_tips = tk.Text(tips_container, wrap="word", bg='#0077BE', fg='white', font=("Helvetica", 12), height=6)
text_tips.pack()

# Define tags for colors
text_tips.tag_configure("darkgreen", foreground="darkgreen")
text_tips.tag_configure("darkred", foreground="darkred")

# Initial tips
initial_tips_list = [
    ("Password should be at least 8 characters long.", False),
    ("Password should include at least one uppercase letter.", False),
    ("Password should include at least one lowercase letter.", False),
    ("Password should include at least one digit.", False),
    ("Password should include at least one special character (!@#$%^&*()-_+=<>?).", False)
]

for tip, met in initial_tips_list:
    color = 'darkgreen' if met else 'darkred'
    checkmark = '✔' if met else '✘'
    text_tips.insert(tk.END, checkmark, (color,))
    text_tips.insert(tk.END, f" {tip}\n")
text_tips.config(state=tk.DISABLED)

# Create different styles for the progress bar
style = ttk.Style()
style.configure('red.Horizontal.TProgressbar', troughcolor='white', background='red')
style.configure('yellow.Horizontal.TProgressbar', troughcolor='white', background='yellow')
style.configure('green.Horizontal.TProgressbar', troughcolor='white', background='green')
style.configure('blue.Horizontal.TProgressbar', troughcolor='white', background='blue')

# Bind the configure event to update the progress bar length when the window is resized
root.bind("<Configure>", update_progressbar_length)

# Run the application
root.mainloop()
