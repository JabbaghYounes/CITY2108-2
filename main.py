import tkinter as tk
from ui.main_ui import MainUI
from database.database import Database


if __name__ == "__main__":
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Initialize the shared database instance
    db = Database("access_control.db")

    # Launch the main UI
    app = MainUI(root, db)

    # Run the main Tkinter loop
    root.mainloop()

    # Close the database connection when the app exits
    db.close()
