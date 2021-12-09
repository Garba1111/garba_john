from flask import Flask, app, render_template,request,redirect,session,url_for

from db import mydb,mycursor


app = Flask(__name__)



@app.route('/')
def first():
    mycursor.execute(f'SELECT * FROM login')
    student = mycursor.fetchall()
    return render_template('base.html', student = student)


@app.route('/gotostudent', methods = ['GET','POST'])
def sent():
    return render_template('form.html')





@app.route('/signupstudent', methods = ['GET','POST'])
def signupstudent():
    if request.method == 'POST':
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _email = request.form['email']
        _password = request.form['password']
        _year = request.form['year']
        sql = f'INSERT INTO login2(first_name,last_name,email,password, year) VALUE (%s,%s,%s,%s,%s)'
        val = (_first_name, _last_name,_email,_password,_year)
        mycursor.execute(sql,val)
        mydb.commit()
        return render_template('form.html')


@app.route('/gotostudentlogin', methods = ['GET','POST'])
def gotostudentlogin():
    return render_template('login.html')



@app.route('/login', methods= ['GET','POST'])
def login():
    if request.method=='POST':
        _first_name = request.form['first_name']
        _password = request.form['password']     
        mycursor.execute (f'SELECT * FROM login2 WHERE first_name = "{_first_name}" AND password = "{_password}"')
        verify=mycursor.fetchone()

        mycursor.execute (f'SELECT * FROM mycourse')
        courses = mycursor.fetchall()
        if verify:
            return render_template('check.html', verify=verify, courses = courses)
        else:
            msg='Invalid username/password !!!!!'
            return render_template('login.html' , msg=msg)





@app.route('/gototeacherlogin', methods = ['GET','POST'])
def gototeacherlogin():
    return render_template('tlogin.html')




@app.route('/gototeacher', methods = ['GET','POST'])
def gototeacher():
    return render_template('tform.html')



@app.route('/signupteacher', methods = ['GET','POST'])
def signupteacher():
    if request.method == 'POST':
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _email = request.form['email']
        _password = request.form['password']
        sql = f'INSERT INTO login2(first_name,last_name,email,password, year) VALUE (%s,%s,%s,%s,%s)'
        val = (_first_name, _last_name,_email,_password,3)
        mycursor.execute(sql,val)
        mydb.commit()
        return render_template('tform.html')





@app.route('/loginteacher', methods= ['GET','POST'])
def loginteacher():
    if request.method=='POST':
        _first_name = request.form['first_name']
        _password = request.form['password']     
        mycursor.execute (f'SELECT * FROM login2 WHERE first_name = "{_first_name}" AND password = "{_password}"')
        verify=mycursor.fetchone()
        mycursor.execute (f'SELECT * FROM login2')
        teachers= mycursor.fetchall()
        if verify:
            return render_template('tcheck.html', verify=verify, teachers = teachers)
        else:
            msg='Invalid username/password !!!!!'
            return render_template('tlogin.html' , msg=msg)






@app.route('/gotocourse', methods = ['GET','POST'])
def gotocourse():
    teachername = request.form['teacher_name']
    return render_template('course.html', teacher = teachername)



@app.route('/uploadcourse', methods = ['GET','POST'])
def uploadcourse():
    if request.method == 'POST':
        teachername = request.form['teacher_name']
        coursename = request.form['course_name']
        coursecode = request.form['course_code']
        time = request.form['time_of_day']
        year = request.form['year']
        sql = f'INSERT INTO mycourse(teachername,coursename,coursecode,time,year) VALUE (%s,%s,%s,%s,%s)'
        val = (teachername,coursename,coursecode,time,year)
        mycursor.execute(sql,val)
        mydb.commit()
        return render_template('course.html')







'''
  if request.method == 'POST':
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _email = request.form['email']
        _password = request.form['password']
        mycursor.execute(f'INSERT INTO login(first_name,last_name,email,password) VALUES("{_first_name}","{_last_name}", "{_email}","{_password}")')
        mydb.commit()
        return redirect('/sent')

'''



@app.route('/teachers', methods = ['GET','POST'])
def teachers():
    if request.method == 'POST':
        _first_name = request.form['first_name']
        _last_name = request.form['last_name']
        _email = request.form['email']
        _password = request.form['password']
        mycursor.execute(f'INSERT INTO login(first_name,last_name,email,password) VALUES("{_first_name}","{_last_name}", "{_email}","{_password}")')
        mydb.commit()
        return redirect('/teachers')
   # return render_template('tform.html')






@app.route('/gotologin', methods= ['GET','POST'])
def gotologin():
    return render_template('tlogin.html')









'''
@app.route('/getmyinfo', methods= ['GET','POST'])
def getmyinfo():
    if request.method=='POST':
        name = request.form['first_name']   
        mycursor.execute (f'SELECT * FROM login WHERE first_name = {name}')
        details=mycursor.fetchall()
        mycursor.execute (f'SELECT * FROM teachers')
        teachers=mycursor.fetchall()
        return render_template('tlogin.html' , details=details, teachers = teachers)
'''

# @app.route('lprofile', methods = ['GET','POST'])
# def lprofile():
    


    

if __name__ =='__main__':
    app.run(debug = True)