FROM python:3.7
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN mkdir /home/work
RUN mkdir /home/work/django
RUN mkdir /home/work/uwsgi
COPY work/ /home/work
WORKDIR /home/work
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "--ini", "/home/work/uwsgi.ini"]
