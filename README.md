```dockerfile
FROM python:3.10-slim

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install git -y
RUN pip3 install -r requirements.txt
RUN pip3 install "git+https://github.com/openai/whisper.git" 
RUN apt-get install -y ffmpeg

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```

## How to run the container?
1. Open a terminal and navigate to the folder where you created the files.
2. Run the following command to build the container:

```bash
docker build -t whisper-api .
```
3. Run the following command to run the container:

```bash
docker run -p 5000:5000 whisper-api
```

Then run:

``` bash
curl -F "file=@/path/to/filename.mp3" http://localhost:5000/whisper
```

```bash
curl -F "file=@/path/to/file" http://localhost:5000/whisper
```
