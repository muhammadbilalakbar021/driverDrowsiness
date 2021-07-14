from flask import Flask, render_template, Response, request
import cv2
import datetime, time
import os, sys
import numpy as np
from threading import Thread
from collections import defaultdict

from DrowsinessDetection.face_rec import process_and_encode, init, detect_and_display
from FaceRecognition.recognizer import findFace

global capture
capture = 0
app = Flask(__name__, template_folder='./templates')
camera = cv2.VideoCapture(0)


def gen_frames():
    global out, capture, rec_frame
    while True:
        success, frame = camera.read()
        if success:
            if capture:
                capture = 0
                p = os.path.sep.join(['shots', "user.png"])
                cv2.imwrite(p, frame)

            try:
                ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            except Exception as e:
                print(e)

        else:
            print("Nothing")


@app.route('/')
def index():
    return render_template(r'index.html')


@app.route('/take_snap')
def take_snap():
    return render_template(r'photoCapture.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video_fee')
def video_fee():
    return Response(drows(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/face', methods=['POST', 'GET'])
def recognizer():
    _, res = findFace('shots/user.png')
    return render_template(r'DrowsinessDetection.html')


@app.route('/drowsiness', methods=['POST', 'GET'])
def drows():
    (model, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, video_capture, images) = init()
    data = process_and_encode(images)

    eyes_detected = defaultdict(str)
    while True:
        frame = detect_and_display(model, video_capture, face_detector, open_eyes_detector, left_eye_detector,
                                   right_eye_detector, data, eyes_detected)
        ret, buffer = cv2.imencode('.jpg', cv2.flip(frame, 1))
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/requests', methods=['POST', 'GET'])
def tasks():
    global switch, camera
    if request.method == 'POST':
        if request.form.get('click') == 'Capture':
            global capture
            capture = 1
    elif request.method == 'GET':
        return render_template('photoCapture.html')
    return render_template('photoCapture.html')


if __name__ == '__main__':
    app.run()

camera.release()
cv2.destroyAllWindows()
