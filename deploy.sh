#!/bin/bash

REMOTE_SERVER= 13.201.134.103
REMOTE_USER= ubuntu
APP_PATH=/home/ubuntu/python


rsync -avz --exclude='.git' ./ ${ubuntu}@${13.201.134.103}:${/home/ubuntu/python}


ssh ${ubuntu}@${13.201.134.103} 'sudo systemctl restart python'

