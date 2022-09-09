from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def MainSplash():
   return render_template('MainSplash.html')

@app.route('/main')
def main():
   return render_template('main.html')

@app.route('/forgotPW')
def forgotPW():
   return render_template('forgotPW.html')

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/option_hair')
def option_hair():
   return render_template('ChangePeopleSelect.html')

@app.route('/option_cartoon')
def option_cartoon():
   return render_template('option_cartoon.html')
   
## 웹에서 사용할 APIs 

## 서버 연결
if __name__ == '__main__':
   app.run('0.0.0.0',port=5002,debug=True)