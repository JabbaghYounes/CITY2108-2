from database.database import Database
import tkinter as tk
from tkinter import messagebox


class RoomManagement:
    def __init__(self, db):
        # debug: checking db connection
        #print(f"debug: RoomManagement received db: {db}")
        #if not isinstance(db, Database):
            #raise TypeError(f"Expected Database instance, got {type(db)}")
        self.db = db  # Use the shared Database instance
        #print(f"RoomManagement using db: {self.db}")
        self.window = tk.Toplevel()
        self.window.title("Room Management")
        self.window.geometry("400x300")

        tk.Label(self.window, text="Room Management", font=("Arial", 16)).pack(pady=10)

        # Buttons for room operations
        tk.Button(self.window, text="Add Room", width=20, command=self.add_room).pack(pady=5)
        tk.Button(self.window, text="Update Room", width=20, command=self.update_room).pack(pady=5)
        tk.Button(self.window, text="Delete Room", width=20, command=self.delete_room).pack(pady=5)
        tk.Button(self.window, text="Change Room State", width=20, command=self.change_room_state).pack(pady=5)
        tk.Button(self.window, text="View Rooms", width=20, command=self.view_rooms).pack(pady=5)
        
        # debug: check for db conection confirmation
        #print(f"RoomManagement using db: {self.db}")

    def add_room(self):
        # debug: checking db connection
        #print(f"debug: add_room using db: {self.db}")  
        """Open a form to add a new room."""
        add_window = tk.Toplevel(self.window)
        add_window.title("Add Room")
        add_window.geometry("300x200")

        # Form fields
        tk.Label(add_window, text="Room Type:").pack(pady=5)
        room_type_entry = tk.Entry(add_window)
        room_type_entry.pack(pady=5)

        tk.Label(add_window, text="Room State (NORMAL/EMERGENCY):").pack(pady=5)
        room_state_entry = tk.Entry(add_window)
        room_state_entry.pack(pady=5)

        def save_room():
            """Save the new room to the database."""
            room_type = room_type_entry.get().strip()
            room_state = room_state_entry.get().strip().upper()

            if room_type and room_state in {"NORMAL", "EMERGENCY"}:
                try:
                    self.db.execute_query("INSERT INTO Rooms (type, state) VALUES (?, ?)", (room_type, room_state))
                    messagebox.showinfo("Success", "Room added successfully.")
                    add_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add room: {e}")
            else:
                messagebox.showerror("Input Error", "Invalid input. Please enter valid data.")

        tk.Button(add_window, text="Save Room", command=save_room).pack(pady=10)

    def update_room(self):
    	"""GUI form to update a room."""
    	update_window = tk.Toplevel(self.window)
    	update_window.title("Update Room")
    	update_window.geometry("300x250")

    	# Form Fields
    	tk.Label(update_window, text="Room ID:").pack(pady=5)
    	room_id_entry = tk.Entry(update_window)
    	room_id_entry.pack(pady=5)

    	tk.Label(update_window, text="New Room Type:").pack(pady=5)
    	room_type_entry = tk.Entry(update_window)
    	room_type_entry.pack(pady=5)

    	tk.Label(update_window, text="New Room State (NORMAL/EMERGENCY):").pack(pady=5)
    	room_state_entry = tk.Entry(update_window)
    	room_state_entry.pack(pady=5)

    	def save_update():
        	room_id = room_id_entry.get().strip()
        	room_type = room_type_entry.get().strip()
        	room_state = room_state_entry.get().strip().upper()

        	if room_id and (room_type or room_state in {"NORMAL", "EMERGENCY"}):
            		updates = []
            		params = []

            		if room_type:
                		updates.append("type = ?")
                		params.append(room_type)
            		if room_state in {"NORMAL", "EMERGENCY"}:
                		updates.append("state = ?")
                		params.append(room_state)

            		params.append(room_id)

            		query = f"UPDATE Rooms SET {', '.join(updates)} WHERE roomID = ?"
            		try:
                		self.db.execute_query(query, params)
                		messagebox.showinfo("Success", "Room updated successfully.")
                		update_window.destroy()
            		except Exception as e:
                		messagebox.showerror("Error", f"Failed to update room: {e}")
        	else:
            		messagebox.showerror("Error", "Invalid input. Room ID is required, and at least one field must be updated.")

    	tk.Button(update_window, text="Update Room", command=save_update).pack(pady=10)

    def delete_room(self):
    	"""GUI form to delete a room."""
    	delete_window = tk.Toplevel(self.window)
    	delete_window.title("Delete Room")
    	delete_window.geometry("300x150")

    	tk.Label(delete_window, text="Enter Room ID to delete:").pack(pady=5)
    	room_id_entry = tk.Entry(delete_window)
    	room_id_entry.pack(pady=5)

    	def confirm_delete():
        	room_id = room_id_entry.get().strip()
        	if room_id:
            		try:
                		self.db.execute_query("DELETE FROM Rooms WHERE roomID = ?", (room_id,))
                		messagebox.showinfo("Success", "Room deleted successfully.")
                		delete_window.destroy()
            		except Exception as e:
                		messagebox.showerror("Error", f"Failed to delete room: {e}")
        	else:
            		messagebox.showerror("Error", "Room ID is required.")

    	tk.Button(delete_window, text="Delete Room", command=confirm_delete).pack(pady=10)
    
    def change_room_state(self):
    	"""GUI form to change room state."""
    	state_window = tk.Toplevel(self.window)
    	state_window.title("Change Room State")
    	state_window.geometry("300x200")

    	tk.Label(state_window, text="Room ID:").pack(pady=5)
    	room_id_entry = tk.Entry(state_window)
    	room_id_entry.pack(pady=5)

    	tk.Label(state_window, text="New State (NORMAL/EMERGENCY):").pack(pady=5)
    	new_state_entry = tk.Entry(state_window)
    	new_state_entry.pack(pady=5)

    	def update_state():
        	room_id = room_id_entry.get().strip()
        	new_state = new_state_entry.get().strip().upper()

        	if room_id and new_state in {"NORMAL", "EMERGENCY"}:
            		try:
                		self.db.execute_query("UPDATE Rooms SET state = ? WHERE roomID = ?", (new_state, room_id))
                		messagebox.showinfo("Success", f"Room state updated to {new_state}.")
                		state_window.destroy()
            		except Exception as e:
                		messagebox.showerror("Error", f"Failed to change room state: {e}")
        	else:
            		messagebox.showerror("Error", "Room ID and a valid new state (NORMAL/EMERGENCY) are required.")

    	tk.Button(state_window, text="Change State", command=update_state).pack(pady=10)

    def view_rooms(self):
        # debug: checking db connection
        #print(f"debug: view_rooms using db: {self.db}") 
        """Fetch and display all rooms in a new window."""
        try:
            rooms = self.db.fetch_all("SELECT * FROM Rooms")
            view_window = tk.Toplevel(self.window)
            view_window.title("View Rooms")
            view_window.geometry("400x300")

            text_area = tk.Text(view_window, wrap="word")
            text_area.pack(expand=True, fill="both", padx=10, pady=10)

            if rooms:
                text_area.insert("1.0", f"{'Room ID':<10}{'Type':<15}{'State':<10}\n")
                text_area.insert("2.0", "-" * 35 + "\n")
                for room in rooms:
                    text_area.insert("end", f"{room[0]:<10}{room[1]:<15}{room[2]:<10}\n")
            else:
                text_area.insert("1.0", "No rooms found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch rooms: {e}")
