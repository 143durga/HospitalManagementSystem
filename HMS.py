import sqlite3

# Connect to database
conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()

# Create table for patients
cursor.execute('''CREATE TABLE IF NOT EXISTS Patient
                  (patient_id INTEGER PRIMARY KEY,
                   name TEXT,
                   age INTEGER,
                   gender TEXT)''')

# Create Patient (C)
def add_patient(patient_id, name, age, gender):
    cursor.execute("INSERT INTO Patient (patient_id, name, age, gender) VALUES (?, ?, ?, ?)",
                   (patient_id, name, age, gender))
    conn.commit()

# Read Patient (R)
def get_patient(patient_id):
    cursor.execute("SELECT * FROM Patient WHERE patient_id=?", (patient_id,))
    return cursor.fetchone()

# Update Patient (U)
def update_patient(patient_id, new_name, new_age, new_gender):
    cursor.execute("UPDATE Patient SET name=?, age=?, gender=? WHERE patient_id=?",
                   (new_name, new_age, new_gender, patient_id))
    conn.commit()

# Delete Patient (D)
def delete_patient(patient_id):
    cursor.execute("DELETE FROM Patient WHERE patient_id=?", (patient_id,))
    conn.commit()

# Example Usage
add_patient(1, "Jane Doe", 30, "Female")
patient = get_patient(1)
print(patient)
update_patient(1, "Jane Smith", 31, "Female")
delete_patient(1)

conn.close()
