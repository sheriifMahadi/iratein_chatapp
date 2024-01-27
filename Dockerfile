FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

ARG USER=root
USER $USER

RUN python3 -m venv iratein_env
WORKDIR /code


COPY requirements.txt /code/
RUN /iratein_env/bin/pip install -r requirements.txt

COPY . /code/
EXPOSE 8000 

docker run -p 6379:6379 -d redis:5
docker container ls

RUN chmod +x /code/build.sh
ENTRYPOINT ["./build.sh"]
