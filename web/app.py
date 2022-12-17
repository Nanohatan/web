import json
import os
import random

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
    
    j = os.environ('GS_JSON')

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