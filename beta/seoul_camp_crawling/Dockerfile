FROM python:3.10

RUN mkdir /data
WORKDIR /data

COPY requirements.txt crawling_seoul_camp.py .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ['python','crawling_seoul_camp.py']