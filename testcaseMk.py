import csv

with open('MK-006.csv', 'w', newline='') as f:
    fieldName = ['sdt', 'password','pass', 'npass','rpass']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'sdt': '0385228474', 'password': '123456','pass': '123456', 'npass':'12345', 'rpass':'12345'})
with open('MK-006.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['sdt']
        b = row['password']
        c=row['pass']
        d=row['npass']
        e=row['rpass']

print(a)
print(b)
print(c)
print(d)
print(e)