""""
Employee Management System



The objective of this exercise is to practice working with: functions, while/for loops, dictionary, list and input validation.



Requirements



1- A company needs a system to manage the data of its employee.



2- Each employee has the following information:



- Employee ID (int)
- First name (string: minimum 2 Characters)
- Last Name (string: minimum 2 Characters)
- Birth Year (int between 1900 and 2004)
- Birth Month (int between 1 and 12)
- Birth Day (int between 1 and 31)
- Position (string)
- Whether graduated from the university or not (boolean)



3- The system's user should be able to perform any of the following tasks:



- Add an Employee
- Remove an Employee
- Get the total number of Employees
- Get a List of Employees
- Retrieve the data of an employee (By ID)
- Update employee's data
- Exit


4- The app should run in a loop that shows a list of options to the user
"""""


def id_func():
    while True:
        id_str = input("Employee ID")
        if id_str.isdigit():
            id_int = int(id_str)
            return id_int
        else:
            print("Add numbers")


def first_name_func():
    while True:
        name = input("name")
        if len(name.strip()) > 2:
            return name


def last_name_func():
    while True:
        l_name = input("last name")
        if len(l_name.strip()) > 2:
            return l_name


def birth_year_func():
    while True:
        birth_year_str = (input("birth year"))
        if birth_year_str.isdigit():
            birth_year = int(birth_year_str)
        if (birth_year >= 1900) and (birth_year <= 2004):
            return birth_year
        else:
            print("Years ranging from 1990-2004")


def birth_month_func():
    while True:
        birth_month_str = (input("birth month"))
        if birth_month_str.isdigit():
            birth_month = int(birth_month_str)
            if (birth_month >= 1) and (birth_month <= 12):
                return birth_month
            print("Please enter as a number")


def bday_func():
    while True:
        bday_str = input("birth Day")
        if bday_str.isdigit():
            bday = int(bday_str)
        if (bday >= 1) and (bday <= 31):
            return bday
        else:
            print("Please enter as a number")


def position_func():
    while True:
        position_str = input("Position")
        if len(position_str.strip()) > 0:
            position = str(position_str)
            return position
        else:
            print("Please enter your position")


def graduate_func():
    answers = ["yes", "no", "Yes", "No"]
    while True:
        graduate_str = input("Have you attended univerisity ? ")
        if graduate_str in answers:
            return graduate_str
        else:
            print("Please answer 'Yes' or 'No'")


def add_employee():
    ids = id_func()
    first_name = first_name_func()
    last_name = last_name_func()
    bday = bday_func()
    birth_month = birth_month_func()
    birth_year = birth_year_func()
    pos = position_func()
    grad = graduate_func()

    employee = {
        "ID": ids,
        "First name": first_name,
        "Last name": last_name,
        "Birth Year": birth_year,
        "Birth Month": birth_month,
        "Birth Day": bday,
        "Position": pos,
        "Univeristy": grad,
    }
    while True:
        employees.append(employee)
        return employee


if __name__ == '__main__':
    import employee_data

    print("Select operation.")
    print("1.Add an Employee")
    print("2.Remove employee")
    print("3.Get a list of employees")
    print("4.Retreive employee (By ID)")
    print("5.Update employee data")
    print("6.Quit")

    employees = []
    while True:
        choice = input("Enter choice(1/2/3/4/5/6):")
        if choice == '1':
            add_employee()
            print(employees)
#elif