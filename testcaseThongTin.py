'''luu mat khau vao file csv
user, password'''

import csv

with open('TT-003.csv', 'w', newline='') as f:
    fieldName = ['sdt', 'password','Name','Phone']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'sdt': '0385228474', 'password': '123456','Phone':'0987564234'})
with open('TT-003.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['sdt']
        b = row['password']
        c=row['Name']
        d=row['Phone']


print(a)
print(b)
print(c)
print(d)
