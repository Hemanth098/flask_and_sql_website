import string

from flask import render_template, url_for, flash, redirect,session
from Event_Runner import app
from Event_Runner.forms import RegistrationForm, LoginForm ,MarriageForm,AdminForm
import sqlite3
detail=[]
def print_details(date):
    selected_columns = "username,number,email,Event,anything,Choose,date"
    with sqlite3.connect("C:/Users/hp/Desktop/Project/NewTry/post.db") as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT {selected_columns} FROM post where date='{date}'")
        rows = cursor.fetchall()
        xa=[]
        y=[]
        z=[]
        a=[]
        b=[]
        c=[]
        d=[]
        for row in rows:
            xa.append(row[0])
            y.append(row[1])
            z.append(row[2])
            a.append(row[3])
            b.append(row[4])
            c.append(row[5])
            d.append(row[6])
        post = []
        for i in range(0, len(xa)):
            ab = {
                'username': xa[i],
                'phone': y[i],
                'email': z[i],
                'Event': a[i],
                'anything': b[i],
                'Time': c[i],
                'Date': d[i],
            }
            post.append(ab)
    conn.close()
    return (post)
def search_user(email,password):
    local= "C:/Users/hp/Desktop/Project/NewTry/use.db"
    connection = sqlite3.connect(local)
    db_cursor = connection.cursor()

    sql = "SELECT * FROM employee WHERE email=? AND password=?"
    db_cursor.execute(sql, (email,password,))
    result = db_cursor.fetchall()
    connection.commit()
    connection.close()

    if len(result) > 0:
        return True
    else:
        return False
def search_username(email,password):
    local= "C:/Users/hp/Desktop/Project/NewTry/use.db"
    connection = sqlite3.connect(local)
    db_cursor = connection.cursor()

    sql = "SELECT username FROM employee WHERE email=? AND password=?"
    db_cursor.execute(sql, (email,password,))
    result = db_cursor.fetchone()
    connection.commit()
    connection.close()
    return result[0]

def _add_data(username,email,password):
    local= "C:/Users/hp/Desktop/Project/NewTry/use.db"
    connection = sqlite3.connect(local)
    db_cursor = connection.cursor()

    # Insert into database
    sql = """INSERT INTO employee(UserName,email,password)
             VALUES(?,?,?)"""
    db_cursor.execute(sql,(username,email,password))
    connection.commit()
    connection.close()
def _add_post(username,email,number,date,Event,seats,time,anything):
    local= "C:/Users/hp/Desktop/Project/NewTry/post.db"
    connection = sqlite3.connect(local)
    db_cursor = connection.cursor()

    # Insert into database
    sql = """INSERT INTO post(username,email,number,date,Event,choose,choosetime,anything)
             VALUES(?,?,?,?,?,?,?,?)"""
    db_cursor.execute(sql,(username,email,number,date,Event,seats,time,anything))
    connection.commit()
    connection.close()
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/about")
def about():
    return render_template('about.html', title='About')
@app.route("/Book")
def Book():
    return render_template('Book.html')
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        _add_data(form.username.data,form.email.data,form.password.data)
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if search_user(form.email.data,form.password.data):
            session['email']=form.email.data
            post=search_username(form.email.data,form.password.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('EventsPage',post=post))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route("/login/EventsPage",methods=['GET','POST'])
def EventsPage():
    if 'email' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    return render_template('EventsPage.html')
@app.route(f"/login/EventsPage/marriage",methods=['GET','POST'])
def marriage():
    if 'email' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    form = MarriageForm()
    if form.validate_on_submit():
        event='marriage'
        _add_post(form.username.data,form.email.data,form.number.data,form.EventDate.data,event,form.Choose.data,form.ChooseTime.data,form.Anything.data)
        flash(f"Generated Slot for {form.username.data} and Send it to Owner",'success')
        return render_template("EventsPage.html")
    return render_template('marriage.html', form=form)
@app.route(f"/login/EventsPage/celebrations",methods=['GET','POST'])
def celebrations():
    if 'email' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    form = MarriageForm()
    if form.validate_on_submit():
        event = 'celebrations'
        _add_post(form.username.data,form.email.data,form.number.data,form.EventDate.data,event,form.Choose.data,form.ChooseTime.data,form.Anything.data)

        flash('You have been Posted Your Event Successfully!!', 'success')
        return redirect(url_for('celebrations'))
    return render_template('celebrations.html', form=form)
@app.route(f"/Login/EventsPage/Birthday",methods=['GET','POST'])
def Birthday():
    if 'email' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    form = MarriageForm()
    if form.validate_on_submit():
        event='birthday'
        _add_post(form.username.data,form.email.data,form.number.data,form.EventDate.data,event,form.Choose.data,form.ChooseTime.data,form.Anything.data)

        flash('You have been Posted Your Event Successfully!!', 'success')
        return redirect(url_for('Birthday'))
    return render_template('Birthday.html', form=form)
@app.route(f"/Adminlogin", methods=['GET', 'POST'])
def Adminlogin():

    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('Adminpage',x='admin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('Adminlogin.html', title='Login', form=form)
@app.route(f"/Adminlogin/Adminpage/<x>",methods=['GET','POST'])
def Adminpage(x):
    form = AdminForm()
    if form.validate_on_submit():
        za=print_details(form.EventDate.data)
        global detail
        detail = za
        return redirect(url_for('details'))
    return render_template('Adminpage.html',form=form,x=x)
@app.route(f"/Adminlogin/Adminpage/details",methods=['GET','POST'])
def details():
    return render_template("details.html",event=detail)
@app.route("/logout")
def logout():
    flash("you have been Logged out Successfully!",'success')
    return render_template('home.html')
@app.route(f"/Login/EventsPage/Meeting",methods=['GET','POST'])
def Meeting():
    if 'email' not in session:
        flash('Please login to access this page.', 'danger')
        return redirect(url_for('login'))
    form = MarriageForm()
    if form.validate_on_submit():
        event='meeting'
        _add_post(form.username.data,form.email.data,form.number.data,form.EventDate.data,event,form.Choose.data,form.ChooseTime.data,form.Anything.data)

        flash('You have been Posted Your Event Successfully!!', 'success')
        return redirect(url_for('Meeting'))
    return render_template('Meeting.html',form=form)
