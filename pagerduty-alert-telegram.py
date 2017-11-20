#!/usr/bin/env python
import json
import requests
import time
import os

class telegram_export(object):
    def __init__(self):
        self.telegram_id  = os.environ['TELEGRAM_ID']
        self.telegram_token = os.environ['TELEGRAM_TOKEN']
        self.telegram_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text='.format(self.telegram_token, self.telegram_id)

    def sendTelegramMessage (self, message,status,severity,summary):
        message = self.telegram_url + "`LINK "+ str(message) +" STATUS ["+ str(status) +"]  SEVERITY ["+ str(severity)+ "] SUMMARY =======> ["+str(summary)+"]"
        sendMessage = requests.get(message)
        return sendMessage


class pagerduty(telegram_export):
    def __init__(self):
        super().__init__()
        self.subdomain = os.environ['SUBDOMAIN']
        self.api_access_key = os.environ['API_ACCESS_KEY']
        self.headers = {
            'Authorization': 'Token token={0}'.format(self.api_access_key),
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.pagerduty+json;version=2',            
        }
        self.pagerduty_url = 'https://{0}.pagerduty.com/api/v1/alerts'.format(self.subdomain)

    def get_alerts(self):
        alerts = requests.get(self.pagerduty_url, headers=self.headers)
        return alerts.json()

    def pagerduty_alerts (self):
        pagerduty_data = self.get_alerts()
        last_textchat = (None)
        while True: 
            for alert in pagerduty_data['alerts']:
                # if alert['status'] == 'resolved':
                if alert['status'] == 'acknowledged' or alert['status'] == 'triggered' :
                    self.sendTelegramMessage(alert['html_url'],alert['status'],alert['severity'],alert['summary'])
                time.sleep(0.5)
            time.sleep (300)


def main ():
    alerts = pagerduty().pagerduty_alerts()

if __name__ == "__main__":
    main()