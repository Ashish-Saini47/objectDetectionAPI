from flask import Flask, jsonify
from flask import request
import torch

app = Flask(__name__)

@app.route("/", methods=["POST"])
def detect():
    reqRef = request.get_json(force=True)
    weigth= reqRef["model"]
    imgUrl=reqRef["imgUrl"]
    try:
        model = torch.hub.load('ultralytics/yolov5', 'custom', weigth )
        results = model(imgUrl)

        return jsonify({
            "weigthURL":"Detected",
       
        })
    except:
        return jsonify({
            "weigthURL":"not Detected",})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
