# Define "class" Flatmates
# Methods: Name. Days, def "pays()"
class Flatmate:
    def __init__(self, name,days):
        self.name = name
        self.days = days

    # Name: pays
    # Input: bill
    # Processing: Treating Days stayed by each flatmates as individual days (i.e. Not Overlapping)
    # ...         and hence giving a weight based off of days stayed out of total
    # ...         Formula would be: Weight 1 = x1 / (x1 + x2) & Weight 2 = 1 - Weight 1
    # ...         Where: x1 = Days of Flatmate One & x2 = Days of Second Flatmates
    # Output: Value Individual Flatmate Pays of Total Bill
    def pays(self, bill, flatmate2):
        weight = self.days / (self.days + flatmate2.days)
        total = bill.amount * weight
        format_total = "$" + format(total,",.2f")
        return format_total
