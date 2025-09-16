import csv

def read_employee_data():
    """Read employee data from CSV file"""
    
    # Note: File path might need to be updated
    filename = "employee_data_updated.csv"
    
    employees = []
    
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        return []
    
    return employees

def analyze_employees(employees):
    """Analyze employee data"""
    if not employees:
        return
    
    print(f"Total employees: {len(employees)}")
    
    # Calculate average salary
    total_salary = sum(float(emp['Salary']) for emp in employees)
    avg_salary = total_salary / len(employees)
    print(f"Average salary: ${avg_salary:,.2f}")
    
    # Department breakdown
    departments = {}
    for emp in employees:
        dept = emp['Department']
        if dept not in departments:
            departments[dept] = []
        departments[dept].append(emp)
    
    print("\nDepartment breakdown:")
    for dept, emps in departments.items():
        avg_dept_salary = sum(float(emp['Salary']) for emp in emps) / len(emps)
        print(f"  {dept}: {len(emps)} employees, avg salary: ${avg_dept_salary:,.2f}")

if __name__ == "__main__":
    employees = read_employee_data()
    analyze_employees(employees)