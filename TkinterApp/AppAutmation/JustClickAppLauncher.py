
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import subprocess
import os
import platform
import hashlib

APP_FILE = "apps.txt"


def get_pin_file_path():
    system = platform.system()
    if system == "Windows":
        base = os.getenv("APPDATA", os.path.expanduser("~"))
        path = os.path.join(base, "AppLauncher")
    else:
        path = os.path.expanduser("~/.config/app_launcher")

    os.makedirs(path, exist_ok=True)
    return os.path.join(path, "pin.dat")


def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()


def set_pin():
    while True:
        pin = simpledialog.askstring("Set PIN", "Create a new PIN (5–10 digits):", show="*")
        if pin is None:
            return False
        if pin.isdigit() and 5 <= len(pin) <= 10:
            confirm = simpledialog.askstring("Confirm PIN", "Re-enter PIN:", show="*")
            if confirm == pin:
                with open(get_pin_file_path(), 'w') as f:
                    f.write(hash_pin(pin))
                return True
            else:
                messagebox.showerror("Mismatch", "PINs do not match.")
        else:
            messagebox.showerror("Invalid PIN", "PIN must be 5–10 digits.")


def verify_pin():
    pin_file = get_pin_file_path()
    if not os.path.exists(pin_file):
        return set_pin()

    with open(pin_file, 'r') as f:
        stored_hash = f.read().strip()

    for _ in range(3):
        entered = simpledialog.askstring("Enter PIN", "Enter your app launcher PIN:", show="*")
        if entered and hash_pin(entered) == stored_hash:
            return True
        else:
            messagebox.showwarning("Invalid", "Incorrect PIN.")
    return False


def read_apps_from_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def write_apps_to_file(file_path, apps):
    with open(file_path, 'w') as f:
        for app in apps:
            f.write(app + '\n')


def append_app_to_file(file_path, app_path):
    with open(file_path, 'a') as f:
        f.write(app_path.strip() + '\n')


def remove_app_from_file(file_path, app_path):
    apps = read_apps_from_file(file_path)
    if app_path in apps:
        apps.remove(app_path)
        write_apps_to_file(file_path, apps)


def launch_app(app_path):
    try:
        system = platform.system()
        if system == "Darwin":
            subprocess.Popen(["open", app_path])
        elif system == "Windows":
            os.startfile(app_path)
        else:
            subprocess.Popen([app_path])
    except Exception as e:
        messagebox.showerror("Launch Error", f"Failed to launch:\n{app_path}\n\n{e}")


def refresh_ui(app_list_frame):
    for widget in app_list_frame.winfo_children():
        widget.destroy()

    apps = read_apps_from_file(APP_FILE)
    for app in apps:
        app_frame = tk.Frame(app_list_frame)
        app_frame.pack(fill='x', padx=10, pady=3)

        app_name = os.path.basename(app)
        launch_btn = tk.Button(app_frame, text=f"Launch {app_name}", command=lambda a=app: launch_app(a))
        launch_btn.pack(side='left', padx=(0, 5), fill='x', expand=True)

        remove_btn = tk.Button(app_frame, text="Remove", fg="red",
                               command=lambda a=app: remove_app_and_refresh(a, app_list_frame))
        remove_btn.pack(side='right')


def remove_app_and_refresh(app_path, app_list_frame):
    if messagebox.askyesno("Confirm Remove", f"Remove {app_path} from the list?"):
        remove_app_from_file(APP_FILE, app_path)
        refresh_ui(app_list_frame)


def add_new_app(entry, app_list_frame):
    new_path = entry.get().strip()
    if not new_path:
        messagebox.showwarning("Empty Input", "Please enter a valid path.")
        return
    if not os.path.exists(new_path):
        messagebox.showwarning("Invalid Path", f"Path does not exist:\n{new_path}")
        return
    append_app_to_file(APP_FILE, new_path)
    entry.delete(0, tk.END)
    refresh_ui(app_list_frame)


def browse_file(entry):
    system = platform.system()
    if system == "Darwin":
        selected = filedialog.askdirectory(title="Select .app Folder")
    else:
        selected = filedialog.askopenfilename(title="Select Executable")
    if selected:
        entry.delete(0, tk.END)
        entry.insert(0, selected)


def create_launcher_ui():
    root = tk.Tk()
    root.title(f"App Launcher - {platform.system()}")
    root.geometry("550x650")

    app_list_frame = tk.Frame(root)
    app_list_frame.pack(pady=10, fill='both', expand=True)

    entry_frame = tk.Frame(root)
    entry_frame.pack(pady=10)

    path_entry = tk.Entry(entry_frame, width=45)
    path_entry.pack(side='left', padx=5)

    browse_button = tk.Button(entry_frame, text="Browse", command=lambda: browse_file(path_entry))
    browse_button.pack(side='left')

    add_button = tk.Button(root, text="Add App", command=lambda: add_new_app(path_entry, app_list_frame))
    add_button.pack(pady=5)

    refresh_ui(app_list_frame)
    root.mainloop()


# Entry point with hidden root for dialogs
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide root for dialogs

    if verify_pin():
        root.destroy()
        create_launcher_ui()
    else:
        messagebox.showerror("Access Denied", "Failed to authenticate. Exiting.")
        root.destroy()




