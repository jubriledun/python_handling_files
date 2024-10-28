#!/usr/bin/env python3

import csv

# Function to read employees from CSV file
def read_employees(csv_file_location):
    employee_list = []
    # Register dialect to skip spaces in CSV
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    
    # Read the CSV file using DictReader
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    
    #iterate over the CSV file that you opened, i.e., employee_file. When you iterate over a CSV file, each iteration of the loop produces a dictionary from strings (key) to strings (value).
    #Append the dictionaries to an empty initialised list employee_list as you iterate over the CSV file.
    for data in employee_file:
        employee_list.append(dict(data))
    
    return employee_list


# Function to process employee data
#initialize a new list called department_list, iterate over employee_list, and add only the departments into the department_list.

def process_data(employee_list):
    department_list = []
    
    # Create a list of all departments
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    # Create a dictionary with department counts
    department_data = {}
    for department_name in set(department_list): #This uses the set() method, which converts iterable elements to distinct elements.
        department_data[department_name] = department_list.count(department_name)
    
    return department_data


# Function to write the department report to a file
def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ': ' + str(dictionary[k]) + '\n')
            

# File paths
employee_file = "/home/student/data/employees.csv"
report_file = "/home/student/data/report.txt"

# Main execution
employee_list = read_employees(employee_file)
department_data = process_data(employee_list)
write_report(department_data, report_file)

print(f"Report generated: {report_file}")
