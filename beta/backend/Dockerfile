# base image
FROM python:3.10

# mv directory
WORKDIR /python

# COPY files
COPY app.py .
COPY mongo.py .
COPY requirements.txt .

# RUN command
RUN pip install -r requirements.txt

# open port
EXPOSE 3000

# CMD python
CMD ["python","app.py"]