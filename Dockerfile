FROM python:latest
MAINTAINER phu.mai@nfq.com
ADD . /app
WORKDIR /app
ENV TELEGRAM_ID='295837768'\
    TELEGRAM_TOKEN='460566288:AAF9-ni1EkSgVtm18d1dUIaZI0iszmbFJrw'\
    SUBDOMAIN='hotelquickly'\
    API_ACCESS_KEY='PZE_McWbnHWEr-57Fnqu'
RUN  pip install -r requirements.txt
CMD ["python", "paygerduty-alert-telegram.py"]
