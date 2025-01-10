import sqlite3
import os

class Database:
    def __init__(self, db_name="access_control.db"):
        # Resolve the database path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(script_dir, "..", db_name)
        print(f"Database path resolved to: {self.db_path}")

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print(f"Connected to database at {self.db_path}")

    def create_tables(self, schema_file="schema.sql"):
        # Resolve the schema file path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(script_dir, schema_file)

        if not os.path.exists(schema_path):
            print(f"Error: Schema file '{schema_path}' not found.")
            return

        with open(schema_path, 'r') as f:
            sql = f.read()

        try:
            self.cursor.executescript(sql)
            self.conn.commit()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_initial_data(self, data_file="init_data.sql"):
        # Resolve the data file path
        script_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(script_dir, data_file)

        if not os.path.exists(data_path):
            print(f"Error: Data file '{data_path}' not found.")
            return

        with open(data_path, 'r') as f:
            sql = f.read()

        try:
            self.cursor.executescript(sql)
            self.conn.commit()
            print("Initial data inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting initial data: {e}")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error during execute_query: {e}")

    def fetch_all(self, query, params=None):
        print(f"Executing fetch_all with query: {query}, params: {params}")
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Database error during fetch_all: {e}")
            return []

    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    # Example usage to create tables and insert initial data
    db = Database()
    db.create_tables("schema.sql")  # Ensure schema.sql exists in the database folder
    db.insert_initial_data("init_data.sql")  # Optional: Add initial data if file exists
    db.close()
