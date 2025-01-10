import os
from access_control.logging import LogManager

def test_write_log():
    log_manager = LogManager(log_directory="./test_logs")
    log_manager.write_log(user_id=1, room_id=101, access_status="Granted", room_state="NORMAL")
    log_file_path = log_manager.get_log_file_path()

    assert os.path.exists(log_file_path), "Log file should exist"
    with open(log_file_path, "r") as file:
        logs = file.readlines()
    assert "User ID: 1" in logs[-1], "Log entry should contain User ID"
    assert "Room ID: 101" in logs[-1], "Log entry should contain Room ID"
