FROM python:3.7-alpine
RUN pip install --upgrade pip
RUN mkdir /db
RUN chmod 775 /db
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
# CMD ["python", "startLp.py"]
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000", "--workers=2"]
