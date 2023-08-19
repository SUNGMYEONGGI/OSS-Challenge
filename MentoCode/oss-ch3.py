# pip install Flask
# pip install pillow
# flask --app c3 run   # 실행 커맨드
from flask import Flask, request, jsonify
from PIL import Image
import json

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


# echo code
@app.route('/echo', methods=["POST"])
def echo():
    param = request.get_json()
    return jsonify(param)


# image post and return image size code
@app.route('/upload_image', methods=["POST"])
def upload_image():
    img = Image.open(request.files['file'])
    width, height = img.size
    imgsize = {}  # dict data type for json response
    imgsize['width'] = width
    imgsize['height'] = height
    return json.dumps(imgsize)
