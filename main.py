import os
from nvd_cve import nvd,mitre_exploit_db
from reporter import create_pdf,create_txt,create_docx
from edb import find_exploit_url
from opener import open_ref
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
download_dir=os.path.expanduser("~/Downloads")
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)''Chrome/58.0.3029.110 Safari/537.36'}

#NR-process_cve() function takes outputs from all other functions,processess them together besides applying error handlings
def process_cve():
    cve_id = cve_var.get()
    extension = extension_var.get()
    browser = browser_var.get()

    if not cve_id or not cve_id.startswith("CVE-"):
        messagebox.showerror("Error", "Please enter a valid CVE-ID ")
        return

    def fetch_data(source_func):
        try:
            return source_func(cve_id)
        except Exception as e:
            print(f"Error fetching data using {source_func.__name__}: {e}")
            return None
# process_cve_task fetches data collected from websites and creates report, download and create zip file
    def process_cve_task():
        data = fetch_data(nvd)
        if data is None:
            data = fetch_data(mitre_exploit_db)

        if data is None:
            messagebox.showerror("Error", "Unable to fetch CVE data.")
            return

        summary, cvss_score, vector, reference1, reference2 = data
        db_links = find_exploit_url(cve_id)

        try:
            if extension == "PDF":
                create_pdf(db_links, cve_id, summary, cvss_score, vector, reference1, reference2)
            elif extension == "TXT":
                create_txt(cve_id, summary, cvss_score, vector, reference1, reference2, db_links)
            elif extension == "DOCX":
                create_docx(cve_id, summary, cvss_score, vector, reference1, reference2, db_links)

            open_ref(cve_id, browser)
            messagebox.showinfo("Info", f"{extension} saved to {download_dir}/{cve_id}.{extension}")

        except Exception as e:
            messagebox.showerror("Error", f"Error occurred during processing: {str(e)}")

    # Run the process_cve_task in a separate thread
    cve_thread = threading.Thread(target=process_cve_task)
    cve_thread.start()

# FM-initialize tkinter window

root = tk.Tk()
root.title("CVE Processing")
root.geometry("400x300")
# Create and place the CVE-ID input field
cve_label = ttk.Label(root, text="CVE-ID:")
cve_label.pack()
cve_var = tk.StringVar()
cve_entry = ttk.Entry(root, textvariable=cve_var)
cve_entry.pack()

# Create and place the Extension buttons
extension_label = ttk.Label(root, text="Select Extension:")
extension_label.pack()
extension_var = tk.StringVar()
extension_var.set("PDF")  # Default selection
extension_buttons = [
    ttk.Radiobutton(root, text="PDF", variable=extension_var, value="PDF"),
    ttk.Radiobutton(root, text="DOCX", variable=extension_var, value="DOCX"),
    ttk.Radiobutton(root, text="TXT", variable=extension_var, value="TXT")
]
for button in extension_buttons:
    button.pack()

# Create and place the Browser buttons
browser_label = ttk.Label(root, text="Select Browser:")
browser_label.pack()
browser_var = tk.StringVar()
browser_var.set("Edge")  # Default selection
browser_buttons = [
    ttk.Radiobutton(root, text="Edge", variable=browser_var, value="EDGE"),
    ttk.Radiobutton(root, text="Firefox", variable=browser_var, value="FIREFOX"),
    ttk.Radiobutton(root, text="Chrome", variable=browser_var, value="CHROME")
]
for button in browser_buttons:
    button.pack()

# Create and place the Process button
process_button = ttk.Button(root, text="Process CVE", command=process_cve)
process_button.pack()

# Start the Tkinter main loop
root.mainloop()