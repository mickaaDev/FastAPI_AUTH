FROM python:3.6

WORKDIR /usr/src/app
ADD req.txt .

RUN apt-get update

# Installing dependencies
RUN pip3 install bottle
RUN pip3 install pillow
RUN apt-get install -y \
    python-setuptools \
    openssh-server \
    openssh-client \
    x11-xserver-utils \
    sudo

# Adding pagan user in order to be able to connect through ssh (user: pagan, pass: pagan)
RUN useradd -m pagan && echo "pagan:pagan" | chpasswd && adduser pagan sudo


RUN /usr/local/bin/python3 -m pip install --upgrade pip

RUN pip install -r req.txt

CMD [ "uvicorn", "main:apps", "--reload", "--host", "0.0.0.0", "--port", "8000"]
