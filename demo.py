from flask import Flask, request
app = Flask(__name__)

@app.route('/demo.html', methods=['POST'])
def demo():
    data = request.get_json()
    username = data['username']
    password = data['password']
   
    print('Username:', username)
    print('Password:', password)
   
    return 'success'

if __name__ == '__main__':
    app.run()