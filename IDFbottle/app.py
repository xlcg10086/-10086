from flask import Flask, request, Response
import numpy as np
import cv2

app = Flask(__name__)

# 全局变量用于存储最新的图像数据
latest_frame = None

@app.route('/receive', methods=['POST'])
def receive_frame():
    global latest_frame
    # 从请求中获取图像数据
    image_data = request.files['file'].read()
    # 解码图像数据
    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # 存储最新的图像数据
    latest_frame = frame
    return 'Frame received successfully!'



def generate_frames():
    while True:
        ret, buffer = cv2.imencode('.jpg', cv2.cvtColor(latest_frame, cv2.COLOR_BGR2RGB))
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/frame')
def stream_latest_frame():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)