# Import necessary libraries
import customtkinter as ctk  # Modern Tkinter wrapper for stylish GUIs
import math  # Provides mathematical functions for scientific calculations

# -------------------- Appearance Settings --------------------
ctk.set_appearance_mode("Dark")  # Set app theme to dark mode for better eye comfort
ctk.set_default_color_theme("dark-blue")  # Set the primary color theme of the app

# -------------------- App Window Setup --------------------
app = ctk.CTk()  # Create the main application window
app.geometry("440x600")  # Set fixed window size (width x height)
app.title("Remoshan's Scientific Calculator")  # Window title
app.configure(fg_color="#1C1C1C")  # Background color of the window
app.resizable(False, False)  # Disable window resizing for consistent layout

# -------------------- Display Area --------------------
entry = ctk.CTkEntry(
    app,
    font=("SF Pro Display", 36, "bold"),  # Font style and size for display
    justify="right",  # Right-align the entered text (standard for calculators)
    width=400,
    height=80,
    corner_radius=10,  # Rounded corners for the entry field
    text_color="white",
    fg_color="#1C1C1C",  # Match background for seamless look
    border_width=0  # No border for a clean appearance
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=(10, 5))  # Place entry at the top spanning 4 columns

# -------------------- Core Functionalities --------------------

def button_click(value):
    """
    Append the clicked button's value to the entry field.
    """
    entry.insert("end", str(value))

def clear_entry():
    """
    Clear all text from the entry field.
    """
    entry.delete(0, "end")

def backspace():
    """
    Remove the last character from the entry field (like a backspace key).
    """
    current = entry.get()
    entry.delete(0, "end")
    entry.insert(0, current[:-1])  # Insert string except the last character

def evaluate():
    """
    Evaluate the mathematical expression in the entry field.
    Converts user-friendly symbols to Python math expressions.
    Displays result or 'Error' if evaluation fails.
    """
    try:
        expression = entry.get()

        # Replace symbols with Python math equivalents
        expression = expression.replace("√", "math.sqrt")
        expression = expression.replace("^", "**")
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")

        # Use eval to calculate the expression
        result = eval(expression)

        entry.delete(0, "end")
        entry.insert("end", round(result, 8))  # Round result for cleaner display
    except:
        entry.delete(0, "end")
        entry.insert("end", "Error")  # Show error message for invalid inputs

def square():
    """
    Calculate the square of the current value in the entry.
    """
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, "end")
        entry.insert("end", result)
    except:
        entry.delete(0, "end")
        entry.insert("end", "Error")

def inverse():
    """
    Calculate the inverse (1/x) of the current value in the entry.
    """
    try:
        value = float(entry.get())
        result = 1 / value
        entry.delete(0, "end")
        entry.insert("end", result)
    except:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# -------------------- Button Creation Helper --------------------
def create_button(text, command, row, col, bg="#505050", fg="white"):
    """
    Helper function to create and place buttons on the grid.
    Parameters:
        - text: The label on the button
        - command: The function to call on button click
        - row, col: Grid position
        - bg: Background color of button
        - fg: Text color of button
    """
    btn = ctk.CTkButton(
        app,
        text=text,
        command=command,
        width=75,
        height=55,
        corner_radius=28,
        font=("SF Pro Display", 18),
        fg_color=bg,
        text_color=fg,
        hover_color="#6b6b6b"
    )
    btn.grid(row=row, column=col, padx=2, pady=2)

# -------------------- Top Row Buttons --------------------
# Special function buttons just below display: Clear, parentheses, backspace
create_button("C", clear_entry, 1, 0, bg="#FF9500")  # Clear button with standout color
create_button("(", lambda: button_click("("), 1, 1)
create_button(")", lambda: button_click(")"), 1, 2)
create_button("⌫", backspace, 1, 3, bg="#333333")  # Backspace button with darker color

# -------------------- Button Layout --------------------
# Layout for all calculator buttons organized by rows and columns
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["sin", "cos", "tan", "="],
    ["ln", "π", "e", "√"],
    ["x²", "1/x", "log", ""],  # Empty string to maintain grid alignment
]

# -------------------- Button Placement --------------------
for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text == "":
            continue  # Skip empty grid cells
        elif text == "=":
            cmd = evaluate
            color = "#FF9500"  # Highlight equal button
        elif text == "C":
            cmd = clear_entry
            color = "#FF9500"  # Highlight clear button
        elif text == "x²":
            cmd = square
            color = "#FF9500"  # Highlight square button
        elif text == "1/x":
            cmd = inverse
            color = "#FF9500"  # Highlight inverse button
        else:
            cmd = lambda val=text: button_click(val)  # Default button input
            color = "#505050"  # Default button color

        create_button(text, cmd, i + 2, j, bg=color)  # Place buttons starting at row 2

# -------------------- Reduce Row Spacing --------------------
# Fix row heights to create a uniform button grid
for i in range(10):
    app.grid_rowconfigure(i, minsize=55)

# -------------------- Start the App --------------------
app.mainloop()  # Run the Tkinter event loop to start the application