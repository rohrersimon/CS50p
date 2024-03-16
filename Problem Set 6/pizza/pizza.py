import sys
from os import path
import csv
from tabulate import tabulate


# Handle command-line arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

csvname = sys.argv[1]

if not path.exists(csvname):
    sys.exit("File does not exist")
elif not csvname.endswith('.csv'):
    sys.exit("Not a csv file")

# Open CSV file
with open(csvname, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Print ACSII table
print(tabulate(data, headers="firstrow", tablefmt="grid"))
