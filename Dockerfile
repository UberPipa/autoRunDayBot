FROM python:3.11.4-alpine3.18
ENV BOT_NAME=$BOT_NAME
WORKDIR /usr/src/app/"${BOT_NAME:-tg_bot}"
COPY requirements.txt /usr/src/app/"${BOT_NAME:-tg_bot}"
RUN pip install -r /usr/src/app/"${BOT_NAME:-tg_bot}"/requirements.txt
COPY . /usr/src/app/"${BOT_NAME:-tg_bot}"
CMD ["python", "run.py"]
