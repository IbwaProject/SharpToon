import os #디렉토리 절대 경로
import shutil
from flask import Flask, render_template, jsonify, request, redirect

#로그인, 회원가입 관련
from flask_sqlalchemy import SQLAlchemy
from models import db
from models import Fcuser
from flask import session #세션

from flask_wtf.csrf import CSRFProtect
from forms import ChangePWForm, RegisterForm, LoginForm, ChangeProfile

#StarGAN
from StarGAN import model
from StarGAN import main as mainPy
from StarGAN import solver

app = Flask(__name__)

## HTML을 주는 부분
@app.route('/')
def MainSplash():
   celeba_image_dir = 'static/images/input'
   result_dir = 'static/images/result'
   if os.path.exists(celeba_image_dir) :
      shutil.rmtree(celeba_image_dir)
   if os.path.exists(result_dir) :
      shutil.rmtree(result_dir)
   return render_template('MainSplash.html')

@app.route('/main')
def main():
   userid = session.get('userid', None)
   username = session.get('username')
   return render_template('main.html', userid=userid, username=username)

@app.route('/changePW', methods = ['GET', 'POST'])
def changePW() :
   form = ChangePWForm()
   if form.validate_on_submit() :
      userid = session.get('userid', None)
      fcuser = Fcuser()
      user = fcuser.query.filter_by(userid=userid).first()
      user.password = form.data.get('password')
      db.session.commit()
      return redirect('/Settings')
   return render_template('changePW.html', form=form)

@app.route('/forgotPW')
def forgotPW():
   return render_template('forgotPW.html')

@app.route('/login', methods=['GET','POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      session['userid'] = form.data.get('userid')
      session['username'] = form.data.get('username')
      return redirect('/main')
   return render_template('login.html', form=form)

@app.route('/logout', methods=['GET'])
def logout():
   session.pop('userid', None)
   return redirect('/main')

#회원가입
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
   form = RegisterForm()
   if form.validate_on_submit() :
      fcuser = Fcuser()
      fcuser.userid = form.data.get('userid')
      fcuser.username = form.data.get('username')
      fcuser.password = form.data.get('password')
      fcuser.stateM = "상태메세지를 입력해주세요"

      db.session.add(fcuser)
      db.session.commit()
      return redirect('/main')
   
   return render_template('signup.html', form=form)

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
   fcuser = Fcuser()
   userid = session.get('userid', None)
   user = fcuser.query.filter_by(userid=userid).first()
   username = user.username
   stateM = user.stateM
   return render_template('ViewProfile.html', userid=userid, username=username, stateM=stateM)

@app.route('/changeProfile', methods = ['GET', 'POST'])
def changeProfile():
   form = ChangeProfile()
   if form.validate_on_submit():
      fcuser = Fcuser()
      userid = session.get('userid', None)
      user = fcuser.query.filter_by(userid=userid).first()
      user.username = form.data.get('username')
      user.stateM = form.data.get('stateM')
      db.session.commit()
      return redirect('/ViewProfile')
   return render_template('changeProfile.html', form=form)

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
      app.config['SECRET_KEY'] = '123'

      csrf = CSRFProtect()
      csrf.init_app(app)

      db.init_app(app) #app설정값 초기화
      db.app = app #Models.py에서 db를 가져와서 db.app에 app을 명시적으로 넣는다
      db.create_all() #DB생성

      app.run('0.0.0.0',port=5002,debug=True)