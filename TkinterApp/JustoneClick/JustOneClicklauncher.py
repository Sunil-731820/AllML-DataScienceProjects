import os
import subprocess
import platform
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import json

# Constants
APP_LIST_FILE = "apps.txt"
PIN_FILE_PATH = "C:\\AppLauncher\\app_pin.json"

# Ensure the directory exists for PIN storage
os.makedirs(os.path.dirname(PIN_FILE_PATH), exist_ok=True)

# App list
app_list = []

# Load apps from file
def load_apps():
    global app_list
    if os.path.exists(APP_LIST_FILE):
        with open(APP_LIST_FILE, "r") as f:
            app_list = [line.strip() for line in f if line.strip()]

# Save apps to file
def save_apps():
    with open(APP_LIST_FILE, "w") as f:
        for app in app_list:
            f.write(app + "\n")

# Add app
def add_app():
    file_path = filedialog.askopenfilename()
    if file_path and file_path not in app_list:
        app_list.append(file_path)
        listbox.insert(tk.END, file_path)
        save_apps()

# Remove selected app
def remove_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        del app_list[index]
        listbox.delete(index)
    save_apps()

# Launch selected app
def launch_selected():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        app_path = app_list[index]
        try:
            if os.path.exists(app_path):
                if platform.system() == "Windows":
                    os.startfile(app_path)
                elif platform.system() == "Darwin":  # macOS
                    subprocess.Popen(["open", app_path])
                else:  # Linux
                    subprocess.Popen(["xdg-open", app_path])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Could not launch:\n{app_path}\n\n{e}")

# Launch all apps
def launch_all_apps():
    for app_path in app_list:
        try:
            if os.path.exists(app_path):
                if platform.system() == "Windows":
                    os.startfile(app_path)
                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", app_path])
                else:
                    subprocess.Popen(["xdg-open", app_path])
        except Exception as e:
            messagebox.showerror("Launch Error", f"Error launching {app_path}:\n{str(e)}")



# PIN handling
def load_pin():
    if os.path.exists(PIN_FILE_PATH):
        with open(PIN_FILE_PATH, "r") as f:
            return json.load(f).get("pin")
    return None

def save_pin(pin):
    with open(PIN_FILE_PATH, "w") as f:
        json.dump({"pin": pin}, f)

def prompt_for_pin():
    saved_pin = load_pin()
    if saved_pin:
        while True:
            entered_pin = simpledialog.askstring("PIN Required", "Enter your PIN:", show="*")
            if entered_pin is None:
                if messagebox.askyesno("Exit", "Do you want to exit the app?"):
                    root.destroy()
                    return
            elif entered_pin == saved_pin:
                break
            else:
                messagebox.showerror("Access Denied", "Incorrect PIN. Please try again.")
    else:
        while True:
            new_pin = simpledialog.askstring("Set a PIN", "Create a 5–10 digit PIN:", show="*")
            if new_pin and new_pin.isdigit() and 5 <= len(new_pin) <= 10:
                save_pin(new_pin)
                messagebox.showinfo("PIN Saved", "PIN has been securely saved.")
                break
            else:
                messagebox.showwarning("Invalid PIN", "PIN must be 5–10 digits.")

# Reset PIN
def reset_pin():
    confirm = messagebox.askyesno("Reset PIN", "Are you sure you want to reset your PIN?")
    if confirm:
        if os.path.exists(PIN_FILE_PATH):
            os.remove(PIN_FILE_PATH)
        prompt_for_pin()

# UI Setup
root = tk.Tk()
root.withdraw()  # Hide main window for PIN prompt
root.title("Just One Click App Launcher")
root.geometry("600x500")

prompt_for_pin()
root.deiconify()  # Show main window after PIN is accepted
load_apps()

listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)
for app in app_list:
    listbox.insert(tk.END, app)

# Buttons
tk.Button(root, text="Add App", command=add_app).pack(pady=2)
tk.Button(root, text="Remove Selected", command=remove_selected).pack(pady=2)
tk.Button(root, text="Launch Selected", command=launch_selected).pack(pady=2)
tk.Button(root, text="Launch All Apps", command=launch_all_apps, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Reset PIN", command=reset_pin).pack(pady=2)

root.mainloop()
