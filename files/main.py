# Import Classes
from Bill import Bill
from Flatmates import Flatmate
from PDF import PDFReport


print("Flatmates App")
print()

# Lets Get User to Input Data - Common-Line Interface ("CLI")
period = input("Input a Period (Month/Year) ")
print("Period:", period)
print()

flatmate1_name = input("Input Name of Flatmate 1 ")
flatmate1_days_stayed = int(input(f"Input Days Stayed by {flatmate1_name} in Apartment "))

while flatmate1_days_stayed < 0:
    print("Invalid Days")
    print()
    flatmate1_days_stayed = int(input(f"Input Days Stayed by {flatmate1_name} in Apartment "))

print()

flatmate2_name = input("Input Name of Flatmate 2 ")
flatmate2_days_stayed = int(input(f"Input Days Stayed by {flatmate2_name} in Apartment "))

while flatmate2_days_stayed < 0:
    print("Invalid Days")
    print()
    flatmate2_days_stayed = int(input(f"Input Days Stayed by {flatmate2_name} in Apartment "))

print()

total_bill = float(input("Enter Total Bill "))

while total_bill < 0:
    print("Invalid Bill")
    print()
    total_bill = float(input("Enter Total Bill "))

# Create Instances with Data

bill = Bill(total_bill, period)
flatmate1 = Flatmate(name=flatmate1_name, days=flatmate1_days_stayed)
flatmate2 = Flatmate(name=flatmate2_name, days=flatmate2_days_stayed)

# Generate PDF Report
pdf_report = PDFReport(f"{bill.period}.pdf")
pdf_report.generate_pdf(flatmate1, flatmate2, bill)
