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
        model = torch.hub.load('ultralytics/yolov5', 'custom', path="best.tflite" ,force_reload=True)
        results = model("1.jpeg")
        print(results.xyxy[0] )
        print(results.pandas().xyxy[0] )
        return jsonify({
            "weigthURL":"Detected",
       
        })
    except Exception as e:
        print(type(str(e)))
        return jsonify({
            "weigthURL":"not Detected",
            "error":str(e)
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
