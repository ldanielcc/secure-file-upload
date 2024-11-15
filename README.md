# Secure File Upload Application with Flask

A secure file upload web application built using Flask. This project showcases best practices in security, including encrypted password storage, safe file handling, and session management. It highlights core cybersecurity skills, particularly in web security and secure software development.

## Features
- User Authentication with Bcrypt Encryption: Hashes and salts all user passwords for maximum security.
- Session Management: Protects user sessions with secure cookies.
- File Upload Sanitization: Only allows secure, validated file types to prevent vulnerabilities.
- Authentication and Role-Based Access Control: Enforces user roles to control access.

## Cybersecurity Approach
This application implements the following cybersecurity best practices:
- Password Security: All passwords are securely hashed using bcrypt to ensure they are stored safely.
- Session Protection: Uses a secure secret key to protect session cookies.
- File Handling Security: Validates and sanitizes all uploaded files with Werkzeug to prevent directory traversal attacks.
- Role-Based Access Control (RBAC): Controls which users have access to certain features, helping minimize the risk of unauthorized actions.

## Technologies Used
- Python (Flask)
- Flask-Login for Authentication
- Bcrypt for Password Hashing
- Werkzeug for Secure File Handling
- HTML/CSS for Frontend 

## How to Run This Project
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies: pip install -r requirements.txt
4. Run the application: python app.py


Sources:
https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/File_Upload_Cheat_Sheet.md
