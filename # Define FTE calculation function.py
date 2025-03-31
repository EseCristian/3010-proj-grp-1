# Define FTE calculation function
def calculate_fte(ch, enrollment, divisor):
    return (ch * enrollment) / divisor

# Example inputs
csci_graduate = {'CH': 3, 'enrollment': 25, 'divisor': 186.23}
csci_undergraduate = {'CH': 4, 'enrollment': 60, 'divisor': 406.24}
seng_graduate = {'CH': 3, 'enrollment': 20, 'divisor': 90.17}
seng_undergraduate = {'CH': 4, 'enrollment': 50, 'divisor': 232.25}
dasc = {'CH': 3, 'enrollment': 30, 'divisor': 186.23}

# Calculate FTEs
fte_csci_grad = calculate_fte(csci_graduate['CH'], csci_graduate['enrollment'], csci_graduate['divisor'])
fte_csci_undergrad = calculate_fte(csci_undergraduate['CH'], csci_undergraduate['enrollment'], csci_undergraduate['divisor'])
fte_seng_grad = calculate_fte(seng_graduate['CH'], seng_graduate['enrollment'], seng_graduate['divisor'])
fte_seng_undergrad = calculate_fte(seng_undergraduate['CH'], seng_undergraduate['enrollment'], seng_undergraduate['divisor'])
fte_dasc = calculate_fte(dasc['CH'], dasc['enrollment'], dasc['divisor'])

# Print results
print("FTE for CSCI Graduate: {:.2f}".format(fte_csci_grad))
print("FTE for CSCI Undergraduate: {:.2f}".format(fte_csci_undergrad))
print("FTE for SENG Graduate: {:.2f}".format(fte_seng_grad))
print("FTE for SENG Undergraduate: {:.2f}".format(fte_seng_undergrad))
print("FTE for DASC: {:.2f}".format(fte_dasc))