'''luu mat khau vao file csv
user, password'''

import csv

with open('DangNhap.csv', 'w', newline='') as f:
    fieldName = ['sdt', 'password']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'sdt': '0334545889', 'password': '0123456789'})
with open('DangNhap.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        u = row['sdt']
        p = row['password']
print(u)
print(p)
