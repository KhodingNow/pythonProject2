import sqlite3


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn):
    try:
        cursor = conn.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary INTEGER NOT NULL)
            """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table created successfully: ")

    except sqlite3.Error as e:
        print(f"Error: {e}")


def insert_employee(conn, name, salary):
    try:
        cursor = conn.cursor()
        insert_query = "INSERT INTO employees (name, salary) VALUES (?, ?)"
        cursor.execute(insert_query, (name, salary))
        conn.commit()
        print("Employee data inserted successfully: ")
    except sqlite3.Error as e:
        print(f"Error: {e}")


def get_employee_by_id(conn, employee_id):
    try:
        cursor = conn.cursor()
        select_query = "SELECT name, salary FROM employees WHERE id = ?"
        cursor.execute(select_query, (employee_id,))
        row = cursor.fetchone()
        if row:
            print(f"Employee name: {row[0]}, Salary: {row[1]} ")
        else:
            print("Employee not found")

    except sqlite3.Error as e:
        print(f"Error: {e}")


def validate_input(input_str):
    if any(char in input_str for char in [" ' ", "\"", ",", "--"]):
        raise ValueError("Invalid input detected: ")


def main():
    db_file = 'example.db'
    conn = create_connection(db_file)

    create_table(conn)

    try:
        name = input("Enter employee name: ")
        salary = input("Enter employee salary: ")

        validate_input(name)
        validate_input(salary)

        insert_employee(conn, name, salary)

        emp_id = input("Input Employee ID to retrieve data: ")
        validate_input(emp_id)

        get_employee_by_id(conn, emp_id)
        conn.close()

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
