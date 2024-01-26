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

RUN chmod +x /code/build.sh
RUN chmod +x /code/deployment/start_app.sh
RUN chmod +x /code/deployment/run_daphne.sh

RUN chmod +x /code/start.sh
ENTRYPOINT ["./build.sh"]