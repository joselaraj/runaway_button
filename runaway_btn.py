import tkinter as tk
import random
import webbrowser

attempt_count = 0

def move_button(event):
    global attempt_count
    attempt_count += 1
    
    if attempt_count <= 20:  # Button moves only before 20 attempts
        # Get the size of the window
        window_width = root.winfo_width()
        window_height = root.winfo_height()
        
        # Get the size of the button
        button_width = runaway_button.winfo_width()
        button_height = runaway_button.winfo_height()

        # Calculate new position for the button
        new_x = random.randint(0, window_width - button_width)
        new_y = random.randint(0, window_height - button_height)

        # Move the button to the new position
        runaway_button.place(x=new_x, y=new_y)

def open_youtube():
    youtube_url = "https://www.linkedin.com/in/jose-lara-6323412b3"  
    webbrowser.open(youtube_url)

# Create the main window
root = tk.Tk()
root.title("Runaway Button")

# Set the window size
root.geometry("400x400")

# Create the runaway button
runaway_button = tk.Button(root, text="Click me \U0001f600", command=open_youtube)
runaway_button.place(x=150, y=150)

# Bind the button to the move function when the mouse enters its area
runaway_button.bind("<Enter>", move_button)

# Run the main loop
root.mainloop()
