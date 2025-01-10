import os
import shutil
from datetime import datetime

class LogManager:
    def __init__(self, log_directory="./logs"):
        #self.log_directory = log_directory
        self.log_directory = os.path.abspath(log_directory)
        os.makedirs(self.log_directory, exist_ok=True)
        print(f"Logs directory: {os.path.abspath(self.log_directory)}")

    def get_log_file_path(self):        
        date_str = datetime.now().strftime("%Y-%m-%d")
        log_file_path = os.path.join(self.log_directory, f"room_access_log_{date_str}.txt")
        print(f"Log file path: {os.path.abspath(log_file_path)}")
        return log_file_path
	
    def write_log(self, user_id, room_id, access_status, room_state):
        os.makedirs(self.log_directory, exist_ok=True)
        log_file_path = self.get_log_file_path()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp}, User ID: {user_id}, Room ID: {room_id}, Access: {access_status}, Room State: {room_state}\n"
        
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)
        print("Log entry added:", log_entry.strip())

    def fetch_logs(self, date=None):
        """fetch logs for the specified date, grab current log abscent specification"""
        if date is None:
            date = datetime.now()

        log_file_name = f"room_access_log_{date.strftime('%Y-%m-%d')}.txt"
        log_file_path = os.path.join(self.log_directory, log_file_name)

        try:
            with open(log_file_path, "r") as log_file:
                return log_file.read()  # Return as a single string
        except FileNotFoundError:
            print(f"No logs found for {date.strftime('%Y-%m-%d')}.")
            return ""
        except Exception as e:
            print(f"Error reading log file: {e}")
            return ""

    def filter_logs(self, user_id=None, room_id=None, access_status=None):
        """filter logs by user ID, room ID, or access status"""
        logs = self.fetch_logs()
        if not logs:
            return []

        filtered_logs = []
        for log in logs:
            if ((user_id and f"User ID: {user_id}" not in log) or
                (room_id and f"Room ID: {room_id}" not in log) or
                (access_status and f"Access: {access_status}" not in log)):
                continue
            filtered_logs.append(log)

        return filtered_logs

    def archive_old_logs(self, retention_days=30):
        """archive older logs"""
        archive_dir = os.path.join(self.log_directory, "archive")
        os.makedirs(archive_dir, exist_ok=True)
        print(f"Archive directory: {os.path.abspath(archive_dir)}")
	
        now = datetime.now()
        for log_file in os.listdir(self.log_directory):
            if log_file.startswith("room_access_log_") and log_file.endswith(".txt"):
                log_date_str = log_file.split("_")[-1].replace(".txt", "")
                try: 
                   log_date = datetime.strptime(log_date_str, "%Y-%m-%d")
                   if (now - log_date).days > retention_days:
                       shutil.move(
                           os.path.join(self.log_directory, log_file),
                           os.path.join(archive_dir, log_file)
                       )
                       print(f"Archived log file: {log_file}")
                except ValueError:
                    print(f"Skipping invalid log file: {log_file}")    

