FROM python:3
RUN mkdir /code
WORKDIR /code
COPY ./src/ .

# RUN npm install

RUN pip install -r requirements.txt