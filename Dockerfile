FROM python:2.7-alpine
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN mkdir /app
COPY requirements.txt /app
#COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt


ADD https://github.com/getpelican/pelican-plugins/archive/6079192.tar.gz /tmp/
RUN tar -xzf /tmp/6079192.tar.gz -C /tmp && mv /tmp/pelican-plugins-* /pelican-plugins

#ADD https://github.com/getpelican/pelican-plugins/archive/6079192.tar.gz /tmp/
#ADD https://github.com/thndgonz/Nuja/archive/a58fd6.tar.gz /tmp/temp.tar.gz
#ADD https://github.com/shouldsee/Nuja/archive/7521546.tar.gz /tmp/temp.tar.gz
RUN touch hi
ADD https://github.com/shouldsee/Nuja/archive/master.tar.gz /tmp/temp.tar.gz
RUN tar -xzf /tmp/temp.tar.gz -C /tmp && mv /tmp/Nuja-* /pelican-theme

#ADD 
#THEME

#RUN mkdir -p /pelican-plugins && tar -xzf 6079192.tar.gz -C /pelican-plugins
COPY src /app

EXPOSE 8000
RUN pelican
WORKDIR /app/output
CMD ["python2","-m","SimpleHTTPServer","8000"]
#CMD ["pelican", "--listen"]
#CMD ["gunicorn", "-w 4", "main:app"]
