import re
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    # prompts for file selection
    cto_file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if cto_file_path:
        selected_file_label.config(text=f"Selected File: {cto_file_path}")
        process_file(cto_file_path)

def process_file(cto_file_path):
    # regex search for all IPs and domains and adds them to file_text (text widget)
    try:
        with open(cto_file_path, 'r') as file:#, open("temp.txt", 'w+') as temp_file:
            for line in file:
                if not line.isspace():
                    #ips_found = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                    ips_found = re.findall(".*\..*", line)
                    for item in ips_found:
                        print(item)
                        item = item.rstrip() + "\n"
                        #temp_file.write(item)
                        file_text.insert(tk.END, item)

    except Exception as e:
        selected_file_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("CTO Extractor 9000")

open_button = tk.Button(root, text="Open File", command=open_file_dialog)
open_button.pack(padx=20, pady=20)

selected_file_label = tk.Label(root, text="Selected File:")
selected_file_label.pack()

file_text = tk.Text(root, wrap=tk.WORD, height=30, width=60)
file_text.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()