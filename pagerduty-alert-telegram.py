#!/usr/bin/env python
import json
import requests
from time import sleep, time
import os
import pypd
from pprint import pprint

class telegram(object):
    def __init__(self):
        self.telegram_id  = os.environ['TELEGRAM_ID']
        self.telegram_token = os.environ['TELEGRAM_TOKEN']
        self.telegram_url = 'https://api.telegram.org/bot{0}/sendMessage?chat_id={1}&text='.format(self.telegram_token, self.telegram_id)

    def telegramSendAMessage (self, message,status,severity,summary):
        try:
            message = self.telegram_url + "`LINK "+ str(message) +" STATUS ["+ str(status) +"]  SEVERITY ["+ str(severity)+ "] SUMMARY =======> ["+str(summary)+"]"
            sendMessage = requests.get(message)
            return sendMessage
        except Exception as e:
            print ("Unexpected error from telegram: {0}".format(e))
        

class pagerduty(telegram):
    import pypd
    def __init__(self):
        super().__init__()
        self.subdomain = os.environ['SUBDOMAIN']
        self.api_access_key = os.environ['API_ACCESS_KEY']
        self.pypd.api_key = os.environ['API_ACCESS_KEY']
        self.headers = {
            'Authorization': 'Token token={0}'.format(self.api_access_key),
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.pagerduty+json;version=2',            
        }
        self.pagerduty_url = 'https://{0}.pagerduty.com/api/v1/alerts'.format(self.subdomain)
        self.triggered_incidents = pypd.Incident.find(statuses=['resolved', ])

    def pagerdutyTriggerIncident(self):
        try:
            while True:
                incidents = pypd.Incident.find(statuses=['resolved', ])
                if len(incidents) == len(self.triggered_incidents):
                    break

            triggered_ids = [i['id'] for i in self.triggered_incidents]
            incident_ids = [i['id'] for i in incidents]
            new_ids = set(triggered_ids).union(set(incident_ids))
            new_incidents = list(filter(lambda i: i['id'] in new_ids, incidents))
            new_incident = new_incidents[0]
            alerts = new_incident.alerts()
            alert = alerts[0]
            self.telegramSendAMessage(alert['html_url'],alert['status'],alert['severity'],alert['summary'])

        except Exception as e:
            print ("Unexpected error from pagerduty: {0}".format(e))
            


def main ():
    alerts = pagerduty().pagerdutyTriggerIncident()

if __name__ == "__main__":
    main()