"# HospitalManagementSystem" 
Hospital Management System Database 🏥
This project contains the database schema for a Hospital Management System, which stores and organizes patient records, doctor information, appointments, and other related data. The database is designed to support the efficient management of hospital operations.

🌟 Features
Patient Table: Stores information about patients, including personal details and medical history.
Doctor Table: Contains details about doctors, including specialties and availability.
Appointment Table: Tracks patient appointments with doctors.
Medical Records Table: Stores patient medical records, including diagnoses and treatment plans.
SQL Queries: Provides predefined SQL queries for managing the system's operations.
📂 Repository Structure
graphql
Copy code
Hospital-Management-System-Database/
├── README.md             # Project documentation
├── HospitalManagementSystem.mwb  # MySQL Workbench file containing the database schema

Here’s the updated README.md with the SQL queries included in the project:

Hospital Management System Database 🏥
This project contains the database schema for a Hospital Management System, which stores and organizes patient records, doctor information, appointments, and other related data. The database is designed to support the efficient management of hospital operations.

🌟 Features
Patient Table: Stores information about patients, including personal details and medical history.
Doctor Table: Contains details about doctors, including specialties and availability.
Appointment Table: Tracks patient appointments with doctors.
Medical Records Table: Stores patient medical records, including diagnoses and treatment plans.
SQL Queries: Provides predefined SQL queries for managing the system's operations.
📂 Repository Structure
graphql
Copy code
Hospital-Management-System-Database/
├── README.md             # Project documentation
├── HospitalManagementSystem.mwb  # MySQL Workbench file containing the database schema
├── queries.sql           # SQL file with sample queries for the system
🛠️ Technologies Used
MySQL: Relational database management system used for storing and querying data.
SQL: Structured Query Language for database management and querying.
MySQL Workbench: Tool used to design the database schema (HospitalManagementSystem.mwb).
🔧 Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/143durga/Hospital-Management-System-Database.git
cd Hospital-Management-System-Database
Create the Database: Open the HospitalManagementSystem.mwb file in MySQL Workbench or a compatible database management tool.
Generate the SQL code to create the necessary tables and relationships.

Import Queries: Use queries.sql to execute various SQL commands to interact with the database. Here are some sample queries:

Create Tables:

sql
Copy code
CREATE TABLE Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    specialty VARCHAR(100),
    contact_number VARCHAR(15)
);

CREATE TABLE Patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    dob DATE,
    contact_number VARCHAR(15),
    address TEXT
);

CREATE TABLE Appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);

CREATE TABLE Medical_Records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    diagnosis TEXT,
    treatment TEXT,
    date_of_record DATE,
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);
Insert Sample Data:

sql
Copy code
INSERT INTO Doctors (first_name, last_name, specialty, contact_number) 
VALUES ('John', 'Doe', 'Cardiologist', '1234567890'),
       ('Jane', 'Smith', 'Neurologist', '0987654321');

INSERT INTO Patients (first_name, last_name, dob, contact_number, address) 
VALUES ('Mark', 'Taylor', '1990-05-15', '1230984567', '123 Main St, City'),
       ('Sarah', 'Johnson', '1985-11-22', '7896541230', '456 Oak St, Town');

INSERT INTO Appointments (patient_id, doctor_id, appointment_date, status) 
VALUES (1, 1, '2024-12-15', 'Scheduled'),
       (2, 2, '2024-12-16', 'Scheduled');
Query Data:

sql
Copy code
-- Retrieve all appointments for a patient
SELECT * FROM Appointments WHERE patient_id = 1;

-- Retrieve medical records for a patient
SELECT * FROM Medical_Records WHERE patient_id = 1;
Run SQL Queries: You can run the queries.sql file to execute all predefined queries in your SQL environment:

bash
Copy code
mysql -u username -p database_name < queries.sql
🌟 Future Enhancements
Database Security: Add user authentication and permissions to protect sensitive data.
Integration with Frontend: Develop a web interface to interact with the database and manage the system.
Performance Optimization: Implement indexing and query optimization for large datasets.

-- Updated Features
Key Features of the System
Patient Management:

Allows patient registration with personal details such as name, email, address, contact number, age, and gender.
Provides patients with the ability to view their medical history and appointment details.
Doctor Management:

Manages doctor registration with email, name, password, and gender.
Allows doctors to manage their schedules and view patient records.
Appointment Scheduling:

Patients can book appointments with doctors based on availability.
Doctors' schedules are managed, and appointments are tracked with status updates.
Medical History Management:

Keeps a record of a patient's medical history, surgeries, medications, and diagnoses.
Medical history is linked to the patient's profile.
Billing:

Generates billing records based on treatments provided, including total amount and payment status.
Tracks billing status with options like "Paid," "Pending," or "Overdue."
Event-based Automation:

Automated events for archiving old appointments, reducing database size.
Ensures regular updates and archival of old data to maintain system performance.
Triggers and Stored Procedures:

Uses triggers to update appointment status when diagnosis is added.
Stored procedures are created for adding new appointments efficiently.
Database Design
The database design for this system includes the following key tables:

Patient Table:

Stores details like name, email, patient ID, contact details, and medical history.
Primary key: patient_id
Doctor Table:

Stores details about doctors such as email, name, gender, and schedules.
Primary key: doctor_id
Appointment Table:

Tracks appointments for patients with doctors, including status and timings.
Primary key: id
MedicalHistory Table:

Contains the medical history records for each patient.
Primary key: id
Billing Table:

Manages patient bills, payment status, and amounts.
Primary key: bill_id
Stored Procedures & Triggers:

AddNewAppointment procedure to add appointments for patients.
UpdateAppointmentStatus trigger to update the appointment status when a diagnosis is made.
Event ArchiveOldAppointments for archiving old appointments.
Automation
Archiving Old Appointments: An event was created to automatically archive old appointments after one year to keep the database clean and efficient.

Update Appointment Status: A trigger was created to update the status of appointments to 'Completed' once the diagnosis is made.

Technical Stack
Database: MySQL (for database management and relational data storage)
Procedures & Triggers: MySQL stored procedures and triggers to automate key tasks.
Backend Logic: SQL queries to manage and automate tasks like data updates, archiving, and billing.
Challenges and Solutions
Complex Foreign Key Relationships:

Multiple foreign key constraints were needed between patient, medical history, and doctor tables. Managing these relationships required precise indexing and constraint management.
Solution: Ensured that all foreign key columns were indexed properly to avoid performance issues.
Event Scheduling:

Managing the automation of database cleanup and archiving of old appointments was a challenge.
Solution: MySQL Events were used to schedule daily archiving operations.
Data Integrity:

Ensuring data consistency across various tables like billing, appointments, and patient data.
Solution: Used triggers to enforce consistency (e.g., when a diagnosis is added, the appointment status automatically changes).
