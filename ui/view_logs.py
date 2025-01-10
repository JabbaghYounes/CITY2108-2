import tkinter as tk
from tkinter import messagebox
from access_control.logging import LogManager
from datetime import datetime

class ViewLogs:
    def __init__(self, root, log_manager):
        self.root = root
        #self.log_manager = LogManager("./logs")
        self.log_manager = log_manager
        
    def open_logs_window(self):
        """Open a window to display today's logs."""
        logs = self.log_manager.fetch_logs()  # Fetch logs for today
        log_window = tk.Toplevel(self.root)
        log_window.title("Access Logs")
        log_window.geometry("500x400")

        text_area = tk.Text(log_window, wrap="word")
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        if logs:
            text_area.insert("1.0", logs)
        else:
            messagebox.showinfo("No Logs", "No logs found for today.")

    def open_logs_for_date(self, date):
        """Open a window to display logs for a specific date."""
        logs = self.log_manager.fetch_logs(date)
        log_window = tk.Toplevel(self.root)
        log_window.title(f"Access Logs - {date.strftime('%Y-%m-%d')}")
        log_window.geometry("500x400")

        text_area = tk.Text(log_window, wrap="word")
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        if logs:
            text_area.insert("1.0", logs)
        else:
            messagebox.showinfo("No Logs", f"No logs found for {date.strftime('%Y-%m-%d')}.")
