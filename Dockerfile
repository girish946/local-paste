FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
#CMD ["python", "startLp.py"]
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:8000", "--workers=2"]
