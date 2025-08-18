import csv
import glob

# Output file
with open('Data_processing.csv', mode='w', newline='') as outfile:
    writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    #  header
    writer.writerow(['Sales', 'Date', 'Region'])

    for filename in glob.glob("data/*.csv"):
        with open(filename, mode='r') as infile:
            reader = csv.DictReader(infile)

            for row in reader:
                
                if row["product"].lower() == "pink morsel":
                    sales = int(row["quantity"]) * float(row["price"].replace("$", ""))
                    writer.writerow([sales, row["date"], row["region"]])

