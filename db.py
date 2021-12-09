import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'test',
    user = 'root',
    password = ''
)

mycursor =mydb.cursor(dictionary=True)


mycursor.execute(""" CREATE TABLE IF NOT EXISTS login(
    ID INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL ,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL,
    PRIMARY KEY(ID)
    )"""
)


mycursor.execute(""" CREATE TABLE IF NOT EXISTS login2(
    ID INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL ,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL,
    year int not null,
    PRIMARY KEY(ID)
    )"""
)



mycursor.execute(""" CREATE TABLE IF NOT EXISTS mycourse(
    teachername varchar(200) not null,
    coursename varchar(200) not null,
    coursecode varchar(200) not null,
    time varchar(200) not null,
    year int not null
    )"""
)




'''
mycursor.execute(""" CREATE TABLE IF NOT EXISTS lecturers2(
    courses varchar(200) not null,
    name varchar(200) not null
    )"""
)
'''

'''
mycursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(
    course  varchar(200) not null,
    name varchar(200) not null,
)"""
)

'''
# mycursor.execute(""" CREATE TABLE IF NOT EXISTS COURSE(
#     NAME VARCHAR(250),
#     GRADE INT,
#     DESCRIPTION VARCHAR(500)
# )""")
# mycursor.execute(""" CREATE TABLE IF NOT EXISTS CLASSROOM(
#     YEAR INT,
#     TEACHER VARCHAR(250),
#     GRADE INT

# )""")
# mycursor.execute(""" CREATE TABLE IF NOT EXISTS EXAM(
    
#     COURSE VARCHAR(250),
#     START_DATE DATE,
#     END_DATE DATE

# )""")
# mycursor.execute(""" CREATE TABLE IF NOT EXISTS EXAM_RESULT(
#     STUDENT VARCHAR(250),
#     YEAR INT,
#     COURSE VARCHAR(250),
#     GRADE INT

# )""")








