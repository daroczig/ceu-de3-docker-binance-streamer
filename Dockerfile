FROM python:3-alpine

RUN apk add python python-dev py-pip py-requests py-cffi py-cryptography py-twisted gcc musl-dev
RUN python2 -m pip install python-binance
ADD binance-websocket-to-stdout.py /root/binance-websocket-to-stdout.py
CMD [ "python2", "/root/binance-websocket-to-stdout.py" ]
