#! /bin/bash
while true; do
    while true; do
        status=`ps -efww | grep -w "pagerduty-alert-telegram.py" | awk -vpid=$$ '$2 != pid { print $2 }'`
        if [ ! -z "$status" ]; then
            break
        else
            `python /app/pagerduty-alert-telegram.py &`
        fi
    done
done