import csv

with inplace(csvfilename, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.reader(outfh)

    for row in reader:
        row += ['new', 'colums']
        writer.writerow(row)