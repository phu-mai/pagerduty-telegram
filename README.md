# PAGERDUTY-ALERTS-TELEGRAM
## Overview

    The script will export an alerts from pagerduty.con page to telegram channel with telegram_bot
## Technology

    The script was writen by Python languge
## Requirements

1. python2.7 or newest
2. python module
    1. `json`
    2. `requests`
    3. `time`
    4. `os`
    5. `pypd`
3. GETTING A TELEGRAM KEY PAIR  
    URL: https://www.assistanz.com/get-server-notification-telegram-app/
4. GETTING A PAGERDUTY ACCESS KEY  
    URL : https://support.pagerduty.com/v1/docs/using-the-api

## Quick start

1. git clone https://github.com/phu-mai/pagerduty-telegram.git

2. cd pagerduty-telegram

3. Change the environment at the list.env file  
    TELEGRAM_ID=`your telegramid`  
    TELEGRAM_TOKEN=`telegram token`  
    SUBDOMAIN=`something`  
    API_ACCESS_KEY=`your api access key from pagerduty`  

4. docker build  -f Dockerfile .

5. docker run -d -it `image you have been created`

6. and enjoy the app