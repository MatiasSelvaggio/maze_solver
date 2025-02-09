
import time
from window import Window

def test():
    window = Window(800, 600)
    
    # Draw something simple
    window.__canvas.create_text(400, 300, text="Close the window to exit.", font=("Arial", 20), fill="black")
    
    # Keep the window open until manually closed
    window.wait_for_close()
