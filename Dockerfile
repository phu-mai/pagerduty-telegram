FROM python:latest
ADD . /app
WORKDIR /app
ENV TELEGRAM_ID='TELEGRAM_ID'\
    TELEGRAM_TOKEN='TELEGRAM_TOKEN'\
    SUBDOMAIN='something'\
    API_ACCESS_KEY='API_ACCESS_KEY'
RUN apt-get update && apt-get -y  install cron && pip install -r requirements.txt
RUN chmod +x /app/check_service.sh
CMD ["bash", "/app/check_service.sh", "&"]
