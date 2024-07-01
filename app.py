# I'm still learning python. 
# Made by @Quinny-J
# 01/07/2024

# if you have it installed but get an error run the last line in term
# pip install requests
# python -m pip install requests

# References 
# Flask - https://flask.palletsprojects.com/en/3.0.x/
# OS Lib - https://docs.python.org/3/library/os.html
# Requests LIB - https://requests.readthedocs.io/en/latest/
# Discord Webhook Lib - https://pypi.org/project/discord-webhook/#basic-webhook

import os
from flask import Flask, request, render_template

app = Flask(__name__)


# Class is being used to store multiple vars in a catagory in this case strings
class statusColors:
    OKCYAN = '\033[96m' # Python likes ANSI :)
    WARN = '\033[91m'
    WHITE = '\033[0m'

# Class is being used to store multiple vars in a catagory in this case fstrings
class statusMsg:
    UI = f'\033[0m[{statusColors.OKCYAN}UI{statusColors.WHITE}]'
    OK = f'\033[0m[{statusColors.OKCYAN}OK{statusColors.WHITE}]'
    WARN = f'\033[0m[{statusColors.WARN}WARN{statusColors.WHITE}]'

@app.route('/')
def do_index():
    return render_template('index.html')

@app.route("/find/", methods=['POST', 'GET'])
def do_command():
    command_user = request.form.get('steam_id')
    response_data = os.popen(command_user).read()
    return render_template('index.html', response_data=response_data, command_user=command_user) 