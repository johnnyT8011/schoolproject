import tkinter as tk

# Create the Tkinter window
window = tk.Tk()

# Create a label with columnspan and borderwidth
label = tk.Label(window, text="Hello, World!", borderwidth=2, relief="solid")
label.grid(row=0, column=0, columnspan=2)

# Create two buttons with columnspan
button1 = tk.Button(window, text="Button 1")
button1.grid(row=1, column=0, columnspan=2, sticky="nsew")  # Stick to all sides of the cell

button2 = tk.Button(window, text="Button 2")
button2.grid(row=2, column=0, columnspan=2, sticky="nsew")  # Stick to all sides of the cell

# Start the Tkinter event loop
window.mainloop()
