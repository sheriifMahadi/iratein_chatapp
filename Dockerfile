FROM ubuntu:22.04
ARG TZ=Africa DEBIAN_FRONTEND=noninteractive 
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv vim-tiny vim-athena build-essential redis


ARG USER=root
USER $USER

RUN python3 -m venv iratein_env
WORKDIR /code


COPY requirements.txt /code/
RUN /iratein_env/bin/pip install -r requirements.txt

COPY . /code/
EXPOSE 8000 

# ADD rootfs.tar.xz /
# CMD ["/bin/sh"]
CMD service docker run -p 6379:6379 -d redis:5
CMD service redis start
RUN chmod +x /code/build.sh
ENTRYPOINT ["./build.sh"]
