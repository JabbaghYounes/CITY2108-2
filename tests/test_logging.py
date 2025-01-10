import os
import unittest
from access_control.logging import LogManager

class TestLogManager(unittest.TestCase):
    def setUp(self):
        """set up a test instance of LogManager"""
        self.log_directory = "./test_logs"
        self.log_manager = LogManager(log_directory=self.log_directory)

    def tearDown(self):
        """clean up test logs directory after each test"""
        if os.path.exists(self.log_directory):
            for file in os.listdir(self.log_directory):
                file_path = os.path.join(self.log_directory, file)
                os.remove(file_path)
            os.rmdir(self.log_directory)

    def test_write_log(self):
        """test write_log method"""
        self.log_manager.write_log(user_id=1, room_id=101, access_status="Granted", room_state="NORMAL")
        log_file_path = self.log_manager.get_log_file_path()

        # assert log file exists
        self.assertTrue(os.path.exists(log_file_path), "Log file should exist")

        # read and validate last log entry
        with open(log_file_path, "r") as file:
            logs = file.readlines()
        self.assertGreater(len(logs), 0, "Log file should contain entries")

        last_log = logs[-1]
        self.assertIn("User ID: 1", last_log, "Log entry should contain User ID")
        self.assertIn("Room ID: 101", last_log, "Log entry should contain Room ID")
        self.assertIn("Access: Granted", last_log, "Log entry should contain Access Status")
        self.assertIn("Room State: NORMAL", last_log, "Log entry should contain Room State")

    def test_log_directory_creation(self):
        """test that log directory is created if not exisitng"""
        self.assertTrue(os.path.exists(self.log_directory), "Log directory should be created")

if __name__ == "__main__":
    unittest.main()
