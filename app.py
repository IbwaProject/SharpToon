from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def MainSplash():
   return render_template('MainSplash.html')


@app.route('/main')
def main():
   return render_template('main.html')
   
## 웹에서 사용할 APIs 

## 서버 연결
if __name__ == '__main__':
   app.run('0.0.0.0',port=5002,debug=True)