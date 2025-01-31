FROM python:3.9.18-slim-bookworm

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN ls

EXPOSE 5050  

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5050" ]
