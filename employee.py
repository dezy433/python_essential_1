"""
Create a new repository for python_essential_1
 Clone this repository on your machine
 Create python project inside the repository
- The app (Employee Data Entry) should do the following:
 You should read the number of the employees from the user
-   For each employee, you should read the first name, last and age.
- You should check that the first name and last name are not empty
- You should check that the age is between 18 and 100
- print the employee information
- You should calculate the sum of ages of all employees. If the total sum is more than 500, print a message that tell us the result, otherwise just finish the app
- All printing and input should use a clear and readable syntax
- All variables should have meaningful names

"""

for index in range(3):
    first_name = input("Please Enter Your First Name ")

    last_name = input("Please Enter Your Last Name ")

    age = input("Please Enter Your Age ")

     # age = int(age_str)
    total_employee_age = (int(age) + int(age) + int(age))
    if int(age) > 17 and int(age) < 101:
        print(first_name +" " + last_name +" "+ age)
    elif total_employee_age < 501:

        print(f"The toal age of all the employees are {total_employee_age}")
    else:
            break


