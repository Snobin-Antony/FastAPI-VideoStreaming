# import numpy as np
import time
import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.video.set(3, 1920)  # float `width`
        self.video.set(4, 1080)  # float `height`
        # self.video = cv2.VideoCapture('Class_Det.mp4')
        # self.video = cv2.VideoCapture(args["input"])

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        print(image.shape)
        image=cv2.resize(image,(640,360))
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

def gen(camera):
    c = 1
    start = time.time()
    while True:
        start_1 = time.time()
        if c % 20 == 0:
            end = time.time()
            FPS = 20/(end-start)
            print("FPS_avg : {:.6f} ".format(FPS))
            start = time.time()
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        end_1 = time.time()
        FPS = 1/(end_1-start_1)
        print("FPS : {:.6f} ".format(FPS))
        c +=1

@app.get('/video_feed')
def video_feed():
    return StreamingResponse(gen(VideoCamera()), media_type="multipart/x-mixed-replace;boundary=frame")
if __name__ == '__main__':
    uvicorn.run("fastapiserver:app", host="0.0.0.0", port=5000, access_log=False)