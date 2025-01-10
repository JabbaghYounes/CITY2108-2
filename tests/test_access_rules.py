import sys
import os
import unittest
from access_control.rules import AccessControl
from access_control.logging import LogManager

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

class TestAccessControl(unittest.TestCase):
    def setUp(self):
        # example setup for users, rooms and times
        self.log_manager = LogManager(log_directory="./test_logs")
        self.staff_user = {"id": 1, "role": "Staff Member"}
        self.student_user = {"id": 2, "role": "Student"}
        self.emergency_responder = {"id": 3, "role": "Emergency Responder"}
        self.room_normal = {"id": 101, "type": "Lecture Hall"}
        self.room_emergency = {"id": 102, "type": "Lecture Hall"}
        self.time_allowed = "10:00:00"
        self.time_restricted = "23:30:00"

    def test_staff_access_normal(self):
        """test access for staff during normal state"""
        access_control = AccessControl(
            user=self.staff_user,
            room=self.room_normal,
            time=self.time_allowed,
            room_state="NORMAL"
        )
        result, _ = access_control.check_access(self.log_manager)
        self.assertEqual(result, "Granted", "Staff should have access in NORMAL state.")

    def test_student_access_restricted_time(self):
        """test access for students during restricted time"""
        access_control = AccessControl(
            user=self.student_user,
            room=self.room_normal,
            time=self.time_restricted,
            room_state="NORMAL"
        )
        result, _ = access_control.check_access(self.log_manager)
        self.assertEqual(result, "Denied", "Student should not have access outside allowed time.")

    def test_emergency_responder_access(self):
        """test access for emergency responders during emergency state"""
        access_control = AccessControl(
            user=self.emergency_responder,
            room=self.room_emergency,
            time=self.time_allowed,
            room_state="EMERGENCY"
        )
        result, _ = access_control.check_access(self.log_manager)
        self.assertEqual(result, "Granted", "Emergency responders should have access during EMERGENCY state.")

    def test_role_room_type_restrictions(self):
        """test room type access restrictions"""
        restricted_room = {"id": 103, "type": "Secure Room"}
        access_control = AccessControl(
            user=self.student_user,
            room=restricted_room,
            time=self.time_allowed,
            room_state="NORMAL"
        )
        result, _ = access_control.check_access(self.log_manager)
        self.assertEqual(result, "Denied", "Students should not have access to secure rooms.")

if __name__ == "__main__":
    unittest.main()
