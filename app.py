from flask import Flask, render_template, jsonify, request
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

@app.route('/signup')
def signup():
   return render_template('signup.html')

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
   return render_template('main.html')
   
## 웹에서 사용할 APIs 

## 서버 연결
if __name__ == '__main__':
   app.run('0.0.0.0',port=5002,debug=True)