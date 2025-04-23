import tkinter as tk
from tkinter import messagebox

# List of tasks
tasks = []

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "You forgot to enter a task, princess/prince!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        del tasks[selected]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Oops!", "Select a task to make it disappear ✨")

def mark_completed():
    try:
        selected = task_listbox.curselection()[0]
        tasks[selected]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Oops!", "Select a task to mark it with ✨ magic!")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display = f"✨ {task['task']} ✨" if task['completed'] else task['task']
        task_listbox.insert(tk.END, display)

# UI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("550x630")
root.configure(bg="#B8C7E0")  # Soft Disney-style blue

# Title
title = tk.Label(
    root,
    text="To-Do List",
    font=("Segoe Print", 26, "bold"),
    bg="#B8C7E0",
    fg="#3E3C76"
)
title.pack(pady=20)

# Entry Field
task_entry = tk.Entry(
    root,
    font=("Segoe Print", 14),
    bg="#F8F0FC",
    fg="#3E3C76",
    insertbackground="#3E3C76",
    relief="flat",
    width=34,
    highlightthickness=2,
    highlightbackground="#A78BFA"
)
task_entry.pack(pady=(10, 20), ipady=10)

# Button Factory
def create_button(text, command, bg_color):
    return tk.Button(
        root, text=text,
        command=command,
        font=("Segoe Print", 12, "bold"),
        bg=bg_color,
        fg="#3E3C76",
        activebackground=bg_color,
        activeforeground="#000000",
        relief="flat",
        bd=0,
        padx=10,
        pady=10,
        width=20,
        cursor="hand2"
    )

# Buttons
add_btn = create_button("✨ Add Task", add_task, "#F9A8D4")         # Disney pink
del_btn = create_button("🗑️ Delete Task", delete_task, "#FECACA")   # Light rose
complete_btn = create_button("✔️ Mark Completed", mark_completed, "#A5F3FC")  # Sky blue

add_btn.pack(pady=5)
del_btn.pack(pady=5)
complete_btn.pack(pady=5)

# Task List
task_listbox = tk.Listbox(
    root,
    font=("Segoe Print", 13),
    bg="#F3F4F6",
    fg="#3E3C76",
    selectbackground="#A78BFA",
    selectforeground="#000000",
    highlightthickness=1,
    highlightbackground="#8B5CF6",
    relief="flat",
    width=42,
    height=12,
    bd=0,
    activestyle="none"
)
task_listbox.pack(pady=30)

# Start
root.mainloop()
