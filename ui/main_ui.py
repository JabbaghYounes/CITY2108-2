import tkinter as tk
from tkinter import messagebox
from ui.user_management import UserManagement
from ui.room_management import RoomManagement
from ui.simulate_access import SimulateAccess
from access_control.logging import LogManager
from ui.view_logs import ViewLogs


class MainUI:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        
        # initialise LogManager with the desired directory
        #log_manager = LogManager(log_directory="./logs")
        log_manager = LogManager("./logs")
        
        # viewlog inint with root
        self.view_logs_manager = ViewLogs(self.root, log_manager)

        # setting up main window
        self.root.title("Room Access Control System")
        self.root.geometry("600x400")

        # main menu setup
        tk.Label(self.root, text="Room Access Control System", font=("Arial", 18)).pack(pady=20)

        # button setup
        tk.Button(self.root, text="User Management", width=20, command=self.open_user_management).pack(pady=10)
        tk.Button(self.root, text="Room Management", width=20, command=self.open_room_management).pack(pady=10)
        tk.Button(self.root, text="Simulate Access", width=20, command=self.simulate_access).pack(pady=10)
        tk.Button(self.root, text="View Logs", width=20, command=self.view_logs).pack(pady=10)
        tk.Button(self.root, text="Exit", width=20, command=self.root.quit).pack(pady=10)

    def open_user_management(self):
        UserManagement(self.db)

    def open_room_management(self):
        RoomManagement(self.db)

    def simulate_access(self):
        SimulateAccess(self.db).open_simulate_access_window()

    def view_logs(self):
        self.view_logs_manager.open_logs_window()
        
