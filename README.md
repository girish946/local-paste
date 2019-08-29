# LocalPaste

LocalPaste is a lightweight pastebin which can be hosted on a RaspberryPi.

## Installation

```bash
$ git clone https://github.com/girish946/local-paste
$ cd local-paste
$ pip install -r requirements.txt
```

If you are using `pipenv`, the instructions are as follows.
```bash
$ git clone https://github.com/girish946/local-paste
$ cd local-paste
$ pipenv install
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

You can build the docker image.

```bash
# build the image
$ sudo docker-compose -f docker-compose.yml build
# run the docker container
$ sudo docker-compose -f docker-compose.yml up
```

Or you can pull the docker image from [docker hub](https://hub.docker.com/r/girish946/local-paste)
using

```bash
$ docker pull girish946/local-paste
```

## Settingup the tables and testing

For initial setup (ie. creating tables), once localpaste is running.

```bash
$ cd tests
$ python testLP.py
```

or go to `http://0.0.0.0:8000/api/CreateDb` from your browser.

## Features

* Create, Update, Search and Delete the pastes.
* Syntax heighlighting while viewing a paste.
* Copy the paste to clipboard from the gui.
* REST API.
* Can be hosted on a low power machine like (RaspberryPi/OrangePi).

## TODO

Please take a look at [Issues](https://github.com/girish946/local-paste/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement).
For the TODO list.

## Contributing.

Bugs and feature requests can be made via [GitHub
issues](https://github.com/girish946/local-paste/issues).

Pull requests are also welcome via git.

LocalPaste uses [the Black python code formatter](https://github.com/python/black)
to keep coding style consistent; you may wish to have it installed to make pull
requests easier.
