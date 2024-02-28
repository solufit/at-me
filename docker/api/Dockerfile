FROM python:3.12
WORKDIR /server
COPY ../../. /server
RUN pip install -r /server/api/requirements.txt
RUN pip install -r /server/auth/requirements.txt