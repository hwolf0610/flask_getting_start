# from flask import Flask
from flask import *
app=Flask(__name__)

# @app.route('/home/<int:age>')
# def home(age):
#     return "Age=%d"%age

# def about():
#     return "This is about page"
# app.add_url_rule("/about", "about", about)

# @app.route('/admin')
# def admin():
#     return 'admin'

# @app.route('/librarion')
# def librarion():
#     return 'librarion'

# @app.route('/student')
# def student():
#     return 'student'

# @app.route('/user/<name>')
# def user(name):
#     if name=='admin':
#         return redirect(url_for('admin'))
#     if name=='librarion':
#         return redirect(url_for('librarion'))
#     if name == 'student':
#         return redirect(url_for('student'))

@app.route('/login', method=['POST'])
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname =="ayush" and password == "google":
        return "Welcome %s" %uname
        
if __name__=='__main__':
    app.run(debug = True)


