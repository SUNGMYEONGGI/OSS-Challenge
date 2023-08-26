# 2023 오픈소스 컨트리뷰션 아카데미

### Git 활용 및 DevOps / MLOps

## 1. 프로젝트 소개
- 프로젝트명 : `Git 활용 및 DevOps / MLOps`
- 목적
- 범위

## 2. 도전 과제
<details>
<summary>&nbsp;2-1. Python 신조어 퀴즈 - 제시된 신조어를 맞추는 퀴즈</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 신조어/줄임말 맞추기 게임입니다. 어떤 문장의 줄임말인지 맞추면 됩니다. 
`취존` , `솔까말` , `케바케`

<h2>📚 TO-DO</h2>

- [x] Python 앱이 시작되면 환영인사가 출력
- [x] 취존이 어떤 문장의 줄임말인가요? 출력되고 입력을 받음
- [x] 입력 받은 문장과 저장된 문장을 비교해 같으면 정답 틀리면 오답 출력
- [x] 3개 질문 모두 완료하면 “3개 퀴즈 중 X개 정답”을 출력

<h2>💡 힌트</h2>

**1️⃣ 랜덤 숫자(정수형)을 생성하려면 randint(시작값, 종료값) 사용**

**2️⃣ 숫자 비교 처리는 IF-ELSE 구문**

**3️⃣ 반복문은 for 또는 while 구문 사용**

**4️⃣ 반복문을 종료하려면 break**

**5️⃣ 함수는 def 구문을 사용해 생성하며 코드를 모듈화**
</details>
<br>
<details>
<summary>&nbsp;2-2. Python 랜덤 업/다운 숫자 맞추기 게임</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 랜덤 업/다운 숫자 맞추기 게임입니다. 
##### 게임이 시작되면 1~20 사이의 랜덤 숫자를 프로그램이 가지고 시작합니다. 숫자를 입력해 맞추는 게임으로 입력한 숫자가 프로그램의 랜덤 숫자와 비교해 작으면 다운  크면 업이 출력됩니다. 총 3번의 기회가 주어집니다.

<h2>📚 TO-DO</h2>

- [x] Python 앱이 시작되면 “숫자를 맞춰보세요”가 출력되고 입력을 받음
- [x] 입력 값과 랜덤 숫자를 비교해 업 다운 출력 
- [x] 입력 값과 랜덤 숫자가 같으면 정답 출력
- [x] 총 3번의 기회. 3번 안에 못 맞추면 실패 출력
- [x] 입력 값과 숫자 비교는 Python 함수를 사용해 처리
- [x] 반복문을 이용해 3회 반복 처리

<h2>💡 힌트</h2>

**1️⃣ 랜덤 숫자(정수형)을 생성하려면 randint(시작값, 종료값) 사용**

**2️⃣ 숫자 비교 처리는 IF-ELSE 구문**

**3️⃣ 반복문은 for 또는 while 구문 사용**

**4️⃣ 반복문을 종료하려면 break**

**5️⃣ 함수는 def 구문을 사용해 생성하며 코드를 모듈화**
</details>
<br>
<details>
<summary>&nbsp;2-3. Python Flask RESTful 웹 서비스 제작</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 웹 애플리케이션 제작입니다. 
- `127.0.0.1:포트번호/hello`
  - hello world를 출력
- `127.0.0.1:포트번호/echo`
  - hello GET 방식으로 전달한 파라미터와 값을 JSON 형식으로 출력
- `127.0.0.1:포트번호/upload_image`
  - upload_image는 POST 방식으로 업로드한 이미지를 분석해 이미지의 가로 세로 픽셀 사이즈를 JSON 형식으로 출력

<h2>📚 TO-DO</h2>

