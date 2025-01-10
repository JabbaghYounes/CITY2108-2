-- insert test roles
INSERT INTO Roles (roleName, accessTimes)
VALUES 
('Staff Member', '{"start": "05:30:00", "end": "23:59:59"}'),
('Student', '{"start": "08:30:00", "end": "22:00:00"}'),
('Visitor', '{"start": "08:30:00", "end": "22:00:00"}'),
('Contract Cleaner', '{"morning": {"start": "05:30:00", "end": "10:30:00"}, "evening": {"start": "17:30:00", "end": "22:30:00"}}'),
('Manager', '{"start": "00:00:00", "end": "23:59:59"}'),
('Security', '{"start": "00:00:00", "end": "23:59:59"}'),
('Emergency Responder', 'N/A');

-- insert test users
INSERT INTO Users (name, roleID, cardID)
VALUES
('Alice Johnson', 1, 'STAFF001'),
('Bob Smith', 2, 'STUDENT001'),
('Charlie Visitor', 3, 'VISITOR001'),
('Dana Cleaner', 4, 'CLEANER001'),
('Eve Manager', 5, 'MANAGER001'),
('Frank Security', 6, 'SECURITY001'),
('Grace Responder', 7, 'RESPONDER001');

-- insert test rooms
INSERT INTO Rooms (type, state)
VALUES
('Lecture Hall', 'NORMAL'),
('Teaching Room', 'NORMAL'),
('Staff Room', 'NORMAL'),
('Secure Room', 'NORMAL');
