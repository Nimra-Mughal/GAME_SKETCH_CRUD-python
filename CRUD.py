# import sqlite3
# con = sqlite3.connect("sample.db")

# ============== Create Database =================
# con.execute('''
#     create table employee(
#     std_id integer primary key autoincrement,
#     std_name varchar(40),
#     std_class varchar(30),
#     std_email varchar(30)
#     )
# ''')
# con.close()

# ============== Insert records =================
# query = '''insert into student(std_name,std_class,std_email) values('Hina','12th','hina@gmail.com'),
# ('Kinza','12th','kinza@gmail.com'),
# ('Owais','12th','Owais@gmail.com'),
# ('john','12th','john@gmail.com')
# '''
# con.execute(query)
# con.commit()
# con.close()

# ============== Show Records ==============
# data = con.execute("select COUNT(*) from student")
# print(data)
# # print("id","Name","class","email")
# # for a in data:
# #     print(a[0],a[1],a[2],a[3])
# con.close()
# cursor=con.cursor()
# no=cursor.execute("select * from register")
# print(no)

# ============== Show Limited Records ==============
# data = con.execute("select * from student limit 2,4")
# print("id","Name","class","email")
# for a in data:
#     print(a[0],a[1],a[2],a[3])
# con.close()

# ============== Delete Records ==============
# std_id=input("Enter Student id")
# con.execute("delete from student where std_id="+std_id)
# con.commit()
# con.close()

# ============== Update records =================
# query = "UPDATE student SET std_class = '13th' WHERE std_id = '2'"
# con.execute(query)
# con.commit()
# con.close()

# ============== Search Records ==============
# name=input("Enter your name")
# data=con.execute("select * from student WHERE std_name like '%" + name + " %'")
# print("id","Name","class","email")
# for a in data:
#     print(a[0],a[1],a[2],a[3])
# con.close()
import pymysql

con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
mycursor = con.cursor()

# Execute the query
mycursor.execute("select COUNT(*) from register")

myresult = mycursor.fetchall()

print(myresult)

# Close database connection
con.close()






