# pip install Flask
# pip install pillow
# flask --app ch3 run   # 실행 커맨드

from flask import Flask, request, jsonify
from PIL import Image
import json


app = Flask(__name__)


# # score predict모델을 로드하고 예측 실행
# loaded_model = joblib.load('model.pkl')


@app.route('/')
def index():
    return '<h1>Index Page</h1>'


@app.route('/hello')
def hello():
    return 'Hello, World'


# echo code
@app.route('/echo', methods=["POST"])
def echo():
    param = request.get_json()
    return jsonify(param)


@app.route("/upload_image", methods=["POST"])
def upload_image():
    img = Image.open(request.files['file'])
    width, height = img.size
    imgsize = {}
    imgsize['width'] = width
    imgsize['height'] = height
    return json.dumps(imgsize)