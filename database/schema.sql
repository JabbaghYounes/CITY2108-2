-- Create Roles table
CREATE TABLE IF NOT EXISTS Roles (
    roleID INTEGER PRIMARY KEY AUTOINCREMENT,
    roleName TEXT UNIQUE NOT NULL,
    accessTimes TEXT NOT NULL
);

-- Create Users table
CREATE TABLE IF NOT EXISTS Users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    roleID INTEGER NOT NULL,
    cardID TEXT UNIQUE NOT NULL,
    FOREIGN KEY (roleID) REFERENCES Roles(roleID)
);

-- Create Rooms table
CREATE TABLE IF NOT EXISTS Rooms (
    roomID INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    state TEXT NOT NULL DEFAULT 'NORMAL'
);

-- Create Logs table
CREATE TABLE IF NOT EXISTS Logs (
    logID INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    time TEXT NOT NULL,
    userID INTEGER NOT NULL,
    roomID INTEGER NOT NULL,
    accessStatus TEXT NOT NULL,
    roomState TEXT NOT NULL,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (roomID) REFERENCES Rooms(roomID)
);
