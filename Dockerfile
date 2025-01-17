FROM python:3.11.2
ADD . /
RUN pip3 install python-telegram-bot
RUN pip3 install requests
ADD main.py /
CMD [ "python", "./main.py" ]