import csv
import sys
from os import path


# Handle command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

csvname = sys.argv[1]

if not path.exists(csvname):
    sys.exit("File does not exist")
elif not csvname.endswith('.csv'):
    sys.exit("Not a csv file")


# Open CSV file
with open(csvname) as file:
    reader = csv.DictReader(file)

    # Initiate output file
    with open(sys.argv[2], "w") as output:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()

        # Write CSV file
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})
