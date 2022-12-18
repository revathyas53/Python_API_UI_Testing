import mysql.connector
#host, database, user,password
conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='Nandhu155')
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')
'''row=cursor.fetchone()
print(row)
print(row[3])
all_row=cursor.fetchall()
print(all_row)'''
# need to sum all the price in the database customer info

rows = cursor.fetchall()
print(rows)
sum = 0
for row in rows:
    sum += row[2]

print(sum)
query = 'update CustomerInfo set Location= %s where CourseName= %s'
data = ('UK', "Jmeter")
cursor.execute(query, data)
conn.commit()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchall()
print(row)
'''select * From APIDevelop.CustomerInfo;
+------------+---------------+--------+----------+
| CourseName | PurchasedDate | Amount | Location |
+------------+---------------+--------+----------+
| selenium   | 2022-11-26    |    120 | Africa   |
| Protractor | 2022-11-26    |     45 | Africa   |
| Appium     | 2022-11-26    |     99 | Asia     |
| Jmeter     | 2022-11-26    |     76 | UK       |
| selenium   | 2022-11-27    |    120 | Africa   |
| Protractor | 2022-11-27    |     45 | Africa   |
| Appium     | 2022-11-27    |     99 | Asia     |
| Jmeter     | 2022-11-27    |     76 | UK       |
+------------+---------------+--------+----------+'''

conn.commit()
cursor.execute('select * from CustomerInfo')
row = cursor.fetchall()
#query = 'SELECT CourseNameFROM (SELECT CourseName, ROW_NUMBER() OVER (PARTITION BY CourseName ORDER BY CourseName) AS row_num FROM CustomerInfo) AS temp_table WHERE row_num>1'
conn.commit()
cursor.execute(query)
row = cursor.fetchall()
print(row)
conn.close()
