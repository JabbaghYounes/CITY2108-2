from datetime import datetime
from access_control.logging import LogManager

class AccessControl:
    def __init__(self, user, room, time, room_state):
        self.user = user
        self.room = room
        self.time = time
        self.room_state = room_state

    def check_access(self, log_manager):
        role = self.user['role']
        room_type = self.room['type']
        state = self.room_state

        # determine access
        if state == 'EMERGENCY' and role == 'Emergency Responder':
            log_manager.write_log(self.user['id'], self.room['id'], "Granted", state)
            return "Granted", f"Role: {role}"
        if state == 'NORMAL':
            if role == 'Security' or role == 'Manager':
                log_manager.write_log(self.user['id'], self.room['id'], "Granted", state)
                return "Granted", f"Role: {role}"
            allowed_time = self._is_within_time_range(role)
            if allowed_time and self._is_room_accessible(role, room_type):
                log_manager.write_log(self.user['id'], self.room['id'], "Granted", state)
                return "Granted", f"Role: {role}"

        # default set to denied
        log_manager.write_log(self.user['id'], self.room['id'], "Denied", state)
        return "Denied", f"Role: {role}"

    def _is_within_time_range(self, role):
        current_time = datetime.strptime(self.time, '%H:%M:%S').time()
        role_time_map = {
            "Staff Member": ("05:30:00", "23:59:59"),
            "Student": ("08:30:00", "22:00:00"),
            "Contract Cleaner": [("05:30:00", "10:30:00"), ("17:30:00", "22:30:00")],
        }
        time_range = role_time_map.get(role)
           # multiple time range
        if isinstance(time_range, list):
            return any(
                current_time >= datetime.strptime(start, '%H:%M:%S').time() and
                current_time <= datetime.strptime(end, '%H:%M:%S').time()
                for start, end in time_range
            )
            # single time range
        if time_range:
            start, end = time_range
            return (
                current_time >= datetime.strptime(start, '%H:%M:%S').time() and
                current_time <= datetime.strptime(end, '%H:%M:%S').time()
            )
        return False

    def _is_room_accessible(self, role, room_type):
        role_room_map = {
            "Staff Member": ["Lecture Hall", "Teaching Room", "Staff Room"],
            "Student": ["Lecture Hall", "Teaching Room"],
            "Visitor / Guest": ["Lecture Hall"],
            "Security": ["Lecture Hall", "Teaching Room", "Staff Room", "Secure Room"],
            "Emergency Responder": []
        }
        allowed_rooms = role_room_map.get(role)
        if not allowed_rooms:
            print(f"Warning: Undefined role '{role}' or no room access configured.")
            return False
        return room_type in allowed_rooms
