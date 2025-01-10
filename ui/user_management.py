from database.database import Database
import tkinter as tk
from tkinter import messagebox

class UserManagement:
    def __init__(self, db):
        self.db = db

        # create the main User Management window
        self.window = tk.Toplevel()
        self.window.title("User Management")
        self.window.geometry("500x400")

        # title label
        tk.Label(self.window, text="User Management", font=("Arial", 16)).pack(pady=10)

        # buttons for user operations
        tk.Button(self.window, text="Add User", width=20, command=self.add_user_form).pack(pady=5)
        tk.Button(self.window, text="Update User", width=20, command=self.update_user_form).pack(pady=5)
        tk.Button(self.window, text="Delete User", width=20, command=self.delete_user_form).pack(pady=5)
        tk.Button(self.window, text="View Users", width=20, command=self.view_users).pack(pady=5)

    def add_user_form(self):
        """GUI form to add a new user"""
        add_window = tk.Toplevel(self.window)
        add_window.title("Add User")
        add_window.geometry("300x250")

        # form fields
        tk.Label(add_window, text="Name:").pack(pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Role ID:").pack(pady=5)
        role_id_entry = tk.Entry(add_window)
        role_id_entry.pack(pady=5)

        tk.Label(add_window, text="Card ID:").pack(pady=5)
        card_id_entry = tk.Entry(add_window)
        card_id_entry.pack(pady=5)

        # save button
        def save_user():
            name = name_entry.get()
            role_id = role_id_entry.get()
            card_id = card_id_entry.get()
            if name and role_id and card_id:
                try:
                    self.add_user(name, int(role_id), card_id)
                    messagebox.showinfo("Success", "User added successfully.")
                    add_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add user: {e}")
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(add_window, text="Save", command=save_user).pack(pady=10)

    def update_user_form(self):
        """GUI form to update a user"""
        messagebox.showinfo("Update User", "Update User functionality is under development.")

    def delete_user_form(self):
        """GUI form to delete a user"""
        delete_window = tk.Toplevel(self.window)
        delete_window.title("Delete User")
        delete_window.geometry("300x150")

        tk.Label(delete_window, text="Enter User ID to delete:").pack(pady=5)
        user_id_entry = tk.Entry(delete_window)
        user_id_entry.pack(pady=5)

        def delete_user():
            user_id = user_id_entry.get()
            if user_id:
                try:
                    self.delete_user(int(user_id))
                    messagebox.showinfo("Success", f"User ID {user_id} deleted successfully.")
                    delete_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete user: {e}")
            else:
                messagebox.showerror("Error", "User ID is required.")

        tk.Button(delete_window, text="Delete", command=delete_user).pack(pady=10)

    def view_users(self):
        """fetch and display all users in a new window"""
        view_window = tk.Toplevel(self.window)
        view_window.title("View Users")
        view_window.geometry("500x400")

        query = """
        SELECT u.userID, u.name, r.roleName, u.cardID
        FROM Users u
        JOIN Roles r ON u.roleID = r.roleID
        """
        try:
            users = self.db.fetch_all(query)
            tk.Label(view_window, text="User List", font=("Arial", 14)).pack(pady=10)

            # Display users in a text area
            text_area = tk.Text(view_window, wrap="word")
            text_area.pack(expand=True, fill="both", padx=10, pady=10)

            if users:
                text_area.insert("1.0", "{:<5} {:<20} {:<15} {:<15}\n".format("ID", "Name", "Role", "Card ID"))
                text_area.insert("2.0", "-" * 55 + "\n")
                for user in users:
                    text_area.insert("end", "{:<5} {:<20} {:<15} {:<15}\n".format(*user))
            else:
                text_area.insert("1.0", "No users found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch users: {e}")

    # existing methods remain unchanged for database operations
    def add_user(self, name, role_id, card_id):
        query = "INSERT INTO Users (name, roleID, cardID) VALUES (?, ?, ?)"
        try:
            self.db.execute_query(query, (name, role_id, card_id))
            print(f"User '{name}' added successfully.")
        except Exception as e:
            print(f"Error adding user: {e}")

    def update_user(self, user_id, name=None, role_id=None, card_id=None):
        updates = []
        params = []
        if name:
            updates.append("name = ?")
            params.append(name)
        if role_id:
            updates.append("roleID = ?")
            params.append(role_id)
        if card_id:
            updates.append("cardID = ?")
            params.append(card_id)

        if updates:
            query = f"UPDATE Users SET {', '.join(updates)} WHERE userID = ?"
            params.append(user_id)
            try:
                self.db.execute_query(query, params)
                print(f"User ID {user_id} updated successfully.")
            except Exception as e:
                print(f"Error updating user: {e}")

    def delete_user(self, user_id):
        query = "DELETE FROM Users WHERE userID = ?"
        try:
            self.db.execute_query(query, (user_id,))
            print(f"User ID {user_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")
