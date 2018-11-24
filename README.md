# LocalPaste

LocalPaste is a lightweight pastebin which can be hosted on a RaspberryPi.

## Installation

```bash
$ git clone https://github.com/girish946/local-paste
$ cd local-paste
$ pip install -r requirements.txt
```

## Usage


```bash
$ python startLp.py --port 8000
```
Using gunicorn

```bash
$ gunicorn wsgi:app -b 0.0.0.0:8000 --workers=2
```

using Docker

```bash
# build the image
$ sudo docker-compose -f docker-compose.yml build
# run the docker container
$ sudo docker-compose -f docker-compose.yml up
```

## Settingup the tables and testing

For initial setup (ie. creating tables), once localpaste is running.

```bash
$ cd tests
$ python testLP.py
```

or go to `http://0.0.0.0:8000/api/CreateDb` from your browser.
