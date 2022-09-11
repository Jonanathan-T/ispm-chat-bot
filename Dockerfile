FROM ghcr.io/iteam-s/ampalibe

ADD . /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ampalibe -p $PORT run