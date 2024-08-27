import sqlite3 as sql3

with sql3.connect('users.db') as connection:
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        salary INTEGER
    )''')

    cursor.execute('''INSERT INTO employees (name, salary)
        VALUES 
        ('Alice', 5000),
        ('Bob', 5500),
        ('Charlie', 6000),
        ('David', 6500),
        ('Ivy', 7000),
        ('Frank', 7500),
        ('Alex', 8000),
        ('Heidi', 8500),
        ('Marcie', 9000),
        ('Judy', 9500)
    ''')

    cursor.execute('''SELECT * FROM employees''')

    employees = cursor.fetchall()
    for employee in employees:
        print(employee)
