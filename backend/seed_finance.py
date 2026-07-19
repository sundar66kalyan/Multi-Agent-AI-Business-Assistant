import sqlite3

conn = sqlite3.connect("business_assistant.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM finance")
count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO finance
    (month, revenue, expenses, profit)
    VALUES
    ('January', 250000, 170000, 80000)
    """)
    conn.commit()
    print("Finance data inserted.")
else:
    print("Finance table already contains data.")

conn.close()