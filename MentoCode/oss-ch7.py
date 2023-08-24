import pandas as pd
import joblib

import tensorflow as tf
from tensorflow import keras

from flask import Flask, request, jsonify
from PIL import Image
import json

app = Flask(__name__)

# score predict모델을 로드하고 예측 실행
loaded_model = joblib.load('model.pkl')

# cat_dog 모델 로드
new_model = tf.keras.models.load_model('c6/cats_dogs.h5')
image_size = (180, 180)

# @app.before_first_request
# def before_first_request():


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


# predict_score code
@app.route('/predict_score', methods=["GET"])
def predict_score():
    # param = request.get_json()
    param = request.args.get("hours")
    print('디버그 파라미터: ', param)

    lst_param = []
    lst_param.append(param)
    # 14를 df에서 np로 변환하고 predict 수행
    X_test = pd.DataFrame({'hours': lst_param}).to_numpy()
    y_pred = loaded_model.predict(X_test)
    y_pred
    print('디버그 y_pred: ', y_pred)

    result = {}
    result['score'] = y_pred[0][0]
    return json.dumps(result)


# predict_cat_dog code
@app.route('/predict_cat_dog', methods=["POST"])
def predict_cat_dog():
    img = Image.open(request.files['file'])
    _ = img.save("_temp.jpg")

    # test_loss, test_acc = new_model.evaluate(x,  y, verbose=2)
    img = keras.utils.load_img(
        "_temp.jpg", target_size=image_size
    )
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis

    predictions = new_model.predict(img_array)
    score = float(predictions[0])
    print("디버그 score", score)
    res = "This image is " + \
        str(100 * round(1 - score, 2)) + "% cat and " + \
        str(100 * round(score, 2)) + "% dog."

    if score > 0.5:
        class_name = "dog"
    else:
        class_name = "cat"

    result = {}
    result['result'] = res
    result['class_name'] = class_name
    return json.dumps(result)
