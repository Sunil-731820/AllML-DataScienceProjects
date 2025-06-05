import os
import subprocess
import platform
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import json

# Constants
APP_LIST_FILE = "apps.txt"
PIN_FILE_PATH = "C:\\AppLauncher\\app_pin.json"

# Ensure PIN directory exists
os.makedirs(os.path.dirname(PIN_FILE_PATH), exist_ok=True)

app_list = []

# --- App Logic ---
def load_apps():
    global app_list
    if os.path.exists(APP_LIST_FILE):
        with open(APP_LIST_FILE, "r") as f:
            app_list = [line.strip() for line in f if line.strip()]

def save_apps():
    with open(APP_LIST_FILE, "w") as f:
        for app in app_list:
            f.write(app + "\n")

def add_app():
    file_path = filedialog.askopenfilename()
    if file_path and file_path not in app_list:
        app_list.append(file_path)
        listbox.insert(tk.END, file_path)
        save_apps()

def remove_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        del app_list[index]
        listbox.delete(index)
    save_apps()

def launch_selected():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        app_path = app_list[index]
        _launch_app(app_path)

def launch_all_apps():
    for app_path in app_list:
        _launch_app(app_path)

def _launch_app(app_path):
    try:
        if os.path.exists(app_path):
            if platform.system() == "Windows":
                os.startfile(app_path)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", app_path])
            else:
                subprocess.Popen(["xdg-open", app_path])
    except Exception as e:
        messagebox.showerror("Launch Error", f"Could not launch:\n{app_path}\n\n{e}")

def export_list():
    export_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if export_path:
        with open(export_path, "w") as f:
            for app in app_list:
                f.write(app + "\n")
        messagebox.showinfo("Export Complete", "App list exported successfully.")

# --- PIN Functions ---
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

def reset_pin():
    confirm = messagebox.askyesno("Reset PIN", "Are you sure you want to reset your PIN?")
    if confirm:
        if os.path.exists(PIN_FILE_PATH):
            os.remove(PIN_FILE_PATH)
        prompt_for_pin()

# --- Splash Screen ---
def show_splash():
    splash = tk.Toplevel()
    splash.title("Welcome")
    splash.geometry("400x200")
    splash.configure(bg="#1e1e1e")
    splash_label = tk.Label(splash, text="🎉 Welcome to Just One Click App Launcher", font=("Arial", 14), bg="#1e1e1e", fg="white")
    splash_label.pack(expand=True)
    splash.update()
    root.after(2500, splash.destroy)

# --- Main GUI Setup ---
root = tk.Tk()
root.withdraw()

# Show splash
show_splash()

# After splash, show PIN
root.after(2500, lambda: [prompt_for_pin(), root.deiconify()])

root.title("Just One Click App Launcher")
root.geometry("650x450")
root.configure(bg="#2d2d2d")

# Dark theme with ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#3c3f41", padding=6, font=("Segoe UI", 10))
style.configure("TLabel", background="#2d2d2d", foreground="white")
style.configure("TFrame", background="#2d2d2d")

# Listbox with dark mode
listbox_frame = ttk.Frame(root)
listbox_frame.pack(pady=10)

scrollbar = ttk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, width=80, height=15, bg="#1e1e1e", fg="white", yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar.config(command=listbox.yview)

load_apps()
for app in app_list:
    listbox.insert(tk.END, app)

# Buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

ttk.Button(button_frame, text="➕ Add App", command=add_app).grid(row=0, column=0, padx=6, pady=4)
ttk.Button(button_frame, text="❌ Remove Selected", command=remove_selected).grid(row=0, column=1, padx=6)
ttk.Button(button_frame, text="🚀 Launch Selected", command=launch_selected).grid(row=0, column=2, padx=6)
ttk.Button(button_frame, text="⚡ Launch All Apps", command=launch_all_apps).grid(row=1, column=0, padx=6, pady=6)
ttk.Button(button_frame, text="📄 Export List", command=export_list).grid(row=1, column=1, padx=6)
ttk.Button(button_frame, text="🔑 Reset PIN", command=reset_pin).grid(row=1, column=2, padx=6)

root.mainloop()
