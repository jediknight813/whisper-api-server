FROM python:3.9.9-bullseye

WORKDIR /src

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip install git+https://github.com/openai/whisper.git 
RUN apt-get update && apt-get install -y ffmpeg

COPY audio_files ./audio_files/
COPY app.py ./


ENTRYPOINT ["python3", "-u", "app.py"]

# docker build -t whisper-api-server:latest .