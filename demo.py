import MySQLdb

db = MySQLdb.connect(host="localhost",user="root",passwd="root",db="nikesh")
cursor = db.cursor()

# create database
cursor.execute('SET sql_notes=0;')
cursor.execute("create database IF NOT EXISTS Employee")

# create table
cursor.execute('SET sql_notes=0;')
cursor.execute("create table IF NOT EXISTS employee_data(ename VARCHAR(20),eemail VARCHAR(30),company VARCHAR(20),enumber NUMERIC)")

#insert data
cursor.execute("insert into employee_data VALUES ('sandeep','san@gmail.com','google',9784563210)")

# update data
cursor.execute("update employee_data set ename='sandeep1' where ename='sandeep'")

# select data
cursor.execute("select * from employee_data")
result = cursor.fetchall()
for i in result:
    print i

# delete data
cursor.execute("delete from employee_data where ename='sweety'")

db.commit()
db.close()
