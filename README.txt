1. Introduction
The Room Access Control System is designed to manage access to rooms based on user roles, room types, and operating modes. This guide explains how to:
Manage users and roles.
Manage rooms and their states.
Simulate access using swipe cards.
View access logs.
 List of Required Dependencies
	
Python3
Pip
SQLite3
Python3-tk 
Python3-pytest
Pythonguitst
Xdotool


2. Main Menu Overview
When you launch the application, the Main Menu appears with the following options:
User Management: Manage users and assign roles.
Room Management: Manage rooms and their states.
Simulate Access: Test access control using swipe cards.
View Logs: View the daily log of access attempts.
Exit: Close the application.

3. User Management
3.1 Add a New User
From the Main Menu, click User Management.
In the User Management window, click Add User.
Enter the following details in the form:
Name: The user’s full name.
Role ID: The numeric ID of the user’s role (e.g., 1 for Staff Member, 2 for Student).
Card ID: A unique ID for the swipe card.
Click Add User.
A confirmation message appears if the user is successfully added.
3.2 Update an Existing User
From the User Management window, click Update User.
Enter the User ID of the user you want to update.
Provide new values for the fields you want to update (e.g., name, role ID, card ID).
Click Update User to save changes.
3.3 Delete a User
From the User Management window, click Delete User.
Enter the User ID of the user you want to delete.
Confirm the deletion by clicking Delete User.
A message appears confirming the user’s removal.
3.4 View All Users
Click View All Users in the User Management window.
A list of all users, along with their roles and card IDs, will be displayed.

4. Room Management
4.1 Add a New Room
From the Main Menu, click Room Management.
In the Room Management window, click Add Room.
Enter the following details:
Room Type: Lecture Hall, Teaching Room, Staff Room, or Secure Room.
Room State: Default state is NORMAL.
Click Add Room to save the new room.
4.2 Update Room Details
Click Update Room in the Room Management window.
Enter the Room ID and update the necessary fields (e.g., type, state).
Click Update Room to save changes.
4.3 Delete a Room
Select Delete Room in the Room Management window.
Enter the Room ID of the room to delete.
Confirm the deletion by clicking Delete Room.
4.4 Change Room State
From the Room Management window, click Change Room State.
Enter the Room ID of the room you want to modify.
Select the new state: NORMAL or EMERGENCY.
Click Change Room State to apply the changes.

5. Simulate Access
From the Main Menu, click Simulate Access.
Enter the following details:
Card ID: Swipe card ID of the user.
Room ID: ID of the room being accessed.
Click Simulate Access.
The system will:
Check the access control rules.
Display a message indicating whether access is granted or denied.
Log the access attempt with details.

6. View Logs
From the Main Menu, click View Logs.
The log file for the current date (room_access_log_{date}.txt) will be displayed.
The log contains:
Date and time of the access attempt.
User’s name and card ID.
Room ID.
Access status (Granted/Denied).
Room state at the time.


