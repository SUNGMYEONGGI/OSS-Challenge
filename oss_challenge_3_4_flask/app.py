# pip install Flask
# pip install pillow
# flask --app ch3 run   # 실행 커맨드

from flask import Flask, request, jsonify
from PIL import Image
import json
import pandas as pd
import joblib


app = Flask(__name__)

# --------------------------------------------------------------------------------
# Challenge 3 Code 
# --------------------------------------------------------------------------------


# score predict모델을 로드하고 예측 실행
loaded_model = joblib.load('model.pkl')


# @app.route('/')
# def index():
#     return '<h1>Index Page</h1>'


@app.route('/hello')
def hello():
    return 'Hello, World'


# echo code
@app.route('/echo', methods=["POST"])
def echo():
    param = request.get_json()
    return jsonify(param)


@app.route("/", methods=["POST"])
def index():
    img = Image.open(request.files['file'])
    width, height = img.size
    return json.dumps({'width': width, 'height': height})

# --------------------------------------------------------------------------------
# Challenge 4 Code 
# --------------------------------------------------------------------------------

# predict_score code
@app.route('/predict_score', methods=["GET"])
def predict_score():
    param = request.args.get("hours")
    print('디버그 파라미터: ', param)

    lst_param = []
    lst_param.append(param)
    X_test = pd.DataFrame({'hours': lst_param}).to_numpy()
    y_pred = loaded_model.predict(X_test)
    y_pred
    print('디버그 y_pred: ', y_pred)

    result = {}
    result['score'] = y_pred[0][0]
    return json.dumps(result)

if __name__ == '__main__':
    app.run()
