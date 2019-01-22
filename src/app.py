from flask import Flask,render_template, request, jsonify, session, redirect, url_for
from pprint import pprint
import psycopg2
import psycopg2.extras
from data import Content
from wtforms import Form, StringField, PasswordField, validators
from dbconnect import connect

app  = Flask(__name__)

conn = connect()
topic_list = Content()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles')
def articles():
    pprint(topic_list)
    name = "baronkimaru"
    return render_template("articles.html", topic_list = topic_list)

@app.route('/article/<string:id>/')
def article(id):
    return render_template("article.html", id = id)

class RegistrationForm(Form):
    name = StringField('Name' , [validators.Length(min = 4,max = 20)])
    username = StringField('Username' , [validators.Length(min = 4,max = 20)])
    email = StringField('Email' , [validators.Length(min = 6,max = 40)])
    password = PasswordField('Password' , [
        validators.DataRequired(),
        validators.EqualTo('confirm', message= "Passwords are not The same")
        ])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods = ['GET','POST'])
def register():
    """Registers the user drawing from the RegistrationForm class"""
    form  = RegistrationForm(request.form)
    try:
        if request.method == "POST" and form.validate():
            print("Yes!!!")
            name  = form.name.data
            username  = form.username.data
            email  = form.email.data
            password  = form.password.data

            print(name)
            # cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            # pprint(cur)
            # sql_insert = """INSERT INTO dev_test.tbl_users(name,email, username, password) VALUES(%s %s %s %s)"""
            # cur.execute(sql_insert, (name, email, username, password, ))
            # conn.commit()
            # cur.close()
            #
            # flash("Thank you for registering. Proceed to Login", "success")
            # redirect(url_for('index'))

    finally:
        if conn is not None:
            conn.close()
        return render_template("register.html" , form = form)

if __name__ == "__main__":
    app.run(debug = True)
