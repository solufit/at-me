FROM python:3.12
WORKDIR /server
COPY ../../. /server
RUN pip install -r /server/api/requirements.txt
CMD [ "python", "/server/api/main.py" ]