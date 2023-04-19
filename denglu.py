from flask import Flask, request, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mysql.infoschema :liyang123@127.0.0.1:5000/user'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # 登录成功，可以跳转到其他页面
            return redirect('/home')
        else:
            # 登录失败，需要显示失败信息
            flash('登录失败，请检查用户名和密码是否正确')
    return render_template('login.html')

@app.route('/index')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

