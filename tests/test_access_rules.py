import unittest
from access_control.rules import AccessControl

class TestAccessControl(unittest.TestCase):
    def setUp(self):
        # Example setup for users, rooms, and times
        self.access_control = AccessControl()
        self.staff_user = {"userID": 1, "role": "Staff Member"}
        self.student_user = {"userID": 2, "role": "Student"}
        self.room_normal = {"roomID": 101, "type": "Lecture Hall", "state": "NORMAL"}
        self.room_emergency = {"roomID": 102, "type": "Lecture Hall", "state": "EMERGENCY"}
        self.time_allowed = "10:00:00"
        self.time_restricted = "23:30:00"

    def test_staff_access_normal(self):
        result = self.access_control.check_access(self.staff_user, self.room_normal, self.time_allowed)
        self.assertTrue(result, "Staff should have access in NORMAL state.")

    def test_student_access_restricted_time(self):
        result = self.access_control.check_access(self.student_user, self.room_normal, self.time_restricted)
        self.assertFalse(result, "Student should not have access outside allowed time.")

    def test_emergency_responder_access(self):
        emergency_user = {"userID": 3, "role": "Emergency Responder"}
        result = self.access_control.check_access(emergency_user, self.room_emergency, self.time_allowed)
        self.assertTrue(result, "Emergency responders should have access during EMERGENCY state.")

if __name__ == "__main__":
    unittest.main()
