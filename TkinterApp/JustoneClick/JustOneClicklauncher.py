import os
import subprocess
import platform
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import webbrowser
import json

APP_LIST_FILE = "apps.txt"
PIN_FILE_PATH = "C:\\AppLauncher\\app_pin.json"
ICON_PATH = "app_icon.ico"

os.makedirs(os.path.dirname(PIN_FILE_PATH), exist_ok=True)

app_list = []

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
    # Allow adding URL or file path
    choice = messagebox.askquestion("Add App or URL", "Do you want to add a URL? Click 'No' to add an application/executable file.")
    if choice == "yes":
        url = simpledialog.askstring("Add URL", "Enter the full URL (including http:// or https://):")
        if url and (url.startswith("http://") or url.startswith("https://")):
            if url not in app_list:
                app_list.append(url)
                listbox.insert(tk.END, url)
                save_apps()
            else:
                messagebox.showinfo("Duplicate", "This URL is already in the list.")
        else:
            messagebox.showerror("Invalid URL", "Please enter a valid URL starting with http:// or https://")
    else:
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path not in app_list:
                app_list.append(file_path)
                listbox.insert(tk.END, file_path)
                save_apps()
            else:
                messagebox.showinfo("Duplicate", "This app is already in the list.")

def remove_selected():
    selected_indices = listbox.curselection()
    for index in reversed(selected_indices):
        del app_list[index]
        listbox.delete(index)
    save_apps()

def launch_selected():
    selected_indices = listbox.curselection()
    for index in selected_indices:
        item = app_list[index]
        launch_item(item)

def launch_all_apps():
    for item in app_list:
        launch_item(item)

def launch_item(item):
    if item.startswith("http://") or item.startswith("https://"):
        # Open URL in default browser
        try:
            webbrowser.open(item)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open URL:\n{item}\n\n{e}")
    else:
        # Launch executable or file
        try:
            if os.path.exists(item):
                if platform.system() == "Windows":
                    os.startfile(item)
                elif platform.system() == "Darwin":
                    subprocess.Popen(["open", item])
                else:
                    subprocess.Popen(["xdg-open", item])
            else:
                messagebox.showerror("Error", f"File not found:\n{item}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch:\n{item}\n\n{e}")



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

def show_splash():
    splash = tk.Toplevel()
    splash.title("🚀 Welcome")
    splash.geometry("400x200")
    splash.configure(bg="#1e1e1e")
    if os.path.exists(ICON_PATH):
        splash.iconbitmap(ICON_PATH)
    splash_label = tk.Label(splash, text="🎉 Welcome to Just One Click App Launcher", font=("Arial", 14), bg="#1e1e1e", fg="white")
    splash_label.pack(expand=True)
    splash.update()
    root.after(2500, splash.destroy)

# --- Main GUI Setup ---
root = tk.Tk()
root.withdraw()

if os.path.exists(ICON_PATH):
    root.iconbitmap(ICON_PATH)

show_splash()
root.after(2500, lambda: [prompt_for_pin(), root.deiconify()])

root.title("🚀 Just One Click App Launcher")
root.geometry("650x450")
root.configure(bg="#2d2d2d")

style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", foreground="white", background="#3c3f41", padding=6, font=("Segoe UI", 10))
style.configure("TLabel", background="#2d2d2d", foreground="white")
style.configure("TFrame", background="#2d2d2d")

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

button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

ttk.Button(button_frame, text="➕ Add App/URL", command=add_app).grid(row=0, column=0, padx=6, pady=4)
ttk.Button(button_frame, text="❌ Remove Selected", command=remove_selected).grid(row=0, column=1, padx=6)
ttk.Button(button_frame, text="🚀 Launch Selected", command=launch_selected).grid(row=0, column=2, padx=6)
ttk.Button(button_frame, text="⚡ Launch All", command=launch_all_apps).grid(row=1, column=1, padx=6, pady=6)
ttk.Button(button_frame, text="🔑 Reset PIN", command=reset_pin).grid(row=1, column=2, padx=6)

root.mainloop()
