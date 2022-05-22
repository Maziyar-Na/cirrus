import sys
import csv

rows = []
with open("train_lr.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print("header: ", header)
    for row in csvreader:
        rows.append(row)
print("[dbg] rows: ", rows[1])
data = []
for row in rows:
    label = row[1]
    numerical_features = row[2:15]
    # print("[dbg] numerical_features",numerical_features)
    numerical_features.append(label)
    data.append(numerical_features)

print("[dbg] data: ", data[1])
#filename = 'lr_example_criteo.csv'
#with open(filename, 'w', newline="") as file:
#    csvwriter = csv.writer(file) # 2. create a csvwriter object
#    csvwriter.writerow(header) # 4. write the header
#    csvwriter.writerows(data) # 5. write the rest of the data
filename = 'lr_example_criteo.svm'
with open(filename, 'w', newline="") as file:
    for d in data:
        label = d[-1]
        pairs = ['%i:%s'%(i,d[i] if d[i] != '' else 0.0) for i in range(len(d))]
        sep_line = [label]
        sep_line.extend(pairs)
        sep_line.append('\n')
        line = ' '.join(sep_line)
        file.write(line)
