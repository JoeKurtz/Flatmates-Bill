# Define "class" PDFReport
# Need def "save()"
import os
import webbrowser

from fpdf import FPDF


class PDFReport:
    def __init__(self, filename):
        self.filename = filename

    # Name: generate_pdf
    # Input: flatmate1, flatmate2, bill
    # Processing: Uses FPDF class. Sets up a PDF under FDPF class.
    # ... Adds Text to Screen using "pdf.cell"
    # ... Saves PDF using "pdf.output()"
    # Output: PDF File
    def generate_pdf(self, flatmate1, flatmate2, bill):
        pdf = FPDF("P","pt","A4")
        pdf.add_page()

        # Put an Image
        pdf.image(name="Inserts/house.png",link="Inserts/house.png",w=60,h=60)

        # Add Text to PDF
        # Choose Font First
        pdf.set_font(family="Times", size=24, style="B")

        # Add Text Cell --> Texts gets Added in Cells
        # Create Header
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align = "C", ln = 1)

        # Insert Subheading for Period
        # Change Font Too
        pdf.set_font(family="Times", size=14,style="B")
        pdf.cell(w=250, h=40, txt="Period:",align="C")
        pdf.cell(w=250, h=40, txt=bill.period, ln=1,align="C")

        # Insert Body Text --> Name, Bill (Both Flatmates)
        # Change Font Too
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=250, h=40, txt=flatmate1.name,align="C")
        pdf.cell(w=250,h=40,txt=flatmate1.pays(bill,flatmate2),align="C",ln=1)
        pdf.cell(w=250, h=40, txt=flatmate2.name,align="C")
        pdf.cell(w=250, h=40, txt=flatmate2.pays(bill, flatmate1),align="C",ln=1)

        # Add Row on Bottom for Total
        pdf.set_font(family="Times",size=14,style="B")
        pdf.cell(w=250, h=40, txt="Total:", align="C")
        pdf.cell(w=250, h=40, txt="$"+str(format(bill.amount,",.2f")), align="C",ln=1)


        # Save File under "filename"
        pdf.output(f"Reports/{self.filename}")

        # Automatically Open File on Execution
        webbrowser.open("file://"+os.path.realpath(f"Reports/{self.filename}"))
