import tkinter as tk
from PIL import ImageGrab


def take_screenshot():
    # Get the geometry of the Tkinter window
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    width = root.winfo_width()
    height = root.winfo_height()

    # Define the bounding box for the screenshot
    bbox = (x, y, x + width, y + height)

    # Capture the screenshot
    screenshot = ImageGrab.grab(bbox)

    # Save the screenshot to a file
    screenshot.save("screenshot.png")
    print("Screenshot saved as 'screenshot.png'")


# Create a Tkinter window
root = tk.Tk()
root.title("Screenshot Example")
root.geometry("300x200")

# Add a button to capture the screenshot
screenshot_button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
screenshot_button.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
