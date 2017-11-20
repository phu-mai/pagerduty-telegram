FROM python:latest
ADD . /app
WORKDIR /app
ENV TELEGRAM_ID='2958377683'\
    TELEGRAM_TOKEN='460566288:AAF9-ni1EkSgVtm18d1dUIaZI0iszmbFJra'\
    SUBDOMAIN='something'\
    API_ACCESS_KEY='PZA_McWbnHWEr-57Fnqu'
RUN  pip install -r requirements.txt
CMD ["python", "paygerduty-alert-telegram.py"]
