#!/bin/bash


echo "push script is running $(date)" >> /Users/ekoegler/Desktop/daffodil-log.txt
/usr/local/bin/pixlet render /Users/ekoegler/Documents/ermako/daffodil/daffodil.star

export TIDBYT_API_TOKEN="eyJhbGciOiJFUzI1NiIsImtpZCI6IjY1YzFhMmUzNzJjZjljMTQ1MTQyNzk5ODZhMzYyNmQ1Y2QzNTI0N2IiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJodHRwczovL2FwaS50aWRieXQuY29tIiwiZXhwIjozMjgwNTE0MzIxLCJpYXQiOjE3MDM3MTQzMjEsImlzcyI6Imh0dHBzOi8vYXBpLnRpZGJ5dC5jb20iLCJzdWIiOiIySXRZM3pyc3Y2ZGZIdE5RZktvc0dkZEo5MzUyIiwic2NvcGUiOiJkZXZpY2UiLCJkZXZpY2UiOiJ0cml1bXBoYW50bHktY3VsdHVyZWQtcGVyY2VwdGl2ZS1udXRoYXRjaC1iYjIifQ._ytxAc0OVvvQwoGEgTsj4FeT-si92twmSSG083-xjqR8Vnk2Vg8srvwqTjl49SxylIncMI0wdSMfrY34L8N2qQ"

/usr/local/bin/pixlet push "triumphantly-cultured-perceptive-nuthatch-bb2" /Users/ekoegler/Documents/ermako/daffodil/daffodil.webp >> /Users/ekoegler/Desktop/daffodil-log.txt
