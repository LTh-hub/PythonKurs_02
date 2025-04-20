# part1.py
#
# Lektionspass 2 - 2025-april-08
#
# Robin startade dagen med att koda biblioteket Tkinter
# Detta är dagens start skript
#
# Dagens föreläsning blev följande fyra filer
#       ./part1.py          # 1a timmen, med bas i Tkinter
#       ./demo.py           # 1a timmen, med bas i Tkinter
#       ./flaskintro.py             # 2a timmen, med bas i Flask
#       ./templates/index.html      # 2a timmen, med bas i Flask
#  
import tkinter as tk

# create main window
root = tk.Tk()
root.title("Basic GUI Window")
root.geometry("300x350")

# Label
label = tk.Label(root, text="this is a label")
label.pack(pady=5)


# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)


# Button
button = tk.Button(root, text="Click me")
button.pack(pady=5)

# Radio button
radio1 = tk.Radiobutton(root, text="Option 1", value=1)
radio1.pack()

radio2 = tk.Radiobutton(root, text="Option 2", value=2)
radio2.pack()


# Checkbox
checkbox = tk.Checkbutton(root, text="prenumere")
checkbox.pack(pady=5)

# Dropdown menu
options = ['Javascript','Python','C#','LabView','MatLab']
dropdown_var = tk.StringVar(value=options[1])

dropdown_label = tk.Label(root, text="Choos favorit language")
dropdown_label.pack(pady=10)

dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack()


# run the application
root.mainloop()



