# Flatmates-Bill
 A system that generates a PDF report of the bills owed by two flatmates
 
 ## Conception
 A program that simulates a scenario of two flatmates splitting their rent bill over a period of time <br/>
 <br/>
 The Total Bill is split in proportion to the amount of days spent in the flat by each flatmate <br/>
``` python
weight = self.days / (self.days + flatmate2.days)
total = bill.amount * weight
```
Where: "self.days" = Amount of days spent in apartment by flatmate one
<br/>
<br/>

**For Instance:** <br/>
Assume a scenario in which the flatmates were splitting the bill for the period of *December 2021* <br/>
- *Total Bill*: $10,000
- *Flatmate One Days in Apartment*: 20
- *Flatmate One Days in Apartment*: 25
<br/>

``` python
weight = 20 / (20 + 25)
total_f1 = 10,000 * 0.4444
total_f1 = 4,444.44
total_f2 = 5,555.56
```
## Execution
The code would run the following way (Excluding the Safeguards):
``` python
period = input("Input a Period (Month/Year): ")
flatmate1_name = input("Input Name of Flatmate 1: ")
flatmate1_days_stayed = int(input(f"Input Days Stayed by {flatmate1_name} in Apartment: "))
flatmate2_name = input("Input Name of Flatmate 2: ")
flatmate2_days_stayed = int(input(f"Input Days Stayed by {flatmate2_name} in Apartment: "))
total_bill = float(input("Enter Total Bill: "))
```
This would output to the user as the Follwing (With Mock Answers)
```
Input a Period (Month/Year): December 2021
Input Name of Flatmate 1: Joe
Input Days Stayed by Joe in Apartment: 20
Input Name of Flatmate 2: Stan
Input Days Stayed by Joe in Apartment: 25
Enter Total Bill: 10,000
```
<br/>
Then, we would instantiate an instance of the classes within the code as following:

```python
# Create Instances with Data
bill = Bill(total_bill, period)
flatmate1 = Flatmate(name=flatmate1_name, days=flatmate1_days_stayed)
flatmate2 = Flatmate(name=flatmate2_name, days=flatmate2_days_stayed)

# Generate PDF Report
pdf_report = PDFReport(f"{bill.period}.pdf")
pdf_report.generate_pdf(flatmate1, flatmate2, bill)
```

## PDF Report
Upon the user inputting the total bill, each flatmates' individual bill iscalculated, and a PDF report, title **"{Month Year}.pdf"** is autoamtically shown to the user, and saved to the users files under *files/Reports*
<br/>
<br/>

A sample PDF would look as follows:
<br/>
![December 2021 Report](files/Inserts/December2021.png)
