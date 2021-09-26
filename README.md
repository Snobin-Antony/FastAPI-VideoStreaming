# Video-Streaming-in-Web-Browsers-with-FastAPI
Streaming live videos from IP Cameras or Webcam with FastAPI ,Python and OpenCV

For implementing the computer vision part I used the OpenCV module in Python and to display the live stream in the web browser I used the FastAPI web framework. 

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. 

To run, install unvicorn, fastapi and necessary packages

`python3 fastapiserver.py`

or 

`uvicorn fastapiserver:app --reload`

Create a folder named templates and put index.html file in that folder