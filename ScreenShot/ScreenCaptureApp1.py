import tkinter as tk
from tkinter import simpledialog
from PIL import ImageGrab
from docx import Document
from docx.shared import Inches
import time

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture Tool")
        self.root.geometry("800x600")
        self.root.attributes("-topmost", True)  # Keep window on top
        self.root.config(cursor="cross")  # Set cursor to crosshair for selection

        # Create a canvas for drawing the selection rectangle
        self.canvas = tk.Canvas(root, bg='gray')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        # Initialize variables
        self.rect_id = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        # Create a save button
        self.save_button = tk.Button(root, text="Save Screenshot to Word", command=self.save_screenshot, state=tk.DISABLED)
        self.save_button.pack(pady=10)

    def on_press(self, event):
        # Record the start position
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)
        self.save_button.config(state=tk.DISABLED)  # Disable the save button until selection is made

    def on_drag(self, event):
        # Update the rectangle as the user drags the mouse
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event):
        # Finalize the rectangle and enable the save button
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)
        self.save_button.config(state=tk.NORMAL)  # Enable the save button

    def save_screenshot(self):
        if not self.start_x or not self.start_y or not self.end_x or not self.end_y:
            return

        # Convert coordinates to absolute screen coordinates
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)

        # Get window position
        x0 = self.root.winfo_rootx() + x1
        y0 = self.root.winfo_rooty() + y1
        x1 = self.root.winfo_rootx() + x2
        y1 = self.root.winfo_rooty() + y2

        # Capture the screenshot
        bbox = (x0, y0, x1, y1)
        screenshot = ImageGrab.grab(bbox)

        # Save the screenshot to a file
        screenshot_filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.png"
        screenshot.save(screenshot_filename)
        print(f"Screenshot saved as '{screenshot_filename}'")

        # Save the screenshot to a Word document
        self.save_to_word(screenshot_filename)

        # Exit the application after saving
        self.root.quit()

    def save_to_word(self, image_path):
        doc = Document()
        doc.add_paragraph("Screenshot:")
        doc.add_picture(image_path, width=Inches(6))  # Adjust width as needed
        word_filename = f"screenshot_{time.strftime('%Y%m%d_%H%M%S')}.docx"
        doc.save(word_filename)
        print(f"Word document saved as '{word_filename}'")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()
