import sqlite3
from employee import Employee


connection = sqlite3.connect(':memory:')

db_cursor = connection.cursor()

db_cursor.execute("""CREATE TABLE employees (
                     first text,
                     last text,
                     pay integer
                     )""")

def insert_emp(emp):
    with connection:
        db_cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                      {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    db_cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return db_cursor.fetchall()

def update_pay(emp, pay):
    with connection:
        db_cursor.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with connection:
        db_cursor.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
# remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)

db_cursor.execute("SELECT COUNT(*) FROM employees")
result = db_cursor.fetchone()
print(result)

if result:
        file_counter = result[0]
        print(file_counter)


connection.close()