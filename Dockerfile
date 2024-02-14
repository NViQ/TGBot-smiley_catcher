FROM python:3.10

WORKDIR /app

RUN pip3 install --upgrade pip

COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . /app/

EXPOSE 3001

CMD python3 ./smileys_catcher/main.py