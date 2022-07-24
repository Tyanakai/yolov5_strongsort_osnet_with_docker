FROM python:3
WORKDIR /usr/src/app
COPY python_src/yolo_strong_sort/requirements.txt ./
RUN pip install -U pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install -y ffmpeg
RUN pip install -q ffmpeg-python
# RUN mkdir ./python-src/Yolov5_StrongSORT_OSNet/yolov5/weights/
# RUN wget -nc https://github.com/ultralytics/yolov5/releases/download/v6.1/yolov5x6.pt -O ./python-src/Yolov5_DeepSort_OSNet/yolov5/weights/yolo.pt
