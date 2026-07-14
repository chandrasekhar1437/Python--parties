import oracledb

# step1
con=oracledb.connect(user="system",password="1234",dsn="localhost/xe")
#step2
cus=con.cursor()
#step3
q="create table student01(rno varchar(20),sname varchar(100),marks=int)"
cus.execute(q)









# step5
con.close()