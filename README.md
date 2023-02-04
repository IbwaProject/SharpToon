<a href="">
    <img src="https://user-images.githubusercontent.com/69100145/216748760-31f6884c-f837-42cd-ab5f-e78fce65ec6c.jpg" align="right" height="90" />
</a>


# #T͟o͟o͟n͟
> 인공지능을 활용한 웹툰 저작도구 웹사이트

  <img src="https://img.shields.io/badge/Sublime Text-FF9800?style=flat&logo=Sublime Text&logoColor=white"/>  <img src="https://img.shields.io/badge/PyCharm-000000?style=flat&logo=PyCharm&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=flat&logo=Flask&logoColor=white"/>  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=TensorFlow&logoColor=white"/>  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=PyTorch&logoColor=white"/>  <img src="https://img.shields.io/badge/NumPy-013243?style=flat&logo=NumPy&logoColor=white"/>  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/>  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=HTML5&logoColor=white"/>  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=CSS3&logoColor=white"/>  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white"/>  <img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=Notion&logoColor=white"/>  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white"/>


## 📢 프로젝트 소개
- 헤어샵 + 카툰의 의미로 사용자가 업로드한 이미지의 헤어스타일을 변환한 후 만화화하여 제공하는 웹 페이지
- 지능형 웹툰 저작 및 스타일 변형을 위한 학습데이터를 생성하고, 인공지능 학습 성능 향상을 유도하기 위한 학습데이터를 확장하는 기술을 활용한다.
- 노동 집약도가 높은 웹툰 산업에 인공지능 저작도구를 활용한 생산성 향상한다.
- 그림을 못 그리는 사람도 스토리 아이디어를 통해 웹툰을 만들 수 있도록 한다.

### 시연 영상
<a href="https://youtu.be/saahFwPO-ls">
 <img src="https://user-images.githubusercontent.com/69100145/216749584-9e4c7bd8-2263-49b6-ac26-ad3d7d10828a.png" height="300"/>
</a><br>
위 이미지를 클릭하면 프로젝트 시연 영상으로 이동합니다.

### ScreenShots
<details>
<summary> #툰 화면 보기 </summary>

</details>

## ✔ 적용 사례
<img src="https://user-images.githubusercontent.com/69100145/216751639-d6319e90-1f58-4825-bb84-c855d3c4cbd8.png" height="300"/>

## 🛠 핵심 기능
### 사용자 헤어스타일 변환
- 검정, 금발, 갈색 중 원하는 스타일을 선택하는 웹페이지
- StarGAN을 활용한 머리 색 변환 학습 모델 생성
- 옵션 선택 후 생성된 "StarGAN" 모델에 적용

### 만화풍으로 변환
- OpenCV를 활용하여 사용자로부터 입력받은 사진의 Edge를 추출해 자동 채색
- CartoonGAN, White-Box 모델로 그림을 자동으로 웹툰화하는 방법 사용

### 말풍선 삽입
- Ballon 버튼을 눌러 사진에 말풍선 추가
- TEXT 버튼을 눌러 말풍선에 텍스트 추가
- 텍스트만 추가하여 자막 기능으로 활용
- 쉬운 사이즈 조절, 이동 및 삭제 기능 제공

## 💡 서비스 구성도
<img src="https://user-images.githubusercontent.com/69100145/216750429-b70c5f49-5867-4247-b254-e5cacf60b56f.png" height="400"/>

- `Back-end`
  - 얼굴인식, 헤어 스타일 변환 알고리즘 : 얼굴 인식 알고리즘으로 인물의 얼굴 부분을 분석하고 다른 헤어 스타일로 변환 시킴
  - 만화화 알고리즘 : OpenCV의 내장 함수를 통한 만화화, White-Box와 CartoonGAN 모델을 사용하여 그림을 자동으로 웹툰화하는 방법 사용
  - 변환된 이미지 결과 : 변환된 결과 이미지는 다운로드 가능

- `Front-end`
  - 사진 데이터 요청 : 입력한 사진의 인물에 대한 헤어 스타일 변화, 여러가지 그림체로의 변화 등 데이터 요청

## 📌 실행 방법
- #툰 원격 저장소를 clone
```shell
git clone https://github.com/IbwaProject/SharpToon.git
```

- 생성된 로컬 저장소로 이동 후 독립된 가상환경 생성 및 실행
```shell
python -m venv env
env\Scripts\activate.bat
```

- 플라스크 서버 실행
```shell
python app.py run
```

## 👩‍💻 Developer
|                                 <a href="https://github.com/yehang218">김석희</a>                                |                                                      <a href="https://github.com/ksb3458">김수빈</a>                                                       |                                                      <a href="https://github.com/jsl1113">이지선</a>                                                       |                                 <a href="https://github.com/kny-5625">김나영</a>                                 |
| :--------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------: |
| ![김석희](https://user-images.githubusercontent.com/69100145/216752333-a03bf85a-5acd-4d27-ac1d-33d302c902c3.png) | ![김수빈](https://user-images.githubusercontent.com/69100145/216752384-cf0a7286-9946-4538-8c16-9d962d72afd0.png) | ![이지선](https://user-images.githubusercontent.com/69100145/216752395-015a1bed-7e42-4f18-b504-c7f02bf9a63a.png) | ![김나영](https://user-images.githubusercontent.com/69100145/216752407-7ed636ba-10b9-41c8-aa29-614b6c8254f9.png) |
