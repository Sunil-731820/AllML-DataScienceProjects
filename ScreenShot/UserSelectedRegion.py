import tkinter as tk
from PIL import ImageGrab


class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture")
        self.root.geometry("400x300")

        self.label = tk.Label(root, text="Click and drag to select the area to capture", pady=10)
        self.label.pack()

        self.capture_button = tk.Button(root, text="Capture", command=self.capture_screen)
        self.capture_button.pack(pady=10)

        self.canvas = tk.Canvas(root, bg='gray')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind mouse events for selection
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.rect_id = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect_id:
            self.canvas.delete(self.rect_id)
        self.rect_id = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y,
                                                    outline='red', width=2)

    def on_drag(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect_id, self.start_x, self.start_y, self.end_x, self.end_y)

    def capture_screen(self):
        if not self.start_x or not self.start_y or not self.end_x or not self.end_y:
            return

        # Adjust coordinates
        x1 = min(self.start_x, self.end_x)
        y1 = min(self.start_y, self.end_y)
        x2 = max(self.start_x, self.end_x)
        y2 = max(self.start_y, self.end_y)

        # Capture the selected area
        bbox = (self.root.winfo_rootx() + x1, self.root.winfo_rooty() + y1, self.root.winfo_rootx() + x2,
                self.root.winfo_rooty() + y2)
        screenshot = ImageGrab.grab(bbox)
        screenshot.save("selected_screenshot.png")
        print("Screenshot saved as 'selected_screenshot.png'")


if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()
