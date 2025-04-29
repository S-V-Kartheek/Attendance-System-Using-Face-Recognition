AI-Based Attendance System with Real-Time Face Recognition

An AI-powered, real-time Face Recognition Attendance System built using Flask, OpenCV, and face_recognition.
It automates attendance tracking with live webcam streaming, secure OTP-based teacher login, email notifications for absentees, time slot management, and Excel export of attendance records.

🚀 Features
🎥 Real-time face detection and recognition via webcam.

🔐 Secure OTP-based login for teachers.

📅 Time slot selection for attendance recording.

🧠 Liveness detection (to avoid spoofing).

📧 Automated email alerts for absent students.

📊 Dashboard to view, download, and manage attendance.

🗂️ Attendance stored in SQLite and exportable as styled Excel sheets.

🔄 Duplicate attendance prevention within the same session.

📈 Tracking student entry and stay duration (optional extension).

🛠️ Tech Stack
Backend: Flask, Flask-Mail, Flask-Session

Frontend: HTML, CSS, JavaScript (Jinja templates)

Database: SQLite3, SQLAlchemy

Face Recognition: OpenCV, face_recognition

Email Service: Flask-Mail (SMTP)

Excel Export: Pandas, OpenPyXL

Authentication: OTP-based secure login system

📂 Project Structure
pgsql
Copy
Edit
/Ai-Attendance-System  
 ├── backend  
 ├── database  
 ├── frontend  
 │    ├── static  
 │    │    ├── css  
 │    │    ├── js  
 │    │    └── img  
 │    └── templates  
 │         ├── index.html  
 │         ├── register.html  
 │         └── attendance.html  
 ├── models  
 ├── services  
 ├── app.py  
 ├── requirements.txt  
 ├── README.md  
 ├── .gitignore  
 └── venv  
📸 How It Works
Teacher Login:
Teachers log in securely using OTP verification to prevent unauthorized access.

Face Recognition:
System captures live video from the webcam, detects faces, and matches them with stored known faces.

Attendance Marking:
Recognized students are automatically marked present for the selected time slot. Duplicate entries are prevented.

Absent Notification:
Students not detected are emailed an absentee notification after the session.

Data Storage & Export:
Attendance data is saved into a database and can be exported as an Excel file for reports.

🧑‍💻 Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Ai-Attendance-System.git
cd Ai-Attendance-System
Create a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure Email Settings
Set up your email credentials inside backend/services/email_service.py.

Run the application

bash
Copy
Edit
python app.py
Access the app
Open http://localhost:5000 in your browser.

✅ Future Enhancements
📱 Mobile App Integration

🌐 Cloud-based Face Storage

🔒 Advanced Liveness Detection (Blink detection, 3D face map)

📢 Voice Confirmation for Students

📅 Google Calendar Integration for Class Scheduling

🤝 Contribution
Contributions, issues, and feature requests are welcome!
Feel free to open an issue or submit a pull request.

