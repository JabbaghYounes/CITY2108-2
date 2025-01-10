import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from database.database import Database

class SimulateAccess:
    def __init__(self, db):
        self.db = db  # Use the shared Database instance

    def open_simulate_access_window(self):
        """open the Simulate Access window"""
        simulate_window = tk.Toplevel()
        simulate_window.title("Simulate Access")
        simulate_window.geometry("400x300")

        # input fields
        tk.Label(simulate_window, text="User Card ID:").pack(pady=5)
        card_id_entry = tk.Entry(simulate_window)
        card_id_entry.pack(pady=5)

        tk.Label(simulate_window, text="Room ID:").pack(pady=5)
        room_id_entry = tk.Entry(simulate_window)
        room_id_entry.pack(pady=5)

        def process_simulation():
            card_id = card_id_entry.get().strip()
            room_id = room_id_entry.get().strip()

            if card_id and room_id:
                try:
                    # fetch user and room details
                    user_query = """
                    SELECT u.name, r.roleName
                    FROM Users u
                    JOIN Roles r ON u.roleID = r.roleID
                    WHERE u.cardID = ?
                    """
                    user = self.db.fetch_all(user_query, (card_id,))
                    room_query = "SELECT type, state FROM Rooms WHERE roomID = ?"
                    room = self.db.fetch_all(room_query, (room_id,))

                    if user and room:
                        user_name, user_role = user[0]
                        room_type, room_state = room[0]

                        # access logic
                        access_granted = False
                        if room_state == "NORMAL":
                            if user_role in {"Manager", "Security"}:
                                access_granted = True
                            elif user_role == "Staff Member" and room_type in {"Lecture Hall", "Teaching Room"}:
                                access_granted = True
                        elif room_state == "EMERGENCY":
                            if user_role in {"Security", "Emergency Responder"}:
                                access_granted = True

                        # write to log
                        log_entry = f"{user_name} ({card_id}) attempted to access Room {room_id} ({room_type}) - {'Granted' if access_granted else 'Denied'}\n"
                        self.write_log(log_entry)

                        # display result
                        messagebox.showinfo("Access Simulation", log_entry)
                    else:
                        messagebox.showerror("Error", "Invalid Card ID or Room ID.")
                except Exception as e:
                    messagebox.showerror("Error", f"Simulation failed: {e}")
            else:
                messagebox.showerror("Error", "Card ID and Room ID are required.")

        tk.Button(simulate_window, text="Simulate Access", command=process_simulation).pack(pady=10)

    def write_log(self, log_entry):
        """write a log entry to daily log file"""
        log_filename = f"room_access_log_{datetime.now().strftime('%Y-%m-%d')}.txt"
        try:
            with open(log_filename, "a") as log_file:
                log_file.write(log_entry)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to write to log file: {e}")
