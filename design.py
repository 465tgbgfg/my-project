import customtkinter as ctk

# Setup
ctk.set_appearance_mode("light")  # "dark" bhi try kar sakte ho
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("300x400")
app.title("🧮 Calculator by Bhavin")

# Entry field
entry = ctk.CTkEntry(app, font=("Arial", 24), justify="right")
entry.pack(pady=20, padx=10, fill="x")

# Function to handle button press
def press(val):
    entry.insert("end", val)

def clear():                                                                            
    entry.delete(0, "end")

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, "end")
        entry.insert("end", str(result))                    
    except:
        entry.delete(0, "end")
        entry.insert("end", "Error")

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
]

for row in buttons:
    frame = ctk.CTkFrame(app)   
    frame.pack(pady=5)
    for btn in row:
        if btn == "=":                                                                                                                     
           
            b = ctk.CTkButton(frame, text=btn, width=50, command=calculate)
        else:
            b = ctk.CTkButton(frame, text=btn, width=50, command=lambda val=btn: press(val))
        b.pack(side="left", padx=5)

# Clear button
clear_btn = ctk.CTkButton(app, text="Clear", command=clear)
clear_btn.pack(pady=10)

app.mainloop()
