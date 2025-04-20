# demo.py
#
# Lektionspass 2, tisdag 08-april-2025
#
# Robin startade dagen med att koda biblioteket Tkinter
# Detta är dagens andra  skript
#
# Dagens föreläsning blev följande fyra filer
#       ./part1.py          # 1a timmen, med bas i Tkinter
#       ./demo.py           # 1a timmen, med bas i Tkinter
#       ./flaskintro.py             # 2a timmen, med bas i Flask
#       ./templates/index.html      # 2a timmen, med bas i Flask
#  
import tkinter as tk
from tkinter import messagebox





def on_submit():
    name = entry.get()
    selected_gender = gender_var.get()
    subscribed = subscribe_var.get()
    language = language_var.get()
    
    info = f"Name: {name}\nGender: {selected_gender}\nSubscribed: {subscribed}\nLanguage: {language}"
    messagebox.showinfo("Submittedinfo", info)





# Main window
root = tk.Tk()
root.title("Lars Demo - kopia av Robin's")
root.geometry("350x350")


# Create Label
label_name = tk.Label(root, text="Name:")
label_name.pack(pady=5)


# Create Entry Widget
entry = tk.Entry(root)
entry.pack(pady=5)


# Radiobuttons for gender
label_gender = tk.Label(root, text="Gender:")
label_gender.pack(pady=5)

gender_var = tk.StringVar(value="Other")

radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_male.pack()

radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_female.pack()

radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")
radio_other.pack()




# Checkbox
subscribe_var = tk.BooleanVar()

checkbox = tk.Checkbutton(root, text="Subscribe to our newsletter?", variable=subscribe_var)
checkbox.pack(pady=5)


label_language = tk.Label(root, text="Favorite Language")
label_language.pack(pady=5)

# Dropdown menu
languages = ['Python','Java','Javascripts','C#','LabView']
language_var = tk.StringVar(value=languages[1])


dropdown = tk.OptionMenu(root, language_var, *languages)
dropdown.pack()


# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

root.mainloop()


