import os #디렉토리 절대 경로
from flask import Flask, render_template, jsonify, request, redirect

#로그인, 회원가입 관련
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import User

#StarGAN
from StarGAN import model
from StarGAN import main as mainPy
from StarGAN import solver

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

#회원가입
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
   if request.method == 'GET':
      return render_template('signup.html')
   else :
      name = request.form.get('name')
      userid = request.form.get('userid')
      password = request.form.get('password')
      password_2 = request.form.get('password_2')

      if not(name and userid and password and password_2) : 
         return "모든 정보를 입력해주세요"
      elif password != password_2 : 
         return "비밀번호가 일치하지 않습니다."
      else : 
         usertable=User() #user_table 클래스
         usertable.name = name
         usertable.userid = userid
         usertable.password = password
            
         db.session.add(usertable)
         db.session.commit()
         return redirect('/main')

@app.route('/option_hair')
def option_hair():
   return render_template('ChangePeopleSelect.html')

@app.route('/option_cartoon')
def option_cartoon():
   return render_template('option_cartoon.html')

@app.route('/result')
def result():
   return render_template('result.html')

@app.route('/select_image')
def select_image():
   return render_template('select_image.html')

@app.route('/Settings')
def Settings():
   return render_template('Settings.html')

@app.route('/camera')
def camera():
   return render_template('camera.html')  

@app.route('/ViewProfile')
def ViewProfile():
   return render_template('ViewProfile.html')

@app.route('/run_model')
def run_model():
   #exec(open("StarGAN/main.py").read())
   #input = "--mode test --dataset CelebA --image_size 128 --c_dim 5 --selected_attrs Black_Hair Blond_Hair Brown_Hair Male Young --celeba_image_dir data/custom/images --attr_path data/list_attr_celeba_custom.txt --model_save_dir='stargan_celeba_128/models' --result_dir='stargan_celeba_128/results'"
   mainPy.main()
   return render_template('result.html')
   
## 웹에서 사용할 APIs 

## 서버 연결
if __name__ == '__main__':
   #데이터베이스
      basedir = os.path.abspath(os.path.dirname(__file__)) #현재 파일이 있는 디렉토리 절대 경로
      dbfile = os.path.join(basedir, 'db.sqlite') #데이터베이스 파일을 만든다

      app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile
      app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True #사용자에게 정보 전달완료하면 teadown. 그 때마다 커밋=DB반영
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #추가 메모리를 사용하므로 꺼둔다

#    db = SQLAlchemy() #SQLAlchemy를 사용해 데이터베이스 저장
      db.init_app(app) #app설정값 초기화
      db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
      db.create_all() #DB생성

      app.run('0.0.0.0',port=5002,debug=True)