import csv

with open('Local Hedge Funds v2.csv') as csv_data:
    reader = csv.reader(csv_data)

    rows = [row for row in reader if row]
    headings = rows[0]

    hf_info = {}
    for row in rows[1:]:
        for col_header, data_column in zip(headings, row):
            hf_info.setdefault(col_header, []).append(data_column)
            
with open('local_hedge_funds_v2.txt', 'w') as f:
    print(hf_info, file=f)
