import json
import os
import random
import sys

from flask import Flask, render_template, send_from_directory, url_for
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

@app.route('/')
def hello():
    return 'こんこん!'

@app.route('/wadai_deck')
def wadai_page():
    return render_template('wadai_deck.html')

@app.route('/gs')
def connect_gspread():
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    
    j ={
        "type": "service_account",
        "project_id": os.environ['project_id'],
        "private_key_id": os.environ['private_key_id'],
        "private_key": os.environ['private_key'],
        "client_email": os.environ['client_email'],
        "client_id": os.environ['client_id'],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": os.environ['client_x509_cert_url'],
        }
    sys.stdout.write(j)


    credentials = ServiceAccountCredentials.from_json_keyfile_dict(j, scope)
    spread_sheet_id = "1_CBVgPVmPohr3ksuQP3sJe6Z5xiGmN0bcUQ23vJHsw0"
    
    #https://developers.google.com/sheets/api/guides/values#apps-script
    service = build('sheets', 'v4', credentials=credentials)

    result = service.spreadsheets().values().get(
        spreadsheetId=spread_sheet_id, range='A2:A').execute()
    wadai_list = result.get('values', [])
    random_wadai_list = random.sample(wadai_list,3)
    return render_template('wadai_deck.html',random_wadai_list=random_wadai_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)