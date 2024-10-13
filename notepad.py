import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import Menu

# Global variable to track the current file
current_file = None

def new_file():
    global current_file
    text_edit.delete(1.0, tk.END)
    current_file = None
    root.title("My Notepad")

def open_file():
    global current_file
    file_location = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_location:
        try:
            with open(file_location, "r") as file_input:
                text_edit.delete(1.0, tk.END)
                text_edit.insert(tk.END, file_input.read())
            current_file = file_location
            root.title(f"My Notepad - {current_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file, "w") as file_output:
                file_output.write(text_edit.get(1.0, tk.END))
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_location = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_location:
        try:
            with open(file_location, "w") as file_output:
                file_output.write(text_edit.get(1.0, tk.END))
            current_file = file_location
            root.title(f"My Notepad - {current_file}")
            messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

def undo_action():
    text_edit.edit_undo()

def cut_text():
    text_edit.event_generate("<<Cut>>")

def copy_text():
    text_edit.event_generate("<<Copy>>")

def paste_text():
    text_edit.event_generate("<<Paste>>")

def delete_text():
    text_edit.delete("sel.first", "sel.last")

def select_all():
    text_edit.tag_add("sel", 1.0, tk.END)

def show_about():
    messagebox.showinfo("About", "My Notepad\nVersion 1.0\nCreated with Tkinter")

# Create main window
root = tk.Tk()
root.title("My Notepad")
root.geometry("800x600")

# Create text area for editing
text_edit = tk.Text(root, wrap=tk.WORD)
text_edit.pack(expand=True, fill='both')

# Create menu bar
menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file, accelerator="Ctrl+Shift+S")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_action, accelerator="Ctrl+Z")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_command(label="Delete", command=delete_text)
edit_menu.add_separator()
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure menu bar
root.config(menu=menu_bar)

# Bind keyboard shortcuts
root.bind('<Control-n>', lambda event: new_file())
root.bind('<Control-o>', lambda event: open_file())
root.bind('<Control-s>', lambda event: save_file())
root.bind('<Control-Shift-S>', lambda event: save_as_file())
root.bind('<Control-z>', lambda event: undo_action())
root.bind('<Control-x>', lambda event: cut_text())
root.bind('<Control-c>', lambda event: copy_text())
root.bind('<Control-v>', lambda event: paste_text())
root.bind('<Control-a>', lambda event: select_all())

# Run the application
root.mainloop()
