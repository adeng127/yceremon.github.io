from flask import Flask, request, redirect, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    # 将用户名和密码存储在数据库中
    password_hash = generate_password_hash(password)
    # 假设您已经定义了一个 User 模型并且已经初始化了数据库
    user = User(username=username, password=password_hash)
    db.session.add(user)
    db.session.commit()
    # 重定向到登录页面
    return redirect(url_for('login'))