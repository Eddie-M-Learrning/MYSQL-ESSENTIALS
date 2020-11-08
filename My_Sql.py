##################(-THESE CODES ARE -(ESSENTIAL)- FOR LEARNING MYSQL-)###################


#### MAIN NOTE : ALWAYS 
###  CONNECT TO SERVER
##   CREATE & EXECUTE CURSOR
#    COMMIT  THE CHANGES 

# REQUIREMENTS : MYSQL COMMUNITY INSTALLER (OPEN SOURCE) & SPYDER(ANACONDA)(RECOMMENDED)

import mysql.connector#NEED TO INSTALL SEPERATELY USING PIP or CONDA


# CONNECTING TO SERVERg:

mydb = mysql.connector.connect(
    host = "localhost",#  COMMON_FOR_ALL
    user = "root",#       WILL MAY CHANGE PER MYSQL COMMUNITY INSTALLER
    password = "",#       ENTER YOUR PASSWORD,THAT SETED WHILE CREATING SERVER
    database = "testdb",# DATABASE CAN BE CREATED IN ANY NAME ENTER HERE ONLY AFTER CREATING CURSOR & DATABASE
)

# CREATING CURSOR :

mycursor = mydb.cursor()#ESSENTIAL


# CREATING DATABASE
    
'''
mycursor.execute("CREATE DATABASE testdb")#DATABASE WILL BE CREATED EVEN IF NOT EXIST
'''

# SHOW DATABASE

'''
mycursor.execute("SHOW DATABASES")

for db in mycursor:
   print(db)
   '''
    
# CREATING TABLE :
    
'''
mycursor.execute("CREATE TABLE students (name VARCHAR(255),age INTEGER(10))")

mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)
 '''
  
#INSERTING SINGLE & MANY VALUES

'''
sqlFormula = "INSERT INTO students (name,age) VALUES(%s,%s)"
student1 = [("kaja",22),
            ("aadi",22),
            ("kartick",22),
            ("magesh",22),
            ("Varatharaja",22),]

mycursor.executemany(sqlFormula,student1)
'''

# VIEWING DATA 

'''
mycursor.execute("SELECT * FROM students ")
my_result = mycursor.fetchall()
print(my_result)
'''

# WHERE

'''
sqql = "SELECT * FROM students WHERE age =22 "
mycursor.execute(sqql)
my_result = mycursor.fetchall()
print(my_result)
'''
# WILDCARDS

'''
sqql = "SELECT * FROM students WHERE name LIKE '%en%' "
mycursor.execute(sqql)
my_result = mycursor.fetchall()
print(my_result)
'''

'''  #SAFE_METHOD
sqql = "SELECT * FROM students WHERE name LIKE %s"
mycursor.execute(sqql,("murga",))
my_result = mycursor.fetchall()
print(my_result)

'''

# UPDATING DATABASE

'''
sqql = " UPDATE  students SET age = 10 WHERE  name = 'murga' "
mycursor.execute(sqql)
'''
# LIMIT & OFFSET 

'''
mycursor.execute("SELECT * FROM students LIMIT 6 OFFSET 6 ")
myresult = mycursor.fetchall()
for result in myresult:
    print(myresult)
'''

# ORDER BY

'''
mycursor.execute("SELECT * FROM students ORDER BY age DESC")
myresult = mycursor.fetchall()
print(myresult)
'''

#DELETE & DROP TABLE 
'''
sql = "DELETE FROM students WHERE name ='murga'"
mycursor.execute(sql)
'''
'''
sql = "DROP TABLE IF EXISTS students"
mycursor.execute(sql)
mydb.commit()
'''





# CREDIT : THECODEX  
# LEARNER: GUGHAN.BABU[EDDIE_M_LEARNING]