- [x] Python flask 코드를 리뷰
- [x] hello route 구현
- [x] GET/POST 방식 파라미터와 값 전달 - curl 또는 Postman 등 사용
- [x] echo route 구현
- [ ] JSON 으로 echo 결과 출력 { "parameter": "value" }
- [x] upload_image route 구현
- [ ] JSON으로 upload_image 결과 출력 { "width": 1024, "height”: 512 }

<h2>💡 힌트</h2>

**1️⃣ [flask 설치](https://flask.palletsprojects.com/en/2.3.x/installation/#install-flask)**

**2️⃣ [Flask route 코드 참조](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)**

**3️⃣ [이미지 파일을 POST로 요청하는 방법과 flask에서 받아 처리하는 방법](https://stackoverflow.com/questions/41655946how-to-send-image-to-flask-server-from-curl-request)**

**4️⃣ [PIL에서 image size를 얻는 방법](https://stackoverflow.com/questions/6444548/how-do-i-get-the-picture-size-with-pil)**

</details>
<br>
<details>
<summary>&nbsp;2-4. 공부시간/점수 예측 회귀 머신러닝 모델 생성</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 예상 점수를 출력하는 머신러닝 모델 생성입니다.

<h2>📚 TO-DO</h2>

- [x] CSV 데이터를 로드
- [x] matplotlib으로 데이터 시각화
- [x] 데이터 분할
- [x] 선형 회귀 또는 다른 회귀 모델 생성
- [x] 모델 정확도 평가, MSE나 MAE 사용
- [x] 모델을 파일로 저장하고, 다시 파일을 모델을 로드
- [x] 로드한 모델로 12시간, 14시간 공부할 경우 예측 결과 출력

<h2>💡 힌트</h2>

**1️⃣ [CSV 로드](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)**

**2️⃣ [matplotlib 산점도](https://kiyoja07.blogspot.com/2019/03/python-scatter.html)**

**3️⃣ [데이터 분할](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)**

**4️⃣ [선형회귀](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)**

**5️⃣ [모델 정확도 평가](https://www.sqler.com/board_MachineLearning_AI_tip_lecture/1096470)**

**6️⃣ [모델 저장과 로드](https://scikit-learn.org/stable/model_persistence.html)**
</details>
<br>
<details>
<summary>&nbsp;2-5. 타이타닉 우주선 분류 모델 생성</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 타이타닉 우주선 데이터 분석입니다.
주어진 [데이터](https://www.kaggle.com/competitions/spaceship-titanic/overview)는 타이타닉 우주선에서 사고가 발생하여 다른 차원으로 안전하게 이동한 승객과 그렇지 못한 승객에 대한 정보를 포함합니다. 이 정보를 분석하여 분류(Classification) 모델을 생성하고 모델의 정확도를 평가하는 작업을 수행할 것입니다. 

<h2>📚 TO-DO</h2>

- [x] 분류 모델에 대한 이해
- [x] 대량 데이터 처리를 위한 pandas
- [x] EDA 수행
- [x] 모델을 생성하고 AUC 계산
- [x] 모델을 파일로 저장하고, 다시 파일을 모델을 로드

</details>
<br>
<details>
<summary>&nbsp;2-6. Cat & Dogs 이미지 분류 딥 러닝 모델 생성</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 고양이와 강아지 분류 딥 러닝 모델을 생성합니다.
딥러닝 프레임워크를 활용해 모델을 생성하고, 이 모델에 개나 고양이 아무 이미지나 넣으면 개 또는 고양이로 분류해 결과를 출력합니다.

<h2>📚 TO-DO</h2>

- [x] 딥러닝 실행
- [x] 대량 이미지 파일 처리
- [x] 이미지를 머신러닝이 처리할 수 있는 포맷으로 변환
- [x] 딥러닝 모델을 생성하고 모델 평가
- [x] 딥러닝 모델을 파일로 저장하고 다시 로드
- [x] 로드된 딥러닝 모델에 아무 강아지/고양이 이미지를 입력하고 예측 결과 출력

<h2>💡 힌트</h2>

**1️⃣ keras 공식 가이드([Image classification from scratch](https://keras.io/examples/vision/image_classification_from_scratch/))**

**2️⃣ 모델 저장 및 로드([Keras 모델 저장 및 로드 | TensorFlow Core](https://www.tensorflow.org/guide/keras/save_and_serialize?hl=ko)) 또는 ([케라스(keras) 모델 저장(save) 및 불러오는(load) 2가지 방법](https://ltlkodae.tistory.com/13))**
</details>
<br>
<details>
<summary>&nbsp;2-7. Git과 Github 활용</summary>
<h2>💁🏻‍♂️ 목표</h2>

#### 도전과제는 코드 버전 컨트롤 시스템 Git과 원격 저장소 Github 를 사용해 코드를 게시합니다.
지난 코드들을 Github에 게시하고, 기본적인 코드 관리를 위해 Git 명령을 사용하는 방법을 이해합니다.

<h2>📚 TO-DO</h2>

- [x] 신조어퀴즈 코드를 Github 리포지토리로 Push
  - [x] Github 리포지토리를 만들고 “도전과제 1번 신조어 퀴즈” 코드를 push
  - [x] Branch를 생성
  - [x] branch에서 README, .gitignore와 MIT License 파일을 추가 
  - [x] push 하고 main branch에 merge 수행

- [ ] 업다운 퀴즈 코드를 Github 리포지토리로 Push
  - [x] 먼저 새로운 리포지토리를 Github에서 생성
  - [x] git clone 명령으로 리포지토리 가져오기
  - [x] “도전과제 2번 업다운 퀴즈” 코드를 Github으로 push
  - [ ] Github에서 branch를 생성
  - [ ] branch에서 린트(Lint) 처리와 단순 Unit test 코드를 추가
  - [ ] push & main branch에 merge 수행

- [ ] Flask 웹앱에 머신러닝 예측 기능 추가
  - [ ] `3번 Flask 앱`에 `4번 공부시간/점` 코드를 Route 추가
  - [ ] 새로운 Github 리포지토리로 push
  - [ ] curl이나 Postman으로 GET방식 요청
  - [ ] JSON 으로 예측 결과 출력 { "score": 80 }

- [x] Flask 웹앱에 딥러닝 예측 기능 추가
  - [x] `6번 Cats&Dogs 이미지 분류` 예측 코드를 Route 추가
  - [x] 새로운 Github 리포지토리로 push
  - [x] curl이나 Postman으로 POST방식으로 아무 개/고양이 이미지 파일을 요청
  - [x] JSON 으로 예측 결과 출력

<h2>💡 힌트</h2>

**1️⃣ [Git과 Github 튜토리얼](https://tagilog.tistory.com/377)**

**2️⃣ [SSH Key 인증이해](https://velog.io/@skyepodium/Github-SSH-Key-%EB%93%B1%EB%A1%9D%ED%95%98%EA%B8%B0)**

**3️⃣ [Python 린트](https://www.sqler.com/board_CSharp/1095920)**

**4️⃣ [Pytest를 이용한 unit test 코드 생성](https://velog.io/@sangmin7648/Flask-%EB%8B%A8%EC%9C%84-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EA%B8%B0-pytest)**

**5️⃣ [vscode source control 기능](https://kim-oriental.tistory.com/31)**
</details>




<!-- ## 3. 구현
- 기술 스택
- 주요 기능
- 문제 해결 과정

## 4. 테스트 및 검증
- 단위 테스트
- 통합 테스트
- 성능 평가

## 5. 결론
- 성과
- 한계
- 향후 계획

## 참고 문헌

## 부록 -->