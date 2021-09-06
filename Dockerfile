
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN pip install pymysql
RUN pip install sqlalchemy
RUN pip install cryptography
