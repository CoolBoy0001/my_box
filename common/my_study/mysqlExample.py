#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql as mysql

########################################################################
#创建数据库使用 "CREATE DATABASE" 语句，以下创建一个名为 runoob_db 的数据库：
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE runoob_db")


################################################
##输出所有数据库列表：

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


##############################################################
##创建数据表
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")


############################################
###主键设置
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
mycursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

###########################################################
######插入数据
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()    # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")

########################################################
##批量插入使用 executemany() 方法，该方法的第二个参数是一个元组列表，包含了我们要插入的数据：
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
  ('Google', 'https://www.google.com'),
  ('Github', 'https://www.github.com'),
  ('Taobao', 'https://www.taobao.com'),
  ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)

mydb.commit()    # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")



########################################
#####查询
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"
sql = "SELECT * FROM sites"
sql = "SELECT * FROM sites WHERE url LIKE '%baidu%'"
#####
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB", )
#####sorted
sql = "SELECT * FROM sites ORDER BY name"
sql = "SELECT * FROM sites ORDER BY name DESC"
sql = "SELECT * FROM sites LIMIT 3"
####从第二条开始读取前 3 条记录：
sql = "SELECT * FROM sites LIMIT 3 OFFSET 1"# 0 为 第一条，1 为第二条，以此类推


mycursor.execute(sql, na)
myresult = mycursor.fetchall()     # fetchall() 获取所有记录
for x in myresult:
  print(x)


####################################
#删除记录使用 "DELETE FROM" 语句：
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

sql = "DELETE FROM sites WHERE name = 'stackoverflow'"
sql = "DELETE FROM sites WHERE name = %s"
na = ("stackoverflow", )

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")


##########################
######update
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Zhihu'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")


####################删除表
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456",
  database="runoob_db"
)
mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)
