from flask import Flask,request, render_template, redirect, session, jsonify, url_for
import requests,random
from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from os import urandom
import os.path
from captcha.image import ImageCaptcha
from flask import flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = urandom(24)
#设置连接url
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:liyang123@127.0.0.1/user'
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\LENOVO\\Desktop\\gpt\\电商动态网页\\static\\retore'

# app.config['UPLOAD_FOLDER'] = os.path.join(app.static_folder, 'test')

# 创建一个SQLAlchemy对象，用来管理数据库连接和操作
db = SQLAlchemy(app)
image_captcha = ImageCaptcha()
#设置数据库模型
class User(db.Model):
    #定义
    id = db.Column(db.Integer, primary_key=True,autoincrement=True) 
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    Email=db.Column(db.String(120))

class search(db.Model):
    name=db.Column(db.Integer,primary_key=True,autoincrement=True)
    color=db.Column(db.String(80),unique=True)
    
# 禁用缓存
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

# 定义一个Flask路由，用于处理客户端发送到/login.html端点的GET和POST请求
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        random_s= str(random.randint(1000, 9999))
        username = request.form['username']
        password = request.form['password']
        #使用username查询用户，并返回第一个查询成功的所有属性。
        user = User.query.filter(User.username==username).first()
        
        
        captcha_code = request.form.get('captcha')
        captcha_image = image_captcha.generate_image(random_s)
        
        captcha_image.save(r'c:\Users\LENOVO\Desktop\gpt\电商动态网页\static\captcha.png')
        
        if user and user.password == password:
            session['username'] = username  # 将用户名存储到 session 中
            return redirect("/aindex.html")
        if not username:
            error1 = "您未输入用户名"
            return render_template("enlo.html", error=error1)
        if not password:
            error1 = "您未输入密码"
            return render_template("enlo.html", error=error1)
        
        else:
            error = "用户名或密码错误" 
            return render_template("enlo.html", error=error) 
   
@app.route('/aindex.html',methods=['GET','POST'])
def aindex():
    return render_template("aindex.html")


@app.route('/register.html',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        q_password=request.form['q_password']
        Email=request.form['email']
        error = None
        random_s= str(random.randint(1000, 9999))
        user = User.query.filter(User.username==username).first()
        captcha_code = request.form.get('captcha')
        captcha_image = image_captcha.generate_image(random_s)
        captcha_image.save(r'c:\Users\LENOVO\Desktop\gpt\电商动态网页\static\captcha.png')
        
            
        if user:
            if not username:
                error = "您未写入用户名"
            if not password:
                error = "您未写入密码"
            if not Email:
                error = "您未写入邮箱"
            if q_password!=password:
                error="对不起，两次密码输入不一致"
            if user and user.password == password:
                error="对不起，已有账户"
          
              
            if error:
                return render_template("enlo.html", error=error)
            
            
        else:
            new_user = User(username=username, password=password, Email=Email)
            db.session.add(new_user)
            db.session.commit()
            error1="用户创建成功！请登录。"
            return render_template("enlo.html",error=error1)
   

@app.route('/infor.html', methods=['GET', 'POST'])
def infor():
    if request.method == 'GET':
        username = session['username']

        user = User.query.filter(User.username == username).first()
        if user:
            Email=user.Email
            password=user.password
            return render_template("infor.html",  username=username,Email=Email,password=password)
        else:
            return '用户信息不存在!'

@app.route("/server", methods=['GET','POST'])
def server():
    
    data = request.get_json()
    one=data["one"]
    color = data["color"]
    size = data["size"]
    
    print(data)  # 打印传递给模板的数据
    
     #保存数据到session
    session['color'] = color
    session['size'] = size
    session['one']=one
    # 处理数据
    return render_template("demo.html",color=color,size=size,one=one)

@app.route("/demo.html", methods=['GET','POST'])
def demo():
    color = session.get('color')
    size = session.get('size')
    one=session.get('one')
    return render_template("shopcar.html",color=color,size=size,one=one)

 #搜索功能
@app.route("/search",methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search= request.form['search']
        search_all = search.query.filter(search.name == search).all()
        if search:
            name=search_all.name
            color=search_all.color
        return render_template("search.html",name=name,color=color)
        
       
#上架商品页面


@app.route('/test2.html')
def test2():
    return render_template("test2.html")

@app.route('/upload', methods=['POST','GET'])
def upload():
    
    files = request.files.getlist('file')
    if not files:
        # 如果文件列表为空，返回错误信息
        print("批量上传失败")
    filenames = []
    for file in files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filenames.append(filename)
    # 显示消息
    print('文件已成功上传')
    print(files)
    # 修改这一行，只传递第一个文件的文件名
    return render_template('test.html',  images=filenames)




# @app.route('/test.html',methods=['POST','GET'])
# def test():
#     # 获取图片文件列表
#     images = os.listdir(app.config['UPLOAD_FOLDER'])
#     print(images)  # 打印图片文件列表
#     # 渲染模板并显示图片

#     return render_template('test.html', images=images)



@app.route('/index.html')
def index1():
    return render_template("index.html")

@app.route('/shopcar.html')
def shopcar():
    return render_template("shopcar.html")

@app.route('/shop1.html')
def shop1():
    return render_template("shop1.html")


@app.route('/shopN.html')
def shopN():
    return render_template("shopN.html")
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/enlo.html')
def enlo():
    
    random_s= str(random.randint(1000, 9999))
    captcha_code = request.form.get('captcha')
    captcha_image = image_captcha.generate_image(random_s)
    
    captcha_image.save(r'c:\Users\LENOVO\Desktop\gpt\电商动态网页\static\captcha.png')
        
    return render_template("enlo.html")






if __name__ == '__main__':
    # 设置输出SQLAlchemy执行的SQL语句
    app.config['SQLALCHEMY_ECHO'] = True
    app.run(debug=True)






