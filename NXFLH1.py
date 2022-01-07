import csv
with open('LienHe.csv','w',newline='') as f:
    fieldName = ['tieude','chitiet','ten','sdt','email']
    write = csv.DictWriter(f,fieldnames= fieldName)
    write.writeheader()
    write.writerow({'tieude':'Skincare','chitiet':'nuoc tay trang','ten':'','sdt':'12345','email':'1954052047lan@ou.edu.vn'})

with open('LienHe.csv',newline='') as f:
    reader=csv.DictReader(f)
    for row in reader:
        t = row['tieude']
        c = row['chitiet']
        n = row['ten']
        s = row['sdt']
        e = row['email']

print(t)
print(c)
print(n)
print(s)
print(e)