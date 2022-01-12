import csv
with open('TestcaseDK.csv', 'w', newline='') as f:
   fieldName = ['email', 'password','fullname']
   writer = csv.DictWriter(f, fieldnames = fieldName)
   writer.writeheader()
   writer.writerow({'email': '1954052007@ou.edu.vn', 'password': '1234567','fullname': 'Ngoc An'})
with open('TestCaseDK.csv', newline='') as f:
   reader = csv.DictReader(f)
   for row in reader:
       e = row['email']
       p = row['password']
       f = row['fullname']


print(e)
print(p)
print(f)
