#! /bin/bash
virtualenv -p python3 env && source env/bin/activate && pip install --upgrade pip && pip install -r requirements.txt
