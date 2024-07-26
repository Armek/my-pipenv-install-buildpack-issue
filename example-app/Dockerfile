FROM python:3.11

COPY ./ ./app

WORKDIR ./app

RUN pip install pipenv
RUN pipenv sync

CMD ["pipenv", "run", "python", "main.py"]