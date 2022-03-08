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
employee_count = input("How many employees do you wish to add ")
employee_names= []
employee_age = []

for index in range(int(employee_count)):
    first_name =""
    last_name = ""
    age = 0
    while first_name.strip()=="":
        first_name = input("Please Enter Your First Name ")
    while last_name.strip()=="":
        last_name = input("Please Enter Your Last Name ")

    while age < 18 or age > 100:
        age = int(input("Please Enter Your Age "))

        employee_names.append(first_name +" "+ last_name)
        employee_age.append(age)


for index in range(int(employee_count)):
    print (employee_names[index] +" " + str(employee_age[index]))

if sum(employee_age) > 500:
    print("Add of all employee ages " + str(sum(employee_age)))



