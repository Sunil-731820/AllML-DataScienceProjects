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

def refresh_treeview():
    for row in tree.get_children():
        tree.delete(row)
    for idx, app in enumerate(app_list):
        tag = 'oddrow' if idx % 2 else 'evenrow'
        tree.insert("", "end", iid=idx, values=(app,), tags=(tag,))

def add_app():
    choice = messagebox.askquestion("Add App or URL", "Add a URL? Click 'No' to add an application/executable file.")
    if choice == "yes":
        url = simpledialog.askstring("Add URL", "Enter full URL (http:// or https://):")
        if url and (url.startswith("http://") or url.startswith("https://")):
            if url not in app_list:
                app_list.append(url)
                refresh_treeview()
                save_apps()
            else:
                messagebox.showinfo("Duplicate", "URL already in list.")
        else:
            messagebox.showerror("Invalid URL", "Please enter valid URL starting with http:// or https://")
    else:
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_path not in app_list:
                app_list.append(file_path)
                refresh_treeview()
                save_apps()
            else:
                messagebox.showinfo("Duplicate", "App already in list.")

def remove_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Remove", "Select item(s) to remove.")
        return
    for iid in selected:
        del app_list[int(iid)]
    refresh_treeview()
    save_apps()

def launch_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showinfo("Launch", "Select item(s) to launch.")
        return
    for iid in selected:
        launch_item(app_list[int(iid)])

def launch_all_apps():
    for item in app_list:
        launch_item(item)

def launch_item(item):
    if item.startswith("http://") or item.startswith("https://"):
        try:
            webbrowser.open(item)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open URL:\n{item}\n\n{e}")
    else:
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
                if messagebox.askyesno("Exit", "Exit app?"):
                    root.destroy()
                    return
            elif entered_pin == saved_pin:
                break
            else:
                messagebox.showerror("Access Denied", "Incorrect PIN. Try again.")
    else:
        while True:
            new_pin = simpledialog.askstring("Set a PIN", "Create a 5–10 digit PIN:", show="*")
            if new_pin and new_pin.isdigit() and 5 <= len(new_pin) <= 10:
                save_pin(new_pin)
                messagebox.showinfo("PIN Saved", "PIN saved securely.")
                break
            else:
                messagebox.showwarning("Invalid PIN", "PIN must be 5–10 digits.")

def reset_pin():
    if messagebox.askyesno("Reset PIN", "Are you sure to reset PIN?"):
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

# Main window setup
root = tk.Tk()
root.withdraw()

if os.path.exists(ICON_PATH):
    root.iconbitmap(ICON_PATH)

show_splash()
root.after(2500, lambda: [prompt_for_pin(), root.deiconify()])

root.title("🚀 Just One Click App Launcher")
root.geometry("700x450")
root.configure(bg="#2d2d2d")

style = ttk.Style()
style.theme_use("clam")

# Style for Treeview and buttons
style.configure("Treeview",
                background="#1e1e1e",
                foreground="white",
                fieldbackground="#1e1e1e",
                font=("Segoe UI", 10))
style.map('Treeview', background=[('selected', '#6a95ff')], foreground=[('selected', 'white')])

style.configure("TButton", foreground="white", background="#3c3f41", padding=6, font=("Segoe UI", 10))
style.configure("TLabel", background="#2d2d2d", foreground="white")
style.configure("TFrame", background="#2d2d2d")

# Alternating row colors
tree_tag_even = "#2a2a2a"
tree_tag_odd = "#3b3b3b"

style.configure("evenrow.Treeview", background=tree_tag_even)
style.configure("oddrow.Treeview", background=tree_tag_odd)

list_frame = ttk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)

columns = ("App/URL",)
tree = ttk.Treeview(list_frame, columns=columns, show="headings", selectmode="extended")
tree.heading("App/URL", text="Application Path or URL")
tree.column("App/URL", anchor="w", width=650)

vsb = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
tree.pack(side="left", fill="both", expand=True)

# Insert data into treeview with alternating row colors
def insert_items():
    for i, app in enumerate(app_list):
        tag = 'oddrow' if i % 2 else 'evenrow'
        tree.insert("", "end", iid=i, values=(app,), tags=(tag,))

load_apps()
insert_items()

style = ttk.Style()
style.theme_use('clam')  # good base theme

# Customize TButton
style.configure('Custom.TButton',
                font=('Segoe UI', 11, 'bold'),
                foreground='white',
                background='#0078d7',
                padding=10,
                borderwidth=0,
                focusthickness=3,
                focuscolor='none')

style.map('Custom.TButton',
          foreground=[('pressed', 'white'), ('active', 'white')],
          background=[('pressed', '#005a9e'), ('active', '#1a85ff')])


button_frame = ttk.Frame(root)
button_frame.pack(pady=15)

ttk.Button(button_frame, text="➕ Add App/URL",style='Custom.TButton', command=add_app).grid(row=0, column=0, padx=6, pady=4)
ttk.Button(button_frame, text="❌ Remove Selected",style='Custom.TButton', command=remove_selected).grid(row=0, column=1, padx=6)
ttk.Button(button_frame, text="🚀 Launch Selected",style='Custom.TButton', command=launch_selected).grid(row=0, column=2, padx=6)
ttk.Button(button_frame, text="⚡ Launch All",style='Custom.TButton', command=launch_all_apps).grid(row=1, column=0, padx=6, pady=6)
ttk.Button(button_frame, text="🔑 Reset PIN",style='Custom.TButton', command=reset_pin).grid(row=1, column=1, padx=6)

root.mainloop()
