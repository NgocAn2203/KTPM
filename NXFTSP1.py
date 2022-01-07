import csv
with open('ThongTin.csv','w',newline='') as f:
    fieldName = ['hoten','sdtemail']
    write = csv.DictWriter(f,fieldnames= fieldName)
    write.writeheader()
    write.writerow({'hoten':'Tran Lan','sdtemail':'1954052047lan@ou.edu.vn'})

with open('ThongTin.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        t = row['hoten']
        e = row['sdtemail']

print(t)
print(e)