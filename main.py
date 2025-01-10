import tkinter as tk
from ui.main_ui import MainUI
from database.database import Database


if __name__ == "__main__":
    # setup main tkinter window
    root = tk.Tk()

    # setup shared database instance
    db = Database("access_control.db")

    # launch main gui
    app = MainUI(root, db)

    # run main tkinter loop
    root.mainloop()

    # close db connection when exit
    db.close()
