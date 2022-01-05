
import csv
with open('TestCase.csv', 'w', newline='') as f:
   fieldName = ['user', 'password']
   writer = csv.DictWriter(f, fieldnames = fieldName)
   writer.writeheader()
   writer.writerow({'user': 'linhe.96.gl@gmail.com', 'password': '1234567'})
with open('TestCase.csv', newline='') as f:
   reader = csv.DictReader(f)
   for row in reader:
       u = row['user']
       p = row['password']
print(u)
print(p)
